import unittest
from datetime import date

from _bootstrap import ROOT  # noqa: F401
from legal_ai_recursal.calendario import adicionar_dias_uteis


class CalendarioTests(unittest.TestCase):
    def test_pula_fim_de_semana(self):
        self.assertEqual(
            adicionar_dias_uteis(date(2026, 11, 6), 1, set()),
            date(2026, 11, 9),
        )

    def test_respeita_feriado_fornecido(self):
        self.assertEqual(
            adicionar_dias_uteis(date(2026, 11, 6), 1, {date(2026, 11, 9)}),
            date(2026, 11, 10),
        )


if __name__ == "__main__":
    unittest.main()
