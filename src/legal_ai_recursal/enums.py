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
    ED_APRESENTADO = "ED_APRESENTADO"


class FonteValorMaterial(StrEnum):
    VALOR_EXATO = "VALOR_EXATO"
    ESTIMATIVA_INICIAL = "ESTIMATIVA_INICIAL"
    NAO_INFORMADO = "NAO_INFORMADO"


class RotaAnalise(StrEnum):
    REVISAO_RECURSAL = "REVISAO_RECURSAL_RECOMENDADA"
    JUSTIFICATIVA_NAO_RECURSO = "JUSTIFICATIVA_NAO_RECURSO"
    RETORNO_ORIGEM = "RETORNO_ORIGEM"
    REVISAO_ECONOMICA_HUMANA = "REVISAO_ECONOMICA_HUMANA"


class TipoRegistro(StrEnum):
    DECISAO_1_GRAU = "REGISTRO_DECISÃO_1_GRAU"
    ACORDAO = "REGISTRO_ACÓRDÃO"
    CUMPRIMENTO = "REGISTRO_CUMPRIMENTO"
    NAO_RECURSO = "REGISTRO_JUSTIFICATIVA_NÃO_RECURSO"
    RETORNO_ORIGEM = "REGISTRO_RETORNO_ORIGEM"
