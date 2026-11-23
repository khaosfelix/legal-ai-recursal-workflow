import unittest
from copy import deepcopy

from _bootstrap import ROOT  # noqa: F401
from legal_ai_recursal.models import CasoEntrada
from legal_ai_recursal.validacao import validar_caso


BASE = {
    "id_caso": "T-VALID",
    "fase": "sentenca",
    "resultado_decisao": "procedente",
    "data_intimacao": "2026-11-03",
    "data_analise": "2026-11-04",
}


class ValidacaoTests(unittest.TestCase):
    def test_rejeita_valor_negativo(self):
        payload = deepcopy(BASE)
        payload["dano_moral"] = "-1"
        with self.assertRaises(ValueError):
            validar_caso(CasoEntrada.from_dict(payload))

    def test_rejeita_analise_anterior_a_intimacao(self):
        payload = deepcopy(BASE)
        payload["data_analise"] = "2026-11-02"
        with self.assertRaises(ValueError):
            validar_caso(CasoEntrada.from_dict(payload))

    def test_rejeita_anulacao_fora_de_acordao(self):
        payload = deepcopy(BASE)
        payload["resultado_decisao"] = "anulado"
        payload["decisao_anulada"] = True
        with self.assertRaises(ValueError):
            validar_caso(CasoEntrada.from_dict(payload))


if __name__ == "__main__":
    unittest.main()
