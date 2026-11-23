from decimal import Decimal, ROUND_HALF_UP

from .enums import FonteValorMaterial
from .models import AnaliseFinanceira

ZERO = Decimal("0.00")
CENT = Decimal("0.01")


def moeda(v: Decimal) -> Decimal:
    return v.quantize(CENT, rounding=ROUND_HALF_UP)


def analisar_financeiro(
    dano_moral: Decimal,
    dano_material_exato: Decimal,
    estimativa_material: Decimal,
    percentual_honorarios: Decimal,
    honorarios_fixos: Decimal,
    outras_verbas: Decimal,
    compensacao: Decimal,
) -> AnaliseFinanceira:
    if dano_material_exato > ZERO:
        material = moeda(dano_material_exato)
        fonte = FonteValorMaterial.VALOR_EXATO
    elif estimativa_material > ZERO:
        material = moeda(estimativa_material)
        fonte = FonteValorMaterial.ESTIMATIVA
    else:
        material = ZERO
        fonte = FonteValorMaterial.NAO_INFORMADO

    if honorarios_fixos > ZERO:
        honorarios = moeda(honorarios_fixos)
    else:
        base = dano_moral + material
        honorarios = moeda(base * (percentual_honorarios / Decimal("100")))

    exposicao = moeda(dano_moral + material + honorarios + outras_verbas)

    return AnaliseFinanceira(
        dano_material=material,
        fonte_material=fonte,
        honorarios=honorarios,
        exposicao_bruta=exposicao,
        compensacao=moeda(compensacao),
    )
