# Como apresentar em entrevista

## Pitch de 30 segundos

“Eu desenvolvi uma arquitetura de automação jurídica para um fluxo de alta repetição. O ponto central foi separar o que deveria ficar com a LLM — leitura e estruturação — do que precisava ser determinístico, como prazos, cálculos, gates e roteamento. Modelei o domínio, criei validações, trilha de auditoria e testes de regressão. Para o portfólio, reconstruí a solução com regras e dados 100% sintéticos para preservar confidencialidade.”

## Se perguntarem “onde está a IA?”

“A versão pública começa no contrato estruturado para não depender de uma API externa. O prompt e o schema da camada de extração estão documentados. Isso é intencional: consigo testar todo o core determinístico sem gastar tokens e sem acoplar o sistema a um provedor.”

## Se perguntarem “por que não deixar a LLM calcular?”

“Porque dinheiro e prazo são excelentes candidatos a código determinístico. O modelo interpreta; o software calcula e valida.”

## Se perguntarem “como você evitou regressões?”

“Transformei comportamentos críticos em testes e separei as regras em módulos. Assim uma alteração no prompt não deveria mudar silenciosamente um cálculo.”

## Competências demonstradas

- Legal Ops;
- Legal Engineering;
- modelagem de processos;
- prompt design;
- structured outputs;
- rule engines;
- Python;
- testes;
- CI;
- privacidade;
- governança de IA.
