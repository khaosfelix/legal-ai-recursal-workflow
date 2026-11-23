import argparse
import json
from pathlib import Path

from .engine import analisar_caso
from .formatacao import formatar_saida_texto
from .models import CasoEntrada


def criar_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="legal-ai-demo",
        description="Executa o workflow recursal sintético de portfólio.",
    )
    parser.add_argument("arquivo", type=Path, help="Caso sintético em JSON.")
    parser.add_argument(
        "--json",
        action="store_true",
        dest="saida_json",
        help="Exibe a saída estruturada em JSON.",
    )
    return parser


def main() -> None:
    args = criar_parser().parse_args()
    payload = json.loads(args.arquivo.read_text(encoding="utf-8"))
    saida = analisar_caso(CasoEntrada.from_dict(payload))

    if args.saida_json:
        print(json.dumps(saida.to_dict(), ensure_ascii=False, indent=2))
        return

    print(formatar_saida_texto(saida))


if __name__ == "__main__":
    main()
