from .models import ObrigacaoEntrada


def _capitalizar_acao(acao: str) -> str:
    acao = acao.strip()
    if not acao:
        raise ValueError("A ação da obrigação não pode ser vazia.")
    return acao[0].upper() + acao[1:]


def formatar_obrigacao(obrigacao: ObrigacaoEntrada | None) -> str | None:
    if obrigacao is None:
        return None

    texto = f"{_capitalizar_acao(obrigacao.acao)} {obrigacao.objeto.strip()}"

    if obrigacao.identificador:
        texto += f" identificada como {obrigacao.identificador.strip()}"

    if obrigacao.local:
        texto += f" na {obrigacao.local.strip()}"

    return texto.rstrip(".") + "."
