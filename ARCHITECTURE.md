# Arquitetura

## Princípio central

A arquitetura separa tarefas probabilísticas de tarefas determinísticas.

A LLM é usada para localizar informações em texto não estruturado, resumir histórico, identificar fundamentos e estruturar dados.

Código e regras determinísticas são preferidos para:
- somas;
- prazos;
- gates;
- enumerações;
- validações;
- estados;
- campos obrigatórios;
- consistência de saída.

## Camadas

### 1. Ingestão
Recebe documentos ou uma representação sintética do caso.

### 2. Extração
Converte texto em um objeto estruturado.

### 3. Classificação
Define a fase:
- `sentence`;
- `appeal_judgment`;
- `enforcement`.

### 4. Rule Engine
Executa regras públicas e sintéticas.

### 5. Deadline Engine
Calcula prazos e identifica status.

### 6. Exposure Engine
Calcula dano moral, dano material, honorários, outras verbas e exposição bruta. A compensação é registrada separadamente.

### 7. Routing
Encaminha para revisão recursal, justificativa de não recurso, retorno à origem ou revisão manual.

### 8. Validation Gate
Impede saída final se campos obrigatórios estiverem ausentes.

### 9. Human-in-the-loop
A decisão final continua sujeita à validação humana.

## Design para integração futura

```text
PDF / e-mail / API / sistema jurídico
              ↓
        NormalizedCase
              ↓
          RuleEngine
              ↓
       AnalysisOutput
              ↓
 DOCX / dashboard / API / sistema
```

## Observabilidade em produção

Eu adicionaria:
- logs estruturados;
- ID de execução;
- versão do prompt;
- versão das regras;
- razão de cada decisão;
- snapshot do input normalizado;
- diff entre sugestão e aprovação;
- métricas de erro e retrabalho.

## Testes

Os casos sintéticos cobrem:
- total financeiro;
- prazo;
- resultado decisório;
- gatilho de não recurso;
- decisão anulada;
- prevenção de regressão.
