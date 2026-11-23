from datetime import date, timedelta

from .enums import StatusPrazo


PRAZO_ED_DIAS_UTEIS_DEMO = 5


def eh_dia_util(data: date, feriados: set[date] | None = None) -> bool:
    feriados = feriados or set()
    return data.weekday() < 5 and data not in feriados


def adicionar_dias_uteis(
    inicio: date,
    quantidade: int,
    feriados: set[date] | None = None,
) -> date:
    if quantidade < 0:
        raise ValueError("A quantidade de dias úteis não pode ser negativa.")

    feriados = feriados or set()
    atual = inicio
    contados = 0

    while contados < quantidade:
        atual += timedelta(days=1)
        if eh_dia_util(atual, feriados):
            contados += 1

    return atual


def calcular_prazo_ed(
    data_intimacao: date,
    feriados: set[date] | None = None,
) -> date:
    return adicionar_dias_uteis(
        data_intimacao,
        PRAZO_ED_DIAS_UTEIS_DEMO,
        feriados,
    )


def status_prazo_ed(
    data_analise: date,
    prazo_ed: date,
    ed_interposto: bool,
) -> StatusPrazo:
    if ed_interposto:
        return StatusPrazo.ED_APRESENTADO
    if data_analise > prazo_ed:
        return StatusPrazo.ULTRAPASSADO
    return StatusPrazo.ABERTO
