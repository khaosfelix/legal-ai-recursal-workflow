# Contribuindo

Contribuições devem preservar três princípios:

1. nenhum dado real;
2. regra demonstrativa explicitamente sintética;
3. teste para qualquer alteração de comportamento.

Fluxo sugerido:

```bash
python -m unittest discover -s tests -v
python scripts/verificar_publicacao.py
```

Mudanças de arquitetura devem ser documentadas em `docs/DECISOES_DE_DESIGN.md`.
