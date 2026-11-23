import unittest

from _bootstrap import ROOT  # noqa: F401
from legal_ai_recursal.enums import FaseProcessual, RotaAnalise, StatusPrazo
from legal_ai_recursal.roteamento import definir_rota


class RoteamentoTests(unittest.TestCase):
    def test_anulacao_tem_prioridade(self):
        rota = definir_rota(
            FaseProcessual.ACORDAO,
            ("questao_compensacao",),
            StatusPrazo.ULTRAPASSADO,
            True,
        )
        self.assertEqual(rota, RotaAnalise.RETORNO_ORIGEM)

    def test_acordao_com_ed_ultrapassado_vai_para_nao_recurso(self):
        rota = definir_rota(
            FaseProcessual.ACORDAO,
            (),
            StatusPrazo.ULTRAPASSADO,
            False,
        )
        self.assertEqual(rota, RotaAnalise.JUSTIFICATIVA_NAO_RECURSO)

    def test_criterio_recursal_aciona_revisao(self):
        rota = definir_rota(
            FaseProcessual.SENTENCA,
            ("questao_compensacao",),
            StatusPrazo.ABERTO,
            False,
        )
        self.assertEqual(rota, RotaAnalise.REVISAO_RECURSAL)

    def test_sem_criterio_vai_para_revisao_humana(self):
        rota = definir_rota(
            FaseProcessual.SENTENCA,
            (),
            StatusPrazo.ABERTO,
            False,
        )
        self.assertEqual(rota, RotaAnalise.REVISAO_ECONOMICA_HUMANA)


if __name__ == "__main__":
    unittest.main()
