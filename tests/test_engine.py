import json
import unittest
from pathlib import Path

from _bootstrap import ROOT
from legal_ai_recursal.engine import analisar_caso
from legal_ai_recursal.enums import (
    FonteValorMaterial,
    RotaAnalise,
    StatusPrazo,
)
from legal_ai_recursal.models import CasoEntrada


def carregar(nome: str) -> CasoEntrada:
    payload = json.loads(
        (ROOT / "synthetic_cases" / nome).read_text(encoding="utf-8")
    )
    return CasoEntrada.from_dict(payload)


class EngineTests(unittest.TestCase):
    def test_sentenca_fluxo_completo(self):
        saida = analisar_caso(carregar("caso_01_sentenca.json"))
        self.assertEqual(saida.exposicao_bruta.as_tuple().exponent, -2)
        self.assertEqual(str(saida.exposicao_bruta), "6820.00")
        self.assertEqual(saida.compensacao, saida.compensacao.__class__("800.00"))
        self.assertEqual(saida.rota, RotaAnalise.REVISAO_RECURSAL)
        self.assertIsNotNone(saida.obrigacao_operacional)

    def test_estimativa_material_gera_alerta(self):
        saida = analisar_caso(carregar("caso_04_estimativa_material.json"))
        self.assertEqual(
            saida.fonte_dano_material,
            FonteValorMaterial.ESTIMATIVA_INICIAL,
        )
        self.assertTrue(saida.alertas)

    def test_acordao_ultrapassado_dispara_nao_recurso(self):
        saida = analisar_caso(
            carregar("caso_02_acordao_prazo_ultrapassado.json")
        )
        self.assertEqual(saida.status_prazo_ed, StatusPrazo.ULTRAPASSADO)
        self.assertEqual(saida.rota, RotaAnalise.JUSTIFICATIVA_NAO_RECURSO)

    def test_anulado_limpa_exposicao_e_obrigacao(self):
        saida = analisar_caso(carregar("caso_03_acordao_anulado.json"))
        self.assertEqual(str(saida.exposicao_bruta), "0.00")
        self.assertEqual(str(saida.dano_material_utilizado), "0.00")
        self.assertEqual(str(saida.honorarios), "0.00")
        self.assertIsNone(saida.obrigacao_operacional)
        self.assertEqual(saida.rota, RotaAnalise.RETORNO_ORIGEM)
        self.assertIsNotNone(saida.prazo_operacional)

    def test_trilha_de_auditoria_nao_vem_vazia(self):
        saida = analisar_caso(carregar("caso_01_sentenca.json"))
        self.assertGreaterEqual(len(saida.trilha_auditoria), 4)


if __name__ == "__main__":
    unittest.main()
