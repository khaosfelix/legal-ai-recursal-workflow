from dataclasses import dataclass
from decimal import Decimal, ROUND_HALF_UP

from .enums import FonteValorMaterial


CENTAVOS = Decimal("0.01")
ZERO = Decimal("0.00")


def moeda(valor: Decimal) -> Decimal:
    return valor.quantize(CENTAVOS, rounding=ROUND_HALF_UP)


@dataclass(frozen=True)
class ApuracaoMaterial:
    valor: Decimal
    fonte: FonteValorMaterial


def apurar_dano_material(
    valor_exato: Decimal,
    estimativa_inicial: Decimal,
) -> ApuracaoMaterial:
    if valor_exato > ZERO:
        return ApuracaoMaterial(moeda(valor_exato), FonteValorMaterial.VALOR_EXATO)

    if estimativa_inicial > ZERO:
        return ApuracaoMaterial(
            moeda(estimativa_inicial),
            FonteValorMaterial.ESTIMATIVA_INICIAL,
        )

    return ApuracaoMaterial(ZERO, FonteValorMaterial.NAO_INFORMADO)


def calcular_honorarios(
    dano_moral: Decimal,
    dano_material: Decimal,
    percentual: Decimal,
    valor_fixo: Decimal,
) -> Decimal:
    if valor_fixo > ZERO:
        return moeda(valor_fixo)

    base = dano_moral + dano_material
    return moeda(base * (percentual / Decimal("100")))


def calcular_exposicao_bruta(
    dano_moral: Decimal,
    dano_material: Decimal,
    honorarios: Decimal,
    outras_verbas: Decimal,
) -> Decimal:
    """
    A compensação não entra nesta função.
    No demo ela é exibida separadamente para preservar rastreabilidade.
    """
    return moeda(dano_moral + dano_material + honorarios + outras_verbas)
