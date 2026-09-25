"""Contrato comum a todas as estruturas do VoluLab.

Toda estrutura (cômodo, cilindro, domo...) herda de `Solido` e implementa os
mesmos métodos. Assim o app, o Monte Carlo e a visualização funcionam com
qualquer estrutura sem precisar saber qual ela é.

Unidades: comprimentos em metros (m), volumes em metros cúbicos (m³).
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np

Intervalo = tuple[float, float]
Caixa = tuple[Intervalo, Intervalo, Intervalo]


@dataclass
class Malha:
    """Malha triangular no formato de `plotly.graph_objects.Mesh3d`.

    - `x`, `y`, `z`: coordenadas dos vértices (um valor por vértice).
    - `i`, `j`, `k`: índices dos vértices de cada triângulo (um valor por
      triângulo). O triângulo n liga os vértices i[n], j[n] e k[n].

    Uso: `go.Mesh3d(x=m.x, y=m.y, z=m.z, i=m.i, j=m.j, k=m.k)`.
    """

    x: np.ndarray
    y: np.ndarray
    z: np.ndarray
    i: np.ndarray
    j: np.ndarray
    k: np.ndarray


class Solido(ABC):
    """Estrutura arquitetônica tridimensional com volume calculável."""

    #: Nome de exibição da estrutura (ex.: "Cômodo retangular").
    nome: str = ""

    @abstractmethod
    def parametros(self) -> dict[str, float]:
        """Retorna os parâmetros da estrutura, ex.: {"comprimento": 8.0, ...} (m)."""

    @abstractmethod
    def volume_analitico(self) -> float:
        """Volume exato (m³), obtido pela integral. Deve usar `volulab.utils`."""

    @abstractmethod
    def contem(self, x: np.ndarray, y: np.ndarray, z: np.ndarray) -> np.ndarray:
        """Função de pertencimento vetorizada.

        Recebe três arrays de mesmo formato (coordenadas em m) e devolve um
        array booleano do mesmo formato: True onde o ponto (x, y, z) está
        dentro do sólido.
        """

    @abstractmethod
    def caixa_delimitadora(self) -> Caixa:
        """Menor caixa alinhada aos eixos que contém o sólido.

        Formato: ((xmin, xmax), (ymin, ymax), (zmin, zmax)), em metros.
        É a região onde o Monte Carlo sorteia os pontos.
        """

    @abstractmethod
    def malha(self) -> Malha:
        """Malha triangular da superfície do sólido, para desenhar em 3D."""

    def volume_caixa(self) -> float:
        """Volume (m³) da caixa delimitadora: (xmax−xmin)·(ymax−ymin)·(zmax−zmin)."""
        (xmin, xmax), (ymin, ymax), (zmin, zmax) = self.caixa_delimitadora()
        return (xmax - xmin) * (ymax - ymin) * (zmax - zmin)

    def __repr__(self) -> str:
        args = ", ".join(f"{k}={v}" for k, v in self.parametros().items())
        return f"{type(self).__name__}({args})"
