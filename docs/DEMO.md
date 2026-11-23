# Roteiro de demo

## Caso 1 — sentença

```bash
python scripts/demo.py synthetic_cases/caso_01_sentenca.json
```

Mostra:
- prazo aberto;
- dano material exato;
- honorários percentuais;
- compensação separada;
- OBF operacional;
- gatilho recursal.

## Caso 2 — acórdão com prazo ultrapassado

```bash
python scripts/demo.py synthetic_cases/caso_02_acordao_prazo_ultrapassado.json
```

Mostra:
- ED ultrapassado;
- rota automática de justificativa de não recurso.

## Caso 3 — acórdão anulado

```bash
python scripts/demo.py synthetic_cases/caso_03_acordao_anulado.json
```

Mostra:
- limpeza de exposição anterior;
- remoção de obrigação anterior;
- retorno à origem;
- prazo operacional sintético.

## JSON estruturado

Após instalar o pacote:

```bash
python -m pip install -e .
legal-ai-demo synthetic_cases/caso_01_sentenca.json --json
```
