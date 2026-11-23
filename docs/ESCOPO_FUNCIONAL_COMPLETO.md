# Escopo funcional — versão sanitizada

A automação foi construída para apoiar análise recursal massificada do início ao cadastro.

## Entrada e leitura

- recebimento dos autos;
- identificação da decisão candidata;
- confirmação humana;
- classificação entre sentença, acórdão e cumprimento;
- leitura de inicial, defesa, subsídios, réplica, documentos, decisões, recursos, contrarrazões, acórdãos e ED;
- separação entre alegação, prova e conclusão judicial.

## Análise jurídica e probatória

- produto/objeto da demanda;
- prescrição e impacto por parcelas;
- contratação;
- elementos de autenticação;
- rastreamento de crédito e movimentação;
- proveito econômico;
- compensação/dedução;
- estornos e recomposição;
- repetição simples/dobrada quando aplicável;
- danos materiais e morais;
- honorários e sucumbência;
- solidariedade;
- obrigação de fazer;
- índices e juros;
- risco e fragilidade probatória;
- matéria para ED;
- matéria para recurso subsequente.

## Prazos e trânsito

- cálculo de ED;
- status do ED;
- cálculo de recurso subsequente;
- efeito de ED pendente sobre o restante do fluxo;
- bloqueio do trânsito por prazo/recurso aberto;
- trânsito certificado;
- trânsito estimado;
- linha formatada para cadastro.

## Posicionamento recursal

- instrumento candidato;
- teses prioritárias;
- prova relevante;
- riscos;
- objetivo da reforma;
- justificativa de não interposição quando não há via útil/recomendada.

## Calculadora recursal externa

- a calculadora não foi criada pela automação;
- em sentença elegível, a automação prepara os campos para preenchimento;
- em acórdão, não gera calculadora;
- em cumprimento, não gera calculadora.

## Financeiro

- dano material exato;
- estimativa quando necessário;
- dano moral;
- honorários;
- demais verbas;
- compensação separada;
- exposição bruta;
- complemento em cumprimento;
- pagamento definitivo x garantia.

## Operação e cadastro

- obrigação de fazer em linguagem operacional;
- referência padronizada;
- geração de DOCX;
- bloco de dados para cadastro;
- prazo de ED;
- prazo de recurso subsequente;
- trânsito;
- providência seguinte;
- apoio ao cadastro nos sistemas jurídicos da instituição e do escritório.

## Casos especiais

- acórdão que anula/cassa sentença;
- retorno ao primeiro grau;
- cenário com contestação já apresentada;
- cenário sem contestação;
- prazo operacional após trânsito;
- decisões em cumprimento;
- complemento de depósito.

## Governança

- human-in-the-loop;
- hierarquia de fontes;
- prevenção de invenção de dados;
- distinção entre valor exato e estimado;
- distinção entre trânsito certificado e estimado;
- testes de regressão para regras críticas.

Nem todas as regras privadas da automação original aparecem no código público. A versão deste repositório foi deliberadamente simplificada para preservar confidencialidade.

## Outras rotinas operacionais

- revisão da classificação de risco e sinalização de agravamento quando necessário;
- preservação do risco já cadastrado quando não há base para alteração;
- custas recursais tratadas separadamente da condenação;
- índices/juros auditados na análise e resumidos na saída operacional;
- busca de OBF também em decisões anteriores ainda vigentes;
- metadado sobre existência de acordo quando disponível em fonte externa;
- seleção do tipo de registro operacional conforme fase, instância e resultado;
- justificativa de não interposição;
- mensagem resumida do caso para comunicação interna;
- gate final de consistência antes da entrega.

## Referências por fase

A automação diferencia o conteúdo da referência conforme a fase:

- sentença: referência de conhecimento + campos financeiros + calculadora externa quando aplicável;
- acórdão: referência de segundo grau, sem calculadora externa;
- cumprimento: referência executiva própria, sem calculadora externa;
- acórdão anulatório: campos de condenação/OBF anterior não são transportados.

A versão pública não reproduz os nomes, códigos e templates internos usados na operação real.
