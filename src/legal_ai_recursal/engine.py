from . import VERSAO_REGRAS
from .calendario import adicionar_dias_uteis, calcular_prazo_ed, status_prazo_ed
from .enums import ResultadoDecisao, RotaAnalise
from .financeiro import (
    apurar_dano_material,
    calcular_exposicao_bruta,
    calcular_honorarios,
)
from .models import CasoEntrada, SaidaAnalise
from .obrigacoes import formatar_obrigacao
from .roteamento import definir_rota, definir_tipo_registro
from .validacao import validar_caso


ROTULOS_DECISAO = {
    ResultadoDecisao.PROCEDENTE: "PROCEDENTE",
    ResultadoDecisao.PARCIALMENTE_PROCEDENTE: "PARCIALMENTE PROCEDENTE",
    ResultadoDecisao.IMPROCEDENTE: "IMPROCEDENTE",
    ResultadoDecisao.PROVIDO: "PROVIDO",
    ResultadoDecisao.PARCIALMENTE_PROVIDO: "PARCIALMENTE PROVIDO",
    ResultadoDecisao.DESPROVIDO: "DESPROVIDO",
    ResultadoDecisao.NAO_CONHECIDO: "NÃO CONHECIDO",
    ResultadoDecisao.ANULADO: "PROVIDO",
}


def analisar_caso(caso: CasoEntrada) -> SaidaAnalise:
    validar_caso(caso)

    trilha: list[str] = []
    alertas: list[str] = []

    feriados = set(caso.feriados)
    prazo_ed = calcular_prazo_ed(caso.data_intimacao, feriados)
    status_ed = status_prazo_ed(caso.data_analise, prazo_ed, caso.ed_interposto)
    trilha.append(
        f"Prazo ED calculado em 5 dias úteis: {prazo_ed.isoformat()} ({status_ed.value})."
    )

    material = apurar_dano_material(
        caso.dano_material_exato,
        caso.estimativa_material_inicial,
    )
    trilha.append(
        f"Dano material: {material.fonte.value} no valor de {material.valor:.2f}."
    )

    if material.fonte.value == "ESTIMATIVA_INICIAL":
        alertas.append(
            "Dano material estimado a partir do valor sintético informado na pretensão inicial."
        )

    honorarios = calcular_honorarios(
        caso.dano_moral,
        material.valor,
        caso.percentual_honorarios,
        caso.honorarios_fixos,
    )
    trilha.append(f"Honorários calculados: {honorarios:.2f}.")

    exposicao = calcular_exposicao_bruta(
        caso.dano_moral,
        material.valor,
        honorarios,
        caso.outras_verbas_efetivas,
    )
    trilha.append(
        "Exposição bruta calculada sem abatimento da compensação; "
        f"compensação registrada separadamente em {caso.compensacao:.2f}."
    )

    rota = definir_rota(
        caso.fase,
        caso.criterios_recursais,
        status_ed,
        caso.decisao_anulada,
    )
    trilha.append(f"Rota selecionada: {rota.value}.")

    tipo_registro = definir_tipo_registro(caso.fase, rota)
    obrigacao = formatar_obrigacao(caso.obrigacao)

    proxima_providencia = None
    prazo_operacional = None

    if rota == RotaAnalise.RETORNO_ORIGEM:
        # Uma decisão anulada não deve carregar efeitos pecuniários/OBF da decisão anterior.
        material_valor = material.valor * 0
        exposicao = exposicao * 0
        honorarios = honorarios * 0
        obrigacao = None

        trilha.append(
            "Decisão anulada: exposição e obrigação anteriores foram removidas da saída."
        )

        if caso.data_transito:
            dias = 1 if caso.contestacao_apresentada else 15
            prazo_operacional = adicionar_dias_uteis(
                caso.data_transito,
                dias,
                feriados,
            )
            proxima_providencia = (
                "VERIFICAR_COMPLEMENTO_DEFESA"
                if caso.contestacao_apresentada
                else "AGENDAR_DEFESA_E_SUBSIDIOS"
            )
            trilha.append(
                f"Prazo operacional sintético calculado a partir do trânsito: "
                f"{prazo_operacional.isoformat()}."
            )
        else:
            alertas.append(
                "Decisão anulada sem data de trânsito: prazo operacional não foi calculado."
            )
    else:
        material_valor = material.valor

    return SaidaAnalise(
        id_caso=caso.id_caso,
        versao_regras=VERSAO_REGRAS,
        decisao=ROTULOS_DECISAO[caso.resultado_decisao],
        prazo_ed=prazo_ed,
        status_prazo_ed=status_ed,
        dano_material_utilizado=material_valor,
        fonte_dano_material=material.fonte,
        honorarios=honorarios,
        compensacao=caso.compensacao,
        exposicao_bruta=exposicao,
        rota=rota,
        tipo_registro=tipo_registro,
        obrigacao_operacional=obrigacao,
        proxima_providencia=proxima_providencia,
        prazo_operacional=prazo_operacional,
        alertas=tuple(alertas),
        trilha_auditoria=tuple(trilha),
    )


def analisar_dict(payload: dict) -> dict:
    return analisar_caso(CasoEntrada.from_dict(payload)).to_dict()
