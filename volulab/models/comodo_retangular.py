"""Cômodo retangular — estrutura do Nível 1 (MVP).

Convenção: origem no canto do cômodo, eixos alinhados às paredes.
    x ∈ [0, comprimento], y ∈ [0, largura], z ∈ [0, altura]   (metros)
"""

import numpy as np

from volulab.models.base import Caixa, Malha, Solido
from volulab.utils.formulas import volume_paralelepipedo


class ComodoRetangular(Solido):
    """Cômodo em forma de paralelepípedo reto."""

    nome = "Cômodo retangular"

    def __init__(self, comprimento: float, largura: float, altura: float):
        for rotulo, valor in (
            ("comprimento", comprimento),
            ("largura", largura),
            ("altura", altura),
        ):
            if valor <= 0:
                raise ValueError(f"{rotulo} deve ser maior que zero (recebido: {valor})")
        self.comprimento = float(comprimento)
        self.largura = float(largura)
        self.altura = float(altura)

    def parametros(self) -> dict[str, float]:
        return {
            "comprimento": self.comprimento,
            "largura": self.largura,
            "altura": self.altura,
        }

    def volume_analitico(self) -> float:
        """Volume exato (m³). A fórmula mora em `utils/formulas.py` (não duplicar aqui)."""
        return volume_paralelepipedo(self.comprimento, self.largura, self.altura)

    def contem(self, x: np.ndarray, y: np.ndarray, z: np.ndarray) -> np.ndarray:
        """Diz, ponto a ponto, se (x, y, z) está dentro do cômodo.

        Entradas: arrays NumPy de mesmo formato, em metros.
        Saída: array booleano do mesmo formato.

        Região: 0 ≤ x ≤ comprimento, 0 ≤ y ≤ largura, 0 ≤ z ≤ altura.
        Fronteira: intervalos FECHADOS — pontos exatamente nas paredes, no
        piso ou no teto contam como dentro (True). Isso não altera o volume
        (a fronteira tem volume zero), só evita ambiguidade nos testes.

        Exemplo (cômodo 8 × 5 × 3):
            contem([4.0, 9.0, 8.0], [2.5, 1.0, 5.0], [1.5, 1.0, 3.0])
            -> array([ True, False,  True])
        """
        # TODO(#5) — Gustavo
        raise NotImplementedError("contem() do cômodo retangular: Issue #5")

    def caixa_delimitadora(self) -> Caixa:
        # O cômodo é a própria caixa.
        return ((0.0, self.comprimento), (0.0, self.largura), (0.0, self.altura))

    def malha(self) -> Malha:
        """Malha triangular do paralelepípedo, no formato de `Mesh3d`.

        Saída esperada: 8 vértices (os cantos do cômodo) e 12 triângulos
        (2 por face × 6 faces). Coordenadas em metros, seguindo a
        convenção x ∈ [0, comprimento], y ∈ [0, largura], z ∈ [0, altura].

        Exemplo (cômodo 1 × 1 × 1): len(m.x) == 8 e len(m.i) == 12.
        """
        # TODO(#6) — Rayssa
        raise NotImplementedError("malha() do cômodo retangular: Issue #6")
