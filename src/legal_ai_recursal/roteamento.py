from .enums import FaseProcessual, RotaAnalise, StatusPrazo, TipoRegistro


# Critérios deliberadamente sintéticos.
CRITERIOS_RECURSAIS_DEMO = {
    "questao_compensacao",
    "questao_prescricao",
    "questao_repeticao_dobro",
    "questao_registro_regulatorio",
    "questao_dano_elevado",
}


def definir_rota(
    fase: FaseProcessual,
    criterios: tuple[str, ...],
    status_ed: StatusPrazo,
    decisao_anulada: bool,
) -> RotaAnalise:
    if decisao_anulada:
        return RotaAnalise.RETORNO_ORIGEM

    if fase == FaseProcessual.ACORDAO and status_ed == StatusPrazo.ULTRAPASSADO:
        return RotaAnalise.JUSTIFICATIVA_NAO_RECURSO

    if set(criterios) & CRITERIOS_RECURSAIS_DEMO:
        return RotaAnalise.REVISAO_RECURSAL

    return RotaAnalise.REVISAO_ECONOMICA_HUMANA


def definir_tipo_registro(
    fase: FaseProcessual,
    rota: RotaAnalise,
) -> TipoRegistro:
    if rota == RotaAnalise.JUSTIFICATIVA_NAO_RECURSO:
        return TipoRegistro.NAO_RECURSO

    if rota == RotaAnalise.RETORNO_ORIGEM:
        return TipoRegistro.RETORNO_ORIGEM

    if fase == FaseProcessual.ACORDAO:
        return TipoRegistro.ACORDAO

    if fase == FaseProcessual.CUMPRIMENTO:
        return TipoRegistro.CUMPRIMENTO

    return TipoRegistro.DECISAO_1_GRAU
