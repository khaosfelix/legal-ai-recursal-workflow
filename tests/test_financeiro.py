import unittest
from decimal import Decimal

from _bootstrap import ROOT  # noqa: F401
from legal_ai_recursal.financeiro import analisar_financeiro


class FinanceiroTests(unittest.TestCase):
    def test_compensacao_nao_reduz_bruto(self):
        f = analisar_financeiro(
            Decimal("5000"), Decimal("1200"), Decimal("0"),
            Decimal("10"), Decimal("0"), Decimal("0"), Decimal("800")
        )
        self.assertEqual(str(f.exposicao_bruta), "6820.00")
        self.assertEqual(str(f.compensacao), "800.00")

    def test_estimativa(self):
        f = analisar_financeiro(
            Decimal("0"), Decimal("0"), Decimal("1840.50"),
            Decimal("0"), Decimal("0"), Decimal("0"), Decimal("0")
        )
        self.assertEqual(f.fonte_material.value, "ESTIMATIVA")


if __name__ == "__main__":
    unittest.main()
