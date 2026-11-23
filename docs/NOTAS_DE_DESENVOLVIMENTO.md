# Notas de desenvolvimento

O projeto foi sendo ajustado conforme os testes mostravam pontos que ainda exigiam retrabalho manual.

Algumas mudanças importantes:

- o prazo de ED deixou de depender de preenchimento manual;
- a perda do ED deixou de encerrar automaticamente a análise: o recurso subsequente passou a ser verificado antes;
- o trânsito passou a ser calculado/estimado e identificado pela fonte;
- a saída passou a fornecer a data de trânsito já formatada para cadastro;
- dano material deixou de terminar simplesmente como “a apurar” quando havia base para estimativa;
- compensação passou a ser mostrada separadamente do bruto;
- obrigação de fazer passou a ser escrita como instrução operacional;
- sentença passou a gerar os campos necessários para a calculadora externa;
- acórdão e cumprimento passaram a bloquear explicitamente essa etapa;
- a referência DOCX passou a integrar a entrega operacional;
- decisão anulada ganhou um fluxo próprio;
- cumprimento ganhou tratamento separado para complemento financeiro.

Essa evolução foi o principal motivo para retirar regras críticas do texto livre do prompt e transformá-las em componentes testáveis.
