import json
import tempfile
import unittest
from pathlib import Path

from _bootstrap import ROOT
from legal_ai_recursal.engine import analisar_caso
from legal_ai_recursal.enums import FonteTransito, RotaAnalise, StatusPrazo
from legal_ai_recursal.models import CasoEntrada


def carregar(nome):
    return CasoEntrada.from_dict(
        json.loads((ROOT / "synthetic_cases" / nome).read_text(encoding="utf-8"))
    )


class WorkflowTests(unittest.TestCase):
    def test_sentenca_gera_calculadora_externa(self):
        s = analisar_caso(carregar("caso_01_sentenca.json"))
        self.assertIsNotNone(s.calculadora_externa)
        self.assertEqual(
            s.calculadora_externa.total_moral_material,
            s.calculadora_externa.dano_moral + s.calculadora_externa.dano_material,
        )

    def test_acordao_nao_gera_calculadora(self):
        s = analisar_caso(carregar("caso_03_acordao_recurso_aberto.json"))
        self.assertIsNone(s.calculadora_externa)

    def test_cumprimento_nao_gera_calculadora(self):
        s = analisar_caso(carregar("caso_05_cumprimento.json"))
        self.assertIsNone(s.calculadora_externa)

    def test_ed_perdido_mas_recurso_aberto_nao_encerra(self):
        s = analisar_caso(carregar("caso_03_acordao_recurso_aberto.json"))
        self.assertEqual(s.prazo_ed.status, StatusPrazo.ULTRAPASSADO)
        self.assertEqual(s.prazo_recurso_subsequente.status, StatusPrazo.ABERTO)
        self.assertEqual(s.rota, RotaAnalise.REVISAO_RECURSAL)
        self.assertIsNone(s.transito.data)

    def test_transito_estimado_quando_prazos_encerram(self):
        s = analisar_caso(carregar("caso_02_acordao_encerrado.json"))
        self.assertEqual(s.transito.fonte, FonteTransito.ESTIMADO)
        self.assertEqual(s.rota, RotaAnalise.JUSTIFICATIVA_NAO_INTERPOSICAO)
        self.assertIsNotNone(s.cadastro_operacional["linha_transito_para_cadastro"])

    def test_ed_pendente_bloqueia_recurso_e_transito(self):
        s = analisar_caso(carregar("caso_06_ed_pendente.json"))
        self.assertEqual(s.prazo_ed.status, StatusPrazo.AGUARDANDO_EVENTO)
        self.assertEqual(s.prazo_recurso_subsequente.status, StatusPrazo.AGUARDANDO_EVENTO)
        self.assertIsNone(s.transito.data)

    def test_anulacao_limpa_condenacao_e_calculadora(self):
        s = analisar_caso(carregar("caso_04_acordao_anulado.json"))
        self.assertEqual(str(s.financeiro.exposicao_bruta), "0.00")
        self.assertIsNone(s.obrigacao_operacional)
        self.assertIsNone(s.calculadora_externa)
        self.assertEqual(s.rota, RotaAnalise.RETORNO_ORIGEM)
        self.assertIsNotNone(s.prazo_operacional)

    def test_execucao_complementar(self):
        s = analisar_caso(carregar("caso_05_cumprimento.json"))
        self.assertEqual(str(s.execucao.complemento), "700")
        self.assertEqual(s.execucao.tipo, "PAGAMENTO_COMPLEMENTAR")

    def test_estimativa_material(self):
        s = analisar_caso(carregar("caso_07_material_estimado.json"))
        self.assertEqual(s.financeiro.fonte_material.value, "ESTIMATIVA")
        self.assertIsNotNone(s.calculadora_externa)

    def test_docx_e_gerado(self):
        with tempfile.TemporaryDirectory() as tmp:
            s = analisar_caso(carregar("caso_01_sentenca.json"), tmp)
            self.assertTrue((Path(tmp) / s.referencia_docx).exists())

    def test_posicionamento_tem_recurso(self):
        s = analisar_caso(carregar("caso_01_sentenca.json"))
        self.assertIn("APELAÇÃO DEMO", s.posicionamento)


if __name__ == "__main__":
    unittest.main()
