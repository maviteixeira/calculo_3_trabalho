# 0004 — Fronteira fechada, `ValueError` e gerador com semente

- **Data:** 24/09/2026
- **Status:** proposta (Issue #3)
- **Quem decidiu:** Maria Vitória (coordenação)

## Contexto
Alguns detalhes do contrato precisavam de uma regra única para os testes serem previsíveis.

## Decisão
1. **Fronteira:** `contem()` usa intervalos fechados. Pontos na superfície contam como dentro.
2. **Erros de entrada:** parâmetros inválidos levantam `ValueError`: dimensão ≤ 0, `n_amostras` ≤ 0, `v_referencia` ≤ 0 em `erro_percentual`. A versão original de `calcular_erro_percentual` devolvia 0.0 quando a referência era 0, o que esconderia um erro como "0% de erro".
3. **Aleatoriedade:** o Monte Carlo usa `np.random.default_rng(semente)`, em vez do gerador global `np.random.uniform`. Com a mesma semente, o resultado é idêntico, e o sorteio não interfere em outras partes do programa.

## Por quê
- A fronteira tem volume zero, então a escolha não muda o resultado, só evita ambiguidade.
- Falhar alto é melhor do que mostrar um número errado na apresentação.
- Reprodutibilidade é necessária para os testes e para repetir uma demonstração ao vivo.
