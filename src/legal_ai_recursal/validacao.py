from decimal import Decimal

from .enums import FaseProcessual, ResultadoDecisao
from .models import CasoEntrada


CAMPOS_MONETARIOS = (
    "dano_moral",
    "dano_material_exato",
    "estimativa_material_inicial",
    "percentual_honorarios",
    "honorarios_fixos",
    "outras_verbas_efetivas",
    "compensacao",
)


def validar_caso(caso: CasoEntrada) -> None:
    if not caso.id_caso.strip():
        raise ValueError("id_caso é obrigatório.")

    if caso.data_analise < caso.data_intimacao:
        raise ValueError("data_analise não pode ser anterior à data_intimacao.")

    for nome in CAMPOS_MONETARIOS:
        valor: Decimal = getattr(caso, nome)
        if valor < Decimal("0"):
            raise ValueError(f"{nome} não pode ser negativo.")

    if caso.percentual_honorarios > Decimal("100"):
        raise ValueError("percentual_honorarios não pode exceder 100 no demo.")

    if caso.decisao_anulada and caso.resultado_decisao != ResultadoDecisao.ANULADO:
        raise ValueError(
            "decisao_anulada=True exige resultado_decisao='anulado'."
        )

    if (
        caso.resultado_decisao == ResultadoDecisao.ANULADO
        and caso.fase != FaseProcessual.ACORDAO
    ):
        raise ValueError("O cenário 'anulado' do demo é exclusivo de acórdão.")

    if caso.data_transito and caso.data_transito < caso.data_intimacao:
        raise ValueError("data_transito não pode ser anterior à intimação.")
