import unittest

from _bootstrap import ROOT  # noqa: F401
from legal_ai_recursal.models import CasoEntrada
from legal_ai_recursal.validacao import validar


class ValidacaoTests(unittest.TestCase):
    def test_ed_julgado_exige_nova_data(self):
        c = CasoEntrada.from_dict({
            "id_caso": "X",
            "fase": "sentenca",
            "resultado_decisao": "procedente",
            "data_intimacao": "2026-11-01",
            "data_analise": "2026-11-20",
            "ed_interposto": True,
            "ed_julgado": True,
        })
        with self.assertRaises(ValueError):
            validar(c)

    def test_valor_negativo_falha(self):
        c = CasoEntrada.from_dict({
            "id_caso": "X",
            "fase": "sentenca",
            "resultado_decisao": "procedente",
            "data_intimacao": "2026-11-01",
            "data_analise": "2026-11-20",
            "dano_moral": "-1",
        })
        with self.assertRaises(ValueError):
            validar(c)


if __name__ == "__main__":
    unittest.main()
