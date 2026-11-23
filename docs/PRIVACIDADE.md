# Privacidade e confidencialidade

Este repositório foi redesenhado para publicação.

## Não publicado

- documentos reais;
- autos;
- nomes de clientes;
- nomes de instituições;
- sistemas internos;
- políticas recursais privadas;
- códigos operacionais privados;
- screenshots;
- tabelas internas;
- bases de acordos;
- credenciais;
- endpoints.

## Dados sintéticos

Todos os casos em `synthetic_cases/` são inventados.

## Scanner de publicação

O script:

```bash
python scripts/verificar_publicacao.py
```

procura padrões como:
- chaves de API;
- tokens GitHub;
- chaves privadas;
- números no formato CNJ;
- CPFs formatados.

Ele é uma barreira adicional, não substitui revisão humana.

## Regra de ouro

A versão pública demonstra **método, arquitetura e engenharia**; nunca o procedimento interno de uma organização.
