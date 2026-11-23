from enum import StrEnum


class FaseProcessual(StrEnum):
    SENTENCA = "sentenca"
    ACORDAO = "acordao"
    CUMPRIMENTO = "cumprimento"


class ResultadoDecisao(StrEnum):
    PROCEDENTE = "procedente"
    PARCIALMENTE_PROCEDENTE = "parcialmente_procedente"
    IMPROCEDENTE = "improcedente"
    PROVIDO = "provido"
    PARCIALMENTE_PROVIDO = "parcialmente_provido"
    DESPROVIDO = "desprovido"
    NAO_CONHECIDO = "nao_conhecido"
    ANULADO = "anulado"


class StatusPrazo(StrEnum):
    ABERTO = "ABERTO"
    ULTRAPASSADO = "ULTRAPASSADO"
    APRESENTADO = "APRESENTADO"
    AGUARDANDO_EVENTO = "AGUARDANDO_EVENTO"


class FonteTransito(StrEnum):
    CERTIFICADO = "CERTIFICADO"
    ESTIMADO = "ESTIMADO"
    NAO_APURADO = "NAO_APURADO"


class FonteValorMaterial(StrEnum):
    VALOR_EXATO = "VALOR_EXATO"
    ESTIMATIVA = "ESTIMATIVA"
    NAO_INFORMADO = "NAO_INFORMADO"


class RotaAnalise(StrEnum):
    REVISAO_RECURSAL = "REVISAO_RECURSAL"
    JUSTIFICATIVA_NAO_INTERPOSICAO = "JUSTIFICATIVA_NAO_INTERPOSICAO"
    RETORNO_ORIGEM = "RETORNO_ORIGEM"
    VALIDACAO_HUMANA = "VALIDACAO_HUMANA"


class TipoDeposito(StrEnum):
    PAGAMENTO_DEFINITIVO = "pagamento_definitivo"
    GARANTIA = "garantia"
