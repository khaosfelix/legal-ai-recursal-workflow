from decimal import Decimal

from .models import SaidaAnalise


def brl(valor: Decimal) -> str:
    bruto = f"{valor:,.2f}"
    return "R$ " + bruto.replace(",", "X").replace(".", ",").replace("X", ".")


def formatar_saida_texto(saida: SaidaAnalise) -> str:
    linhas = [
        f"CASO: {saida.id_caso}",
        f"VERSÃO DAS REGRAS: {saida.versao_regras}",
        f"DECISÃO: {saida.decisao}",
        f"PRAZO ED: {saida.prazo_ed.strftime('%d/%m/%Y')} — {saida.status_prazo_ed.value}",
        (
            "DANO MATERIAL: "
            f"{brl(saida.dano_material_utilizado)} — {saida.fonte_dano_material.value}"
        ),
        f"HONORÁRIOS: {brl(saida.honorarios)}",
        f"COMPENSAÇÃO: {brl(saida.compensacao)} — informada separadamente",
        f"EXPOSIÇÃO BRUTA: {brl(saida.exposicao_bruta)}",
        f"ROTA: {saida.rota.value}",
        f"REGISTRO: {saida.tipo_registro.value}",
    ]

    if saida.obrigacao_operacional:
        linhas.append(f"OBRIGAÇÃO: {saida.obrigacao_operacional}")

    if saida.proxima_providencia:
        linhas.append(f"PRÓXIMA PROVIDÊNCIA: {saida.proxima_providencia}")

    if saida.prazo_operacional:
        linhas.append(
            f"PRAZO OPERACIONAL: {saida.prazo_operacional.strftime('%d/%m/%Y')}"
        )

    if saida.alertas:
        linhas.append("ALERTAS:")
        linhas.extend(f"- {item}" for item in saida.alertas)

    linhas.append("TRILHA DE AUDITORIA:")
    linhas.extend(f"- {item}" for item in saida.trilha_auditoria)

    return "\n".join(linhas)
