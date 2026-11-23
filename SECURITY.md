# Segurança

Não envie dados reais em issues ou pull requests.

Antes de publicar:

```powershell
python -m unittest discover -s tests -v
python scripts/verificar_publicacao.py
```
