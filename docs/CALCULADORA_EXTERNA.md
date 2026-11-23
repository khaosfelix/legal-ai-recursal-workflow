# Calculadora recursal externa

A calculadora recursal não foi desenvolvida neste projeto.

Ela já existia como ferramenta da instituição financeira.

A automação foi criada para diminuir o trabalho manual de preenchimento: depois de analisar uma sentença elegível, ela entrega os campos processuais, jurídicos e financeiros necessários para que a usuária preencha a ferramenta externa.

No repositório público, essa etapa é representada por `calculadora_externa.py`.

O módulo:
- não calcula a decisão econômica da ferramenta institucional;
- não reproduz a interface real;
- não reproduz critérios privados;
- apenas estrutura campos sintéticos para demonstrar a integração do workflow com uma ferramenta já existente.

Regra de fase:
- sentença: pode gerar campos para preenchimento;
- acórdão: não gera;
- cumprimento/execução: não gera.
