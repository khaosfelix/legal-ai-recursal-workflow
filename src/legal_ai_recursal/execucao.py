from decimal import Decimal

from .enums import TipoDeposito
from .models import AnaliseExecucao, CumprimentoEntrada

ZERO = Decimal("0.00")


def analisar_execucao(dados: CumprimentoEntrada | None) -> AnaliseExecucao | None:
    if not dados:
        return None

    complemento = dados.valor_devido - dados.valor_pago_ou_garantido
    if complemento <= ZERO:
        return AnaliseExecucao(
            complemento=ZERO,
            tipo=None,
            justificativa="Não há complemento financeiro no cenário sintético.",
        )

    if dados.tipo_deposito == TipoDeposito.GARANTIA:
        tipo = "GARANTIA_COMPLEMENTAR"
        justificativa = (
            f"Complementar a garantia em {complemento:.2f}, considerando "
            f"valor devido de {dados.valor_devido:.2f} e valor já garantido de "
            f"{dados.valor_pago_ou_garantido:.2f}."
        )
    else:
        tipo = "PAGAMENTO_COMPLEMENTAR"
        justificativa = (
            f"Complementar o pagamento em {complemento:.2f}, considerando "
            f"valor devido de {dados.valor_devido:.2f} e valor já pago de "
            f"{dados.valor_pago_ou_garantido:.2f}."
        )

    return AnaliseExecucao(
        complemento=complemento,
        tipo=tipo,
        justificativa=justificativa,
    )
