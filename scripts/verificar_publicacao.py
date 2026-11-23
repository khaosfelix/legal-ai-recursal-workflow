"""Scanner simples para reduzir risco de publicar segredos ou dados reais."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]

IGNORADOS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".pytest_cache",
}

EXTENSOES = {".py", ".md", ".json", ".yml", ".yaml", ".toml", ".txt", ".svg"}

PADROES = {
    "chave OpenAI": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "token GitHub": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "chave privada": re.compile(r"BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY"),
    "CNJ aparente": re.compile(r"\b\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}\b"),
    "CPF aparente": re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"),
}

problemas = []

for arquivo in ROOT.rglob("*"):
    if not arquivo.is_file():
        continue
    if any(parte in IGNORADOS for parte in arquivo.parts):
        continue
    if arquivo.suffix.lower() not in EXTENSOES:
        continue

    texto = arquivo.read_text(encoding="utf-8", errors="ignore")
    for nome, padrao in PADROES.items():
        if padrao.search(texto):
            problemas.append(f"{arquivo.relative_to(ROOT)}: padrão suspeito ({nome})")

if problemas:
    print("Falha na verificação de publicação:")
    for problema in problemas:
        print(f"- {problema}")
    sys.exit(1)

print("Verificação de publicação concluída: nenhum padrão sensível detectado.")
