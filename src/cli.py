import json
import sys
from pathlib import Path
from .engine import analyze_dict

def money(value):
    return f"R$ {value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python -m src.cli <case.json>")
    payload = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    result = analyze_dict(payload)
    print(f"Caso: {result['case_id']}")
    print(f"Decisão: {result['decision_label']}")
    print(f"Prazo ED: {result['deadline_ed']} — {result['deadline_status']}")
    print(f"Danos materiais utilizados: {money(result['material_value_used'])}")
    print(f"Honorários: {money(result['fees'])}")
    print(f"Compensação: {money(result['compensation'])} — informada separadamente")
    print(f"Valor total bruto: {money(result['gross_total'])}")
    print(f"Roteamento: {result['route']}")
    print(f"Registro: {result['record_type']}")
    if result["obligation"]:
        print(f"Obrigação operacional: {result['obligation']}")
    if result["next_operational_deadline"]:
        print(f"Próximo prazo operacional: {result['next_operational_deadline']}")
    for warning in result["warnings"]:
        print(f"Aviso: {warning}")

if __name__ == "__main__":
    main()
