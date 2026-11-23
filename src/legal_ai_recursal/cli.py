import argparse
import json
from pathlib import Path

from .engine import analisar_caso
from .formatacao import formatar
from .models import CasoEntrada


def main():
    parser = argparse.ArgumentParser(description="Executa um caso sintético do Legal AI Recursal Workflow.")
    parser.add_argument("arquivo", type=Path)
    parser.add_argument("--docx-dir", type=Path, default=Path("generated"))
    args = parser.parse_args()

    payload = json.loads(args.arquivo.read_text(encoding="utf-8"))
    saida = analisar_caso(CasoEntrada.from_dict(payload), args.docx_dir)
    print(formatar(saida))


if __name__ == "__main__":
    main()
