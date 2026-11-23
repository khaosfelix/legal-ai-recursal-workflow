# Contrato de extração

A camada de LLM deve produzir um objeto compatível com `schemas/caso_entrada.schema.json`.

Exemplo:

```json
{
  "id_caso": "DEMO-001",
  "fase": "sentenca",
  "resultado_decisao": "parcialmente_procedente",
  "data_intimacao": "2026-11-03",
  "data_analise": "2026-11-06",
  "data_transito": null,
  "dano_moral": "5000.00",
  "dano_material_exato": "1200.00",
  "estimativa_material_inicial": "0.00",
  "percentual_honorarios": "10",
  "honorarios_fixos": "0.00",
  "outras_verbas_efetivas": "0.00",
  "compensacao": "800.00",
  "criterios_recursais": ["questao_compensacao"],
  "ed_interposto": false,
  "decisao_anulada": false,
  "contestacao_apresentada": true,
  "feriados": [],
  "obrigacao": {
    "acao": "cancelar a",
    "objeto": "cesta de serviços",
    "identificador": "DEMO-PACOTE",
    "local": "conta fictícia da parte autora"
  }
}
```

O contrato é deliberadamente simples para permitir adaptação a qualquer provedor de LLM com structured outputs.
