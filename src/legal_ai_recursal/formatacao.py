from decimal import Decimal

from .models import SaidaAnalise


def brl(v: Decimal) -> str:
    s = f"{v:,.2f}"
    return "R$ " + s.replace(",", "X").replace(".", ",").replace("X", ".")


def data_br(v):
    return v.strftime("%d/%m/%Y") if v else "NÃO APURADO"


def formatar(saida: SaidaAnalise) -> str:
    recurso = saida.prazo_recurso_subsequente

    linhas = [
        f"CASO: {saida.id_caso}",
        f"DECISÃO: {saida.decisao}",
        "",
        f"ED: {data_br(saida.prazo_ed.data_fatal)} — {saida.prazo_ed.status.value}",
    ]

    if recurso:
        linhas += [
            f"RECURSO SUBSEQUENTE: {recurso.nome}",
            f"PRAZO: {data_br(recurso.data_fatal)} — {recurso.status.value}",
        ]
    else:
        linhas.append("RECURSO SUBSEQUENTE: NÃO INFORMADO")

    linhas += [
        f"TRÂNSITO: {data_br(saida.transito.data)} — {saida.transito.fonte.value}",
        "",
        f"DANO MATERIAL: {brl(saida.financeiro.dano_material)} — {saida.financeiro.fonte_material.value}",
        f"HONORÁRIOS: {brl(saida.financeiro.honorarios)}",
        f"EXPOSIÇÃO BRUTA: {brl(saida.financeiro.exposicao_bruta)}",
        f"COMPENSAÇÃO: {brl(saida.financeiro.compensacao)} — separada",
        "",
        f"ROTA: {saida.rota.value}",
        f"POSICIONAMENTO: {saida.posicionamento}",
    ]

    if saida.obrigacao_operacional:
        linhas.append(f"OBRIGAÇÃO: {saida.obrigacao_operacional}")

    if saida.calculadora_externa:
        c = saida.calculadora_externa
        linhas += [
            "",
            "CALCULADORA EXTERNA — CAMPOS PARA PREENCHIMENTO",
            f"Rito: {c.rito}",
            f"Liquidez: {c.liquidez}",
            f"UF: {c.uf}",
            f"Identificador: {c.identificador_processo}",
            f"Critérios: {', '.join(c.criterios) if c.criterios else 'Nenhum'}",
            f"Dano moral: {brl(c.dano_moral)}",
            f"Dano material: {brl(c.dano_material)}",
            f"Total moral + material: {brl(c.total_moral_material)}",
        ]

    if saida.execucao:
        linhas += [
            "",
            f"EXECUÇÃO: {saida.execucao.tipo or 'SEM COMPLEMENTO'}",
            f"Complemento: {brl(saida.execucao.complemento)}",
            f"Justificativa: {saida.execucao.justificativa}",
        ]

    if saida.referencia_docx:
        linhas += ["", f"DOCX GERADO: {saida.referencia_docx}"]

    if saida.proxima_providencia:
        linhas += [
            "",
            f"PRÓXIMA PROVIDÊNCIA: {saida.proxima_providencia}",
            f"PRAZO OPERACIONAL: {data_br(saida.prazo_operacional)}",
        ]

    if saida.cadastro_operacional.get("linha_transito_para_cadastro"):
        linhas += [
            "",
            "TRÂNSITO PARA CADASTRO:",
            saida.cadastro_operacional["linha_transito_para_cadastro"],
        ]

    if saida.alertas:
        linhas += ["", "ALERTAS:"]
        linhas.extend(f"- {x}" for x in saida.alertas)

    return "\n".join(linhas)
