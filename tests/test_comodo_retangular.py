import numpy as np
import pytest

from volulab.models import ESTRUTURAS, ComodoRetangular


def test_registrado_em_estruturas():
    assert ESTRUTURAS["Cômodo retangular"] is ComodoRetangular


def test_parametros():
    comodo = ComodoRetangular(8, 5, 3)
    assert comodo.parametros() == {"comprimento": 8.0, "largura": 5.0, "altura": 3.0}


@pytest.mark.parametrize(
    "dimensoes",
    [(0, 5, 3), (8, 0, 3), (8, 5, 0), (-1, 5, 3), (8, -5, 3), (8, 5, -0.1)],
)
def test_dimensoes_invalidas_levantam_value_error(dimensoes):
    with pytest.raises(ValueError):
        ComodoRetangular(*dimensoes)


def test_caixa_delimitadora():
    comodo = ComodoRetangular(8, 5, 3)
    assert comodo.caixa_delimitadora() == ((0.0, 8.0), (0.0, 5.0), (0.0, 3.0))


def test_volume_caixa():
    assert ComodoRetangular(8, 5, 3).volume_caixa() == pytest.approx(120.0)


@pytest.mark.skip(reason="aguardando #4")
def test_volume_analitico_comodo_padrao():
    assert ComodoRetangular(8, 5, 3).volume_analitico() == pytest.approx(120.0)


@pytest.mark.skip(reason="aguardando #4")
def test_volume_analitico_cubo_unitario():
    assert ComodoRetangular(1, 1, 1).volume_analitico() == pytest.approx(1.0)


@pytest.mark.skip(reason="aguardando #5")
def test_contem_ponto_interno_e_externo():
    comodo = ComodoRetangular(8, 5, 3)
    x = np.array([4.0, 9.0, 4.0, 4.0, -0.1])
    y = np.array([2.5, 2.5, 6.0, 2.5, 2.5])
    z = np.array([1.5, 1.5, 1.5, 3.5, 1.5])
    np.testing.assert_array_equal(comodo.contem(x, y, z), [True, False, False, False, False])


@pytest.mark.skip(reason="aguardando #5")
def test_contem_fronteira_conta_como_dentro():
    # Convenção documentada em ComodoRetangular.contem: intervalos fechados.
    comodo = ComodoRetangular(8, 5, 3)
    x = np.array([0.0, 8.0, 8.0])
    y = np.array([0.0, 5.0, 2.5])
    z = np.array([0.0, 3.0, 3.0])
    np.testing.assert_array_equal(comodo.contem(x, y, z), [True, True, True])


@pytest.mark.skip(reason="aguardando #6")
def test_malha_tem_8_vertices_e_12_triangulos():
    m = ComodoRetangular(1, 1, 1).malha()
    assert len(m.x) == len(m.y) == len(m.z) == 8
    assert len(m.i) == len(m.j) == len(m.k) == 12
