import unittest
from datetime import date

from _bootstrap import ROOT  # noqa: F401
from legal_ai_recursal.calendario import (
    adicionar_dias_uteis,
    calcular_prazo_ed,
    status_prazo_ed,
)
from legal_ai_recursal.enums import StatusPrazo


class CalendarioTests(unittest.TestCase):
    def test_adiciona_dias_uteis_pulando_fim_de_semana(self):
        sexta = date(2026, 11, 6)
        self.assertEqual(adicionar_dias_uteis(sexta, 1), date(2026, 11, 9))

    def test_respeita_feriado_fornecido(self):
        inicio = date(2026, 11, 6)
        feriados = {date(2026, 11, 9)}
        self.assertEqual(
            adicionar_dias_uteis(inicio, 1, feriados),
            date(2026, 11, 10),
        )

    def test_prazo_ed_cinco_dias_uteis(self):
        self.assertEqual(
            calcular_prazo_ed(date(2026, 11, 3)),
            date(2026, 11, 10),
        )

    def test_status_ultrapassado(self):
        self.assertEqual(
            status_prazo_ed(
                date(2026, 11, 11),
                date(2026, 11, 10),
                False,
            ),
            StatusPrazo.ULTRAPASSADO,
        )

    def test_ed_apresentado_tem_prioridade(self):
        self.assertEqual(
            status_prazo_ed(
                date(2026, 11, 20),
                date(2026, 11, 10),
                True,
            ),
            StatusPrazo.ED_APRESENTADO,
        )


if __name__ == "__main__":
    unittest.main()
