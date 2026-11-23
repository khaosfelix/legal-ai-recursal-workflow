# Como substituir a versão atual pela Premium

A forma mais limpa é manter o histórico Git e substituir os arquivos do repositório.

## 1. Faça uma cópia de segurança da pasta atual

Opcional, mas recomendado.

## 2. Dentro do repositório atual, remova os arquivos rastreados

```powershell
git rm -r .
```

Isso remove os arquivos do projeto, **mas mantém a pasta `.git` e o histórico**.

## 3. Copie todo o conteúdo desta versão Premium para a pasta do repositório

A pasta deve voltar a conter `README.md`, `src`, `tests`, `docs`, etc.

## 4. Confira

```powershell
git status
```

## 5. Rode os testes

```powershell
python -m unittest discover -s tests -v
```

## 6. Rode o scanner de publicação

```powershell
python scripts/verificar_publicacao.py
```

## 7. Adicione tudo

```powershell
git add .
```

## 8. Faça o commit

```powershell
git commit -m "refactor: evolui projeto para arquitetura premium de Legal AI"
```

## 9. Envie

```powershell
git push origin main
```
