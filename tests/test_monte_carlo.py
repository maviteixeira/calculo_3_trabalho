import numpy as np
import pytest

from volulab.models import ComodoRetangular
from volulab.models.base import Solido
from volulab.volumetry.monte_carlo import erro_percentual, estimar_volume


class MeiaCaixa(Solido):
    """Sólido de apoio só para testes: metade inferior (z ≤ 0,5) de um cubo 1 × 1 × 1.

    Volume exato 0,5 m³ numa caixa de 1 m³. Permite testar o Monte Carlo
    sem depender dos stubs de ComodoRetangular.
    """

    nome = "Meia caixa (teste)"

    def parametros(self):
        return {}

    def volume_analitico(self):
        return 0.5

    def contem(self, x, y, z):
        return z <= 0.5

    def caixa_delimitadora(self):
        return ((0.0, 1.0), (0.0, 1.0), (0.0, 1.0))

    def malha(self):
        raise NotImplementedError


def test_erro_percentual():
    assert erro_percentual(110, 100) == 10.0


def test_erro_percentual_estimativa_abaixo():
    assert erro_percentual(90, 100) == pytest.approx(10.0)


def test_erro_percentual_referencia_invalida():
    with pytest.raises(ValueError):
        erro_percentual(1.0, 0.0)


def test_monte_carlo_meia_caixa():
    r = estimar_volume(MeiaCaixa(), 100_000, semente=1)
    assert r.volume_caixa == pytest.approx(1.0)
    assert r.n_amostras == 100_000
    assert r.volume_estimado == pytest.approx(r.volume_caixa * r.n_dentro / r.n_amostras)
    assert erro_percentual(r.volume_estimado, 0.5) < 2.0
    assert r.erro_padrao > 0
    assert r.pontos.shape == (100_000, 3)
    assert r.dentro.shape == (100_000,)


def test_monte_carlo_meia_caixa_reprodutivel():
    a = estimar_volume(MeiaCaixa(), 10_000, semente=7)
    b = estimar_volume(MeiaCaixa(), 10_000, semente=7)
    assert a.volume_estimado == b.volume_estimado
    np.testing.assert_array_equal(a.pontos, b.pontos)


def test_monte_carlo_n_amostras_invalido():
    with pytest.raises(ValueError):
        estimar_volume(MeiaCaixa(), 0)


@pytest.mark.skip(reason="aguardando #5")
def test_monte_carlo_comodo_padrao_erro_menor_que_2_por_cento():
    r = estimar_volume(ComodoRetangular(8, 5, 3), 100_000, semente=42)
    assert erro_percentual(r.volume_estimado, 120.0) < 2.0


@pytest.mark.skip(reason="aguardando #5")
def test_monte_carlo_comodo_reprodutivel_com_mesma_semente():
    comodo = ComodoRetangular(8, 5, 3)
    a = estimar_volume(comodo, 10_000, semente=42)
    b = estimar_volume(comodo, 10_000, semente=42)
    assert a.volume_estimado == b.volume_estimado
    assert a.n_dentro == b.n_dentro
