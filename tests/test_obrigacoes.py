import unittest

from _bootstrap import ROOT  # noqa: F401
from legal_ai_recursal.models import ObrigacaoEntrada
from legal_ai_recursal.obrigacoes import formatar_obrigacao


class ObrigacoesTests(unittest.TestCase):
    def test_formata_obrigacao_operacional(self):
        texto = formatar_obrigacao(
            ObrigacaoEntrada(
                acao="cancelar a",
                objeto="cesta de serviços",
                identificador="DEMO-PACOTE",
                local="conta fictícia da parte autora",
            )
        )
        self.assertEqual(
            texto,
            "Cancelar a cesta de serviços identificada como DEMO-PACOTE "
            "na conta fictícia da parte autora.",
        )

    def test_none_permanece_none(self):
        self.assertIsNone(formatar_obrigacao(None))


if __name__ == "__main__":
    unittest.main()
