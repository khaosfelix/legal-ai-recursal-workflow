import unittest
from decimal import Decimal

from _bootstrap import ROOT  # noqa: F401
from legal_ai_recursal.enums import FonteValorMaterial
from legal_ai_recursal.financeiro import (
    apurar_dano_material,
    calcular_exposicao_bruta,
    calcular_honorarios,
)


class FinanceiroTests(unittest.TestCase):
    def test_valor_exato_tem_prioridade(self):
        r = apurar_dano_material(Decimal("1000"), Decimal("2500"))
        self.assertEqual(r.valor, Decimal("1000.00"))
        self.assertEqual(r.fonte, FonteValorMaterial.VALOR_EXATO)

    def test_estimativa_quando_nao_ha_valor_exato(self):
        r = apurar_dano_material(Decimal("0"), Decimal("1840.50"))
        self.assertEqual(r.valor, Decimal("1840.50"))
        self.assertEqual(r.fonte, FonteValorMaterial.ESTIMATIVA_INICIAL)

    def test_honorarios_percentuais(self):
        valor = calcular_honorarios(
            Decimal("5000"),
            Decimal("1200"),
            Decimal("10"),
            Decimal("0"),
        )
        self.assertEqual(valor, Decimal("620.00"))

    def test_honorarios_fixos_prevalecem(self):
        valor = calcular_honorarios(
            Decimal("5000"),
            Decimal("1200"),
            Decimal("10"),
            Decimal("400"),
        )
        self.assertEqual(valor, Decimal("400.00"))

    def test_exposicao_nao_recebe_compensacao(self):
        total = calcular_exposicao_bruta(
            Decimal("5000"),
            Decimal("1200"),
            Decimal("620"),
            Decimal("0"),
        )
        self.assertEqual(total, Decimal("6820.00"))


if __name__ == "__main__":
    unittest.main()
