# Prompt de extração estruturada

A camada de IA deve transformar os documentos sintéticos em um objeto compatível com o schema de entrada.

A extração procura responder:

1. qual é a decisão candidata?
2. qual a fase: sentença, acórdão ou cumprimento?
3. qual o resultado objetivo?
4. qual a data de intimação?
5. houve ED? foi julgado?
6. existe recurso subsequente candidato?
7. existe data certificada de trânsito?
8. qual a condenação vigente?
9. há valor material exato ou apenas estimativa?
10. há compensação?
11. há obrigação de fazer?
12. quais teses merecem revisão?
13. quais provas sustentam ou enfraquecem a tese?
14. quais riscos processuais precisam ser registrados?

A LLM extrai. O motor determinístico calcula datas, somas, status e gates.
