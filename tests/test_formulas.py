import pytest

from volulab.utils.formulas import volume_paralelepipedo


@pytest.mark.skip(reason="aguardando #4")
def test_volume_paralelepipedo_comodo_padrao():
    assert volume_paralelepipedo(8.0, 5.0, 3.0) == pytest.approx(120.0)


@pytest.mark.skip(reason="aguardando #4")
def test_volume_paralelepipedo_cubo_unitario():
    assert volume_paralelepipedo(1.0, 1.0, 1.0) == pytest.approx(1.0)
