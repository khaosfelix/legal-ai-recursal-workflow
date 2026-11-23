from pathlib import Path

from .calendario import adicionar_dias_uteis
from .calculadora_externa import gerar_campos_calculadora
from .docx_renderer import gerar_docx
from .enums import FonteTransito, RotaAnalise, StatusPrazo
from .execucao import analisar_execucao
from .financeiro import analisar_financeiro
from .models import AnaliseFinanceira, CasoEntrada, SaidaAnalise
from .obrigacoes import formatar_obrigacao
from .posicionamento import gerar_posicionamento
from .recursos import analisar_ed, analisar_recurso_subsequente, apurar_transito
from .validacao import validar

ROTULOS = {
    "procedente": "PROCEDENTE",
    "parcialmente_procedente": "PARCIALMENTE PROCEDENTE",
    "improcedente": "IMPROCEDENTE",
    "provido": "PROVIDO",
    "parcialmente_provido": "PARCIALMENTE PROVIDO",
    "desprovido": "DESPROVIDO",
    "nao_conhecido": "NÃO CONHECIDO",
    "anulado": "PROVIDO",
}


def analisar_caso(caso: CasoEntrada, pasta_docx: str | Path | None = None) -> SaidaAnalise:
    validar(caso)
    feriados = set(caso.feriados)
    alertas: list[str] = []

    ed = analisar_ed(caso, feriados)
    recurso = analisar_recurso_subsequente(caso, feriados)
    transito = apurar_transito(caso, ed, recurso, feriados)

    financeiro = analisar_financeiro(
        caso.dano_moral,
        caso.dano_material_exato,
        caso.estimativa_material,
        caso.percentual_honorarios,
        caso.honorarios_fixos,
        caso.outras_verbas,
        caso.compensacao,
    )

    obrigacao = formatar_obrigacao(caso.obrigacao)
    calculadora = gerar_campos_calculadora(caso, financeiro)
    execucao = analisar_execucao(caso.cumprimento)
    posicionamento = gerar_posicionamento(caso, ed, recurso)

    if caso.decisao_anulada:
        financeiro = AnaliseFinanceira(
            dano_material=financeiro.dano_material * 0,
            fonte_material=financeiro.fonte_material,
            honorarios=financeiro.honorarios * 0,
            exposicao_bruta=financeiro.exposicao_bruta * 0,
            compensacao=financeiro.compensacao,
        )
        obrigacao = None
        calculadora = None
        execucao = None
        rota = RotaAnalise.RETORNO_ORIGEM
    elif caso.recomendar_recurso and (
        ed.status == StatusPrazo.ABERTO
        or (recurso and recurso.status == StatusPrazo.ABERTO)
    ):
        rota = RotaAnalise.REVISAO_RECURSAL
    elif (
        ed.status == StatusPrazo.ULTRAPASSADO
        and (not recurso or recurso.status == StatusPrazo.ULTRAPASSADO)
        and not caso.recomendar_recurso
    ):
        rota = RotaAnalise.JUSTIFICATIVA_NAO_INTERPOSICAO
    else:
        rota = RotaAnalise.VALIDACAO_HUMANA

    proxima_providencia = None
    prazo_operacional = None
    if caso.decisao_anulada and transito.data:
        dias = 1 if caso.contestacao_apresentada else 15
        prazo_operacional = adicionar_dias_uteis(transito.data, dias, feriados)
        proxima_providencia = (
            "VERIFICAR_COMPLEMENTO_DA_CONTESTACAO"
            if caso.contestacao_apresentada
            else "AGENDAR_CONTESTACAO_E_SUBSIDIOS"
        )

    cadastro = {
        "data_intimacao": caso.data_intimacao.strftime("%d/%m/%Y"),
        "prazo_ed": ed.data_fatal.strftime("%d/%m/%Y") if ed.data_fatal else None,
        "status_ed": ed.status.value,
        "recurso_subsequente": recurso.nome if recurso else None,
        "prazo_recurso_subsequente": (
            recurso.data_fatal.strftime("%d/%m/%Y") if recurso and recurso.data_fatal else None
        ),
        "status_recurso_subsequente": recurso.status.value if recurso else None,
        "data_transito": transito.data.strftime("%d/%m/%Y") if transito.data else None,
        "fonte_transito": transito.fonte.value,
        "linha_transito_para_cadastro": (
            f"1. DATA: {transito.data.strftime('%d/%m/%Y')}." if transito.data else None
        ),
        "rota": rota.value,
    }

    docx_name = None
    if pasta_docx is not None:
        caminho = Path(pasta_docx) / f"referencia_{caso.id_caso}.docx"
        linhas = [
            f"1. Data da intimação: {cadastro['data_intimacao']}",
            f"2. Decisão: {ROTULOS[caso.resultado_decisao.value]}",
            f"3. Posicionamento: {posicionamento}",
            f"4. Obrigação de fazer: {obrigacao or 'Não há.'}",
            f"5. Exposição bruta: {financeiro.exposicao_bruta:.2f}",
            f"Prazo de ED: {cadastro['prazo_ed'] or 'Não apurado'} — {cadastro['status_ed']}",
            f"Prazo do recurso subsequente: {cadastro['prazo_recurso_subsequente'] or 'Não aplicável'}",
            f"Trânsito: {cadastro['data_transito'] or 'Não apurado'} — {cadastro['fonte_transito']}",
        ]
        gerar_docx(caminho, linhas)
        docx_name = caminho.name

    if financeiro.fonte_material.value == "ESTIMATIVA":
        alertas.append("Dano material apresentado como estimativa no cenário sintético.")

    if transito.fonte == FonteTransito.ESTIMADO:
        alertas.append("Trânsito estimado; validar certidão/expediente em operação real.")

    return SaidaAnalise(
        id_caso=caso.id_caso,
        decisao=ROTULOS[caso.resultado_decisao.value],
        prazo_ed=ed,
        prazo_recurso_subsequente=recurso,
        transito=transito,
        financeiro=financeiro,
        rota=rota,
        posicionamento=posicionamento,
        obrigacao_operacional=obrigacao,
        calculadora_externa=calculadora,
        execucao=execucao,
        cadastro_operacional=cadastro,
        referencia_docx=docx_name,
        proxima_providencia=proxima_providencia,
        prazo_operacional=prazo_operacional,
        alertas=tuple(alertas),
    )
