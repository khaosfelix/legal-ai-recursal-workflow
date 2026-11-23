import unicodedata

from .enums import StatusPrazo
from .models import AnalisePrazo, CasoEntrada


def _normalizar(texto: str) -> str:
    return "".join(
        c for c in unicodedata.normalize("NFD", texto.lower())
        if unicodedata.category(c) != "Mn"
    )


def gerar_posicionamento(
    caso: CasoEntrada,
    prazo_ed: AnalisePrazo,
    prazo_recurso: AnalisePrazo | None,
) -> str:
    if caso.decisao_anulada:
        return "A decisão foi anulada; seguir fluxo de retorno à origem."

    if not caso.recomendar_recurso:
        return (
            "Não foi marcado fundamento suficiente para recomendação recursal automática; "
            "validar dispensa e providência de cadastro."
        )

    instrumento = None
    if prazo_ed.status == StatusPrazo.ABERTO and any(
        "omissao" in _normalizar(x) or "contradicao" in _normalizar(x)
        for x in caso.teses_prioritarias
    ):
        instrumento = "Embargos de Declaração"
    elif prazo_recurso and prazo_recurso.status == StatusPrazo.ABERTO:
        instrumento = prazo_recurso.nome

    if not instrumento:
        return (
            "Há matéria para revisão, mas nenhum instrumento configurado está aberto no "
            "cenário sintético."
        )

    teses = "; ".join(caso.teses_prioritarias) or "teses identificadas na análise"
    provas = "; ".join(caso.provas_relevantes) or "provas relevantes dos autos"
    riscos = "; ".join(caso.riscos_recursais) or "riscos processuais e probatórios"

    return (
        f"Recomenda-se revisar a interposição de {instrumento}. "
        f"Priorizar: {teses}. Confrontar com: {provas}. "
        f"Registrar como riscos: {riscos}."
    )
