# 0003 — `ResultadoMonteCarlo` carrega os pontos sorteados

- **Data:** 24/09/2026
- **Status:** proposta (revisar com Marcelly na Issue #7 e Rayssa na Issue #6)
- **Quem decidiu:** Maria Vitória (coordenação)

## Contexto
O resultado do Monte Carlo foi definido com `volume_estimado`, `n_amostras`, `n_dentro`, `volume_caixa` e `erro_padrao`. Mas `figura_monte_carlo(solido, pontos, dentro)` precisa dos pontos sorteados e da marcação dentro/fora. A função original da Marcelly já devolvia `x, y, z, pontos_dentro`.

## Decisão
`ResultadoMonteCarlo` ganhou dois campos opcionais: `pontos` (array N × 3) e `dentro` (array booleano N). Eles ficam fora do `repr` para não poluir a saída.

## Por quê
- Evita sortear os pontos duas vezes (uma para calcular e outra para desenhar), o que poderia mostrar no gráfico pontos diferentes dos usados no cálculo.
- Com 200.000 amostras o custo de memória é pequeno (~5 MB).
