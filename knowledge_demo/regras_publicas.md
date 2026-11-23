# Regras públicas e sintéticas

> Estas regras existem somente para demonstrar arquitetura. Elas não reproduzem política de empresa, cliente ou escritório.

## Prazo de ED

No cenário de demonstração:
- prazo: 5 dias úteis;
- o dia da intimação não é contado;
- o primeiro dia útil seguinte é o dia 1;
- sábados, domingos e feriados fornecidos ao motor são excluídos.

O projeto não consulta calendário forense oficial.

## Dano material

Prioridade:
1. valor exato;
2. estimativa sintética informada na pretensão inicial;
3. zero, com fonte `NAO_INFORMADO`.

A fonte do valor acompanha a saída.

## Honorários

No demo:
- valor fixo prevalece sobre percentual;
- percentual incide sobre `dano moral + dano material`;
- dinheiro é calculado com `Decimal`.

## Exposição bruta

```text
dano moral
+ dano material
+ honorários
+ outras verbas efetivas
= exposição bruta
```

Compensação é exibida separadamente e não reduz esse total demonstrativo.

## Critérios recursais fictícios

- `questao_compensacao`
- `questao_prescricao`
- `questao_repeticao_dobro`
- `questao_registro_regulatorio`
- `questao_dano_elevado`

A presença de qualquer um desses critérios roteia o caso para revisão recursal, exceto quando outra regra de maior prioridade se aplica.

## Acórdão com prazo ultrapassado

No demo, acórdão com prazo de ED ultrapassado e sem ED apresentado é roteado para `JUSTIFICATIVA_NAO_RECURSO`.

## Decisão anulada

Tem prioridade sobre os demais gates:
- rota para retorno à origem;
- exposição anterior zerada;
- obrigação anterior removida;
- se houver data de trânsito, o demo calcula prazo operacional sintético:
  - 1 dia útil quando já houve defesa;
  - 15 dias úteis quando não houve defesa.

Esses prazos são regras de demonstração, não instruções jurídicas oficiais.
