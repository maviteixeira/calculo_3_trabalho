"""Fórmulas analíticas de volume (volume de referência).

Cada função aqui é o resultado de uma integral resolvida à mão e documentada
em docs/matematica/. É contra estes valores que o Monte Carlo é comparado.
"""


def volume_paralelepipedo(comprimento: float, largura: float, altura: float) -> float:
    """Volume exato de um paralelepípedo reto (cômodo retangular).

    Integral tripla da função constante 1 sobre a região
        E = {(x, y, z) : 0 ≤ x ≤ comprimento, 0 ≤ y ≤ largura, 0 ≤ z ≤ altura}

        V = ∭_E 1 dV = ∫₀^comprimento ∫₀^largura ∫₀^altura 1 dz dy dx

    Entradas: comprimento, largura, altura em metros (valores > 0).
    Saída: volume em metros cúbicos (m³), como float.

    Exemplos esperados:
        volume_paralelepipedo(8.0, 5.0, 3.0) -> 120.0
        volume_paralelepipedo(1.0, 1.0, 1.0) -> 1.0
    """
    # TODO(#4/#5) — Gustavo
    raise NotImplementedError("volume_paralelepipedo: Issue #4")
