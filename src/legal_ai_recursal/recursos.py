from datetime import date

from .calendario import analisar_prazo, proximo_dia_util
from .enums import FonteTransito, StatusPrazo
from .models import AnalisePrazo, AnaliseTransito, CasoEntrada

PRAZO_ED_DEMO = 5


def analisar_ed(caso: CasoEntrada, feriados: set[date]) -> AnalisePrazo:
    if caso.ed_interposto and not caso.ed_julgado:
        return AnalisePrazo(
            nome="Embargos de Declaração",
            data_fatal=None,
            status=StatusPrazo.AGUARDANDO_EVENTO,
        )

    base = (
        caso.data_intimacao_pos_ed
        if caso.ed_interposto and caso.ed_julgado and caso.data_intimacao_pos_ed
        else caso.data_intimacao
    )
    return analisar_prazo(
        nome="Embargos de Declaração",
        data_base=base,
        dias_uteis=PRAZO_ED_DEMO,
        data_analise=caso.data_analise,
        apresentado=caso.ed_interposto,
        feriados=feriados,
    )


def analisar_recurso_subsequente(caso: CasoEntrada, feriados: set[date]) -> AnalisePrazo | None:
    recurso = caso.recurso_subsequente
    if recurso is None:
        return None

    if caso.ed_interposto and not caso.ed_julgado:
        return AnalisePrazo(
            nome=recurso.nome,
            data_fatal=None,
            status=StatusPrazo.AGUARDANDO_EVENTO,
        )

    data_base = (
        caso.data_intimacao_pos_ed
        if caso.ed_interposto and caso.ed_julgado and caso.data_intimacao_pos_ed
        else recurso.data_base or caso.data_intimacao
    )

    return analisar_prazo(
        nome=recurso.nome,
        data_base=data_base,
        dias_uteis=recurso.prazo_dias_uteis,
        data_analise=caso.data_analise,
        apresentado=recurso.interposto,
        feriados=feriados,
    )


def apurar_transito(
    caso: CasoEntrada,
    ed: AnalisePrazo,
    recurso: AnalisePrazo | None,
    feriados: set[date],
) -> AnaliseTransito:
    if caso.data_transito_certificada:
        return AnaliseTransito(
            data=caso.data_transito_certificada,
            fonte=FonteTransito.CERTIFICADO,
            observacao="Data certificada no caso sintético.",
        )

    bloqueadores = {
        StatusPrazo.ABERTO,
        StatusPrazo.APRESENTADO,
        StatusPrazo.AGUARDANDO_EVENTO,
    }

    if ed.status in bloqueadores:
        return AnaliseTransito(
            data=None,
            fonte=FonteTransito.NAO_APURADO,
            observacao="Há ED ou prazo de ED que impede apuração do trânsito.",
        )

    if recurso and recurso.status in bloqueadores:
        return AnaliseTransito(
            data=None,
            fonte=FonteTransito.NAO_APURADO,
            observacao="Há recurso subsequente aberto, apresentado ou dependente de evento.",
        )

    datas = [x.data_fatal for x in (ed, recurso) if x and x.data_fatal]
    if not datas:
        return AnaliseTransito(
            data=None,
            fonte=FonteTransito.NAO_APURADO,
            observacao="Não há base suficiente para estimar o trânsito.",
        )

    ultimo_prazo = max(datas)
    if caso.data_analise <= ultimo_prazo:
        return AnaliseTransito(
            data=None,
            fonte=FonteTransito.NAO_APURADO,
            observacao="Ainda existe prazo relevante em curso.",
        )

    return AnaliseTransito(
        data=proximo_dia_util(ultimo_prazo, feriados),
        fonte=FonteTransito.ESTIMADO,
        observacao="Estimativa operacional após o encerramento dos prazos configurados.",
    )
