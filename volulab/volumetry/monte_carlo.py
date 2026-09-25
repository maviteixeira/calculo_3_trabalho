"""Volume por Monte Carlo e comparação com o volume analítico.

Lógica original de Marcelly (src/calculus.py, `monte_Carlo`), adaptada ao
contrato `Solido`: a caixa e a função de pertencimento vêm do próprio sólido.
"""

from dataclasses import dataclass, field

import numpy as np

from volulab.models.base import Solido


@dataclass
class ResultadoMonteCarlo:
    """Resultado de uma estimativa de volume por Monte Carlo.

    - volume_estimado: Vcaixa · Ndentro / Ntotal (m³)
    - n_amostras: total de pontos sorteados (Ntotal)
    - n_dentro: pontos que caíram dentro do sólido (Ndentro)
    - volume_caixa: volume da caixa delimitadora (m³)
    - erro_padrao: incerteza estatística da estimativa (m³)
    - pontos: array (n_amostras, 3) com os pontos sorteados, para o gráfico
    - dentro: array booleano (n_amostras,), True para os pontos dentro
    """

    volume_estimado: float
    n_amostras: int
    n_dentro: int
    volume_caixa: float
    erro_padrao: float
    pontos: np.ndarray | None = field(default=None, repr=False)
    dentro: np.ndarray | None = field(default=None, repr=False)


def estimar_volume(
    solido: Solido, n_amostras: int, semente: int | None = None
) -> ResultadoMonteCarlo:
    """Estima o volume do sólido sorteando pontos na caixa delimitadora.

    Método: sorteia `n_amostras` pontos uniformes na caixa, conta quantos
    caem dentro do sólido (`solido.contem`) e usa a proporção:

        Vobj ≈ Vcaixa · Ndentro / Ntotal

    O erro padrão vem da distribuição binomial, com p = Ndentro / Ntotal:

        erro_padrao = Vcaixa · √(p · (1 − p) / Ntotal)

    Entradas:
        solido: qualquer `Solido` (usa caixa_delimitadora e contem).
        n_amostras: nº de pontos sorteados (> 0).
        semente: fixa o gerador aleatório; mesma semente → mesmo resultado.

    Exemplo esperado: cômodo 8 × 5 × 3, 100.000 amostras → volume ≈ 120 m³
    com erro percentual abaixo de 2%.
    """
    # TODO(#7) — Marcelly: revisar e validar a adaptação
    if n_amostras <= 0:
        raise ValueError(f"n_amostras deve ser maior que zero (recebido: {n_amostras})")

    gerador = np.random.default_rng(semente)
    (xmin, xmax), (ymin, ymax), (zmin, zmax) = solido.caixa_delimitadora()
    x = gerador.uniform(xmin, xmax, n_amostras)
    y = gerador.uniform(ymin, ymax, n_amostras)
    z = gerador.uniform(zmin, zmax, n_amostras)

    dentro = np.asarray(solido.contem(x, y, z), dtype=bool)
    n_dentro = int(np.sum(dentro))

    v_caixa = solido.volume_caixa()
    p = n_dentro / n_amostras
    return ResultadoMonteCarlo(
        volume_estimado=v_caixa * p,
        n_amostras=n_amostras,
        n_dentro=n_dentro,
        volume_caixa=v_caixa,
        erro_padrao=v_caixa * float(np.sqrt(p * (1 - p) / n_amostras)),
        pontos=np.column_stack((x, y, z)),
        dentro=dentro,
    )


def erro_percentual(v_estimado: float, v_referencia: float) -> float:
    """Erro percentual da estimativa em relação ao volume de referência.

        Erro (%) = |Vest − Vref| / Vref × 100

    Exemplo: erro_percentual(110, 100) -> 10.0

    Levanta ValueError se v_referencia ≤ 0 (a divisão não faria sentido).
    """
    if v_referencia <= 0:
        raise ValueError(f"v_referencia deve ser maior que zero (recebido: {v_referencia})")
    return abs(v_estimado - v_referencia) * 100 / v_referencia
