# Decisões de design

## ADR-001 — Separar LLM de cálculos

**Decisão:** prazos e dinheiro ficam no código.

**Motivo:** são operações que precisam ser reproduzíveis, testáveis e auditáveis.

## ADR-002 — Usar `Decimal`

**Decisão:** evitar `float` para valores monetários.

**Motivo:** reduzir artefatos binários e tornar arredondamento explícito.

## ADR-003 — Regras sintéticas isoladas

**Decisão:** critérios demonstrativos ficam em `roteamento.py` e `knowledge_demo`.

**Motivo:** não misturar regra privada, prompt e código.

## ADR-004 — Entrada normalizada por JSON

**Decisão:** a versão pública começa após a etapa de extração documental.

**Motivo:** permitir execução sem API externa e testar o core sem custo de LLM.

## ADR-005 — Decisão anulada tem prioridade

**Decisão:** a anulação limpa exposição e obrigação anteriores antes do roteamento comum.

**Motivo:** demonstrar um gate de consistência que impede transportar estado inválido.

## ADR-006 — Compensação separada

**Decisão:** compensação não reduz a exposição bruta demonstrativa.

**Motivo:** preservar rastreabilidade do valor total e do ajuste em campos distintos.

## ADR-007 — Human-in-the-loop obrigatório

**Decisão:** nenhuma rota é apresentada como decisão jurídica final.

**Motivo:** domínio de alto impacto exige revisão humana e contexto processual completo.
