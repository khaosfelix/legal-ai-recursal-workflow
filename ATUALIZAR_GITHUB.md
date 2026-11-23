# Atualizar o repositório

Dentro da pasta que já está conectada ao GitHub:

```powershell
git status
git rm -r .
```

Copie todo o conteúdo desta versão para a pasta do repositório.

Depois:

```powershell
git add .
python -m unittest discover -s tests -v
python scripts/verificar_publicacao.py
git status
git commit -m "feat: completa fluxo de análise e cadastro recursal"
git push origin main
```

O commit descreve a mudança funcional sem termos de marketing ou referência ao processo de montagem do portfólio.
