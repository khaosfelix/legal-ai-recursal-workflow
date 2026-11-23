# Checklist antes de publicar

- [ ] Nenhum nome de cliente ou escritório.
- [ ] Nenhum número real de processo ou contrato.
- [ ] Nenhum dado pessoal.
- [ ] Nenhum sistema ou código interno.
- [ ] Nenhum manual, política, tabela ou screenshot privado.
- [ ] Nenhuma chave, token, senha ou endpoint.
- [ ] Casos continuam identificados como sintéticos.
- [ ] Regras continuam descritas como fictícias.
- [ ] Histórico do Git não contém arquivos confidenciais.

## Busca local
```bash
git grep -niE "empresa-real|cliente-real|sistema-interno|codigo-interno"
```

Se algo sensível tiver sido commitado, apagar depois não basta: o conteúdo permanece no histórico.
