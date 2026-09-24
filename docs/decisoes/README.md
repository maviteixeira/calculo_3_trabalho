# Registro de decisões

Toda decisão que muda o rumo do projeto (estrutura, tecnologia, convenção) vira um arquivo curto nesta pasta. O objetivo é que qualquer pessoa entenda, depois, **por que** algo é do jeito que é.

- Nome do arquivo: `NNNN-titulo-curto.md` (ex.: `0001-pacote-volulab.md`).
- Uma decisão por arquivo. Se ela mudar, crie uma nova decisão que substitui a anterior; não apague a antiga.

## Modelo

```markdown
# NNNN — Título da decisão

- **Data:** DD/MM/AAAA
- **Status:** proposta | aceita | substituída por NNNN
- **Quem decidiu:** nomes

## Contexto
Qual era o problema ou a dúvida.

## Decisão
O que foi decidido, em uma ou duas frases.

## Por quê
Motivos e alternativas descartadas.
```

## Decisões

| Nº | Decisão | Status |
|---|---|---|
| [0001](0001-pacote-volulab.md) | Código em um pacote `volulab/` com contrato `Solido` | proposta |
| [0002](0002-sem-sympy-no-mvp.md) | SymPy fora da stack do MVP | proposta |
| [0003](0003-pontos-no-resultado-monte-carlo.md) | `ResultadoMonteCarlo` carrega os pontos sorteados | proposta |
| [0004](0004-convencoes-do-contrato.md) | Fronteira fechada, `ValueError` e gerador com semente | proposta |
