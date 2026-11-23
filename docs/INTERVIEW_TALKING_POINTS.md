# Pontos para entrevista

## Em 30 segundos
“Eu desenvolvi uma automação de Legal AI para um fluxo jurídico de alto volume. A parte mais importante foi não deixar tudo na responsabilidade do modelo: usei a LLM para ler e estruturar informação, mas coloquei cálculos, prazos, gates e roteamento em regras determinísticas. Também construí validações, outputs padronizados e testes de regressão. A versão pública foi totalmente sanitizada e usa apenas dados sintéticos.”

## Desafio técnico
Evitar regressões quando novas regras eram adicionadas.

## Solução
- separar prompt, knowledge e regras;
- usar hierarquia de fontes;
- criar máquina de estados;
- definir contratos de entrada/saída;
- criar gates finais;
- testar cenários de regressão.

## Privacidade
“A versão pública mantém a arquitetura, mas substitui nomes, políticas, códigos, documentos e casos por equivalentes sintéticos.”
