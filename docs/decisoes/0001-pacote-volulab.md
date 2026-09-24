# 0001 — Código em um pacote `volulab/` com contrato `Solido`

- **Data:** 24/09/2026
- **Status:** proposta (Issue #3, aguardando revisão do PR)
- **Quem decidiu:** Maria Vitória (coordenação)

## Contexto
O código estava em `src/` (arquivos quase vazios, mais o Monte Carlo da Marcelly em `src/calculus.py`). Havia também uma proposta na branch `chore/reestrutura-conforme-pdf`, com pastas soltas na raiz (`models/`, `utils/`, `volumetry/`, `visualization/`).

## Decisão
Todo o código fica no pacote `volulab/` (`models/`, `utils/`, `volumetry/`, `visualization/`), com `app.py` na raiz. Toda estrutura implementa a classe abstrata `Solido`. A pasta `src/` foi removida, e o Monte Carlo foi portado para `volulab/volumetry/monte_carlo.py`. A branch `chore/reestrutura-conforme-pdf` fica substituída por esta estrutura.

## Por quê
- Um pacote único evita conflito de nomes (`utils`, `models` são nomes genéricos) e permite `from volulab.models import ...` em qualquer lugar, inclusive nos testes.
- O contrato `Solido` permite que Monte Carlo e visualização funcionem com qualquer estrutura nova (Nível 4) sem alteração.
- A divisão de pastas por responsável foi mantida, igual à proposta anterior.
