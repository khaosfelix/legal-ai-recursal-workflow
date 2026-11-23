from datetime import date, timedelta

from .enums import StatusPrazo
from .models import AnalisePrazo


def eh_dia_util(data: date, feriados: set[date]) -> bool:
    return data.weekday() < 5 and data not in feriados


def adicionar_dias_uteis(inicio: date, quantidade: int, feriados: set[date]) -> date:
    atual = inicio
    contados = 0
    while contados < quantidade:
        atual += timedelta(days=1)
        if eh_dia_util(atual, feriados):
            contados += 1
    return atual


def proximo_dia_util(data: date, feriados: set[date]) -> date:
    return adicionar_dias_uteis(data, 1, feriados)


def analisar_prazo(
    nome: str,
    data_base: date,
    dias_uteis: int,
    data_analise: date,
    apresentado: bool,
    feriados: set[date],
) -> AnalisePrazo:
    data_fatal = adicionar_dias_uteis(data_base, dias_uteis, feriados)
    if apresentado:
        status = StatusPrazo.APRESENTADO
    elif data_analise > data_fatal:
        status = StatusPrazo.ULTRAPASSADO
    else:
        status = StatusPrazo.ABERTO
    return AnalisePrazo(nome=nome, data_fatal=data_fatal, status=status)
