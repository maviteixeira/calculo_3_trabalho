"""Figuras 3D (Plotly) das estruturas e dos pontos do Monte Carlo."""

import numpy as np
import plotly.graph_objects as go

from volulab.models.base import Solido


def figura_solido(solido: Solido) -> go.Figure:
    """Desenha o sólido em 3D a partir de `solido.malha()`.

    Entrada: qualquer `Solido`.
    Saída: `go.Figure` com um traço `go.Mesh3d` (x, y, z, i, j, k da malha),
    eixos rotulados em metros e proporção real (`aspectmode="data"`), para
    que um cômodo 8 × 5 × 3 não apareça como cubo.

    Exemplo esperado: `figura_solido(ComodoRetangular(8, 5, 3))` mostra uma
    caixa com x de 0 a 8, y de 0 a 5 e z de 0 a 3.
    """
    # TODO(#6) — Rayssa
    raise NotImplementedError("figura_solido: Issue #6")


def figura_monte_carlo(solido: Solido, pontos: np.ndarray, dentro: np.ndarray) -> go.Figure:
    """Desenha o sólido e os pontos sorteados pelo Monte Carlo.

    Entradas:
        solido: o `Solido` avaliado.
        pontos: array (N, 3) com as coordenadas x, y, z (m) — ver
            `ResultadoMonteCarlo.pontos`.
        dentro: array booleano (N,), True para pontos dentro do sólido.

    Saída: `go.Figure` com o sólido semitransparente e dois traços
    `go.Scatter3d`: pontos dentro (uma cor) e fora (outra cor), com legenda.
    Para não travar o navegador, desenhar no máximo alguns milhares de
    pontos (amostra dos N), mesmo que o cálculo use 200.000.
    """
    # TODO(#6) — Rayssa
    raise NotImplementedError("figura_monte_carlo: Issue #6")
