from .models import ObrigacaoEntrada


def formatar_obrigacao(obrigacao: ObrigacaoEntrada | None) -> str | None:
    if not obrigacao:
        return None

    partes = [obrigacao.acao.strip().capitalize(), obrigacao.objeto.strip()]

    if obrigacao.identificador:
        partes.append(f"identificada como {obrigacao.identificador.strip()}")

    texto = " ".join(partes)

    if obrigacao.local:
        texto += f" na {obrigacao.local.strip()}"

    return texto.rstrip(".") + "."
