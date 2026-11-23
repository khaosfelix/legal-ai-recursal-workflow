# Como subir este projeto para o GitHub

## Opção recomendada — Git

1. Crie um repositório vazio no GitHub com o nome:
   `legal-ai-recursal-workflow`

2. Não marque opções para criar README, .gitignore ou licença, porque esses arquivos já existem aqui.

3. Extraia esta pasta no seu computador.

4. Abra o terminal dentro da pasta `legal-ai-recursal-workflow`.

5. Execute:

```bash
git init
git add .
git commit -m "feat: publish sanitized Legal AI workflow demo"
git branch -M main
git remote add origin https://github.com/SEU-USUARIO/legal-ai-recursal-workflow.git
git push -u origin main
```

6. Abra o repositório no GitHub e confira se o README apareceu na página inicial.

## Antes de tornar público

Confira `docs/PUBLICATION_CHECKLIST.md`.

Nunca adicione ao repositório público:
- autos reais;
- screenshots corporativos;
- prompts privados;
- políticas internas;
- planilhas ou bases internas;
- nomes de clientes;
- credenciais ou endpoints privados.
