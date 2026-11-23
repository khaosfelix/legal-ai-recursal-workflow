from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
IGNORAR = {".git", ".venv", "venv", "__pycache__"}
EXT = {".py",".md",".json",".yml",".yaml",".toml",".txt",".svg"}

PADROES = {
    "chave_api": re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b"),
    "token_github": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "chave_privada": re.compile(r"BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY"),
    "cnj": re.compile(r"\b\d{7}-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}\b"),
    "cpf": re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b"),
}

achados = []

for arquivo in ROOT.rglob("*"):
    if not arquivo.is_file():
        continue
    if any(x in IGNORAR for x in arquivo.parts):
        continue
    if arquivo.suffix.lower() not in EXT:
        continue

    texto = arquivo.read_text(encoding="utf-8", errors="ignore")
    for nome,padrao in PADROES.items():
        if padrao.search(texto):
            achados.append(f"{arquivo.relative_to(ROOT)}: {nome}")

if achados:
    print("Foram encontrados padrões que merecem revisão:")
    for x in achados:
        print("-", x)
    sys.exit(1)

print("Verificação concluída: nenhum padrão sensível detectado.")
