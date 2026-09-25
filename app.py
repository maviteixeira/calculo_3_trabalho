"""VoluLab 3D — interface Streamlit.

Execução: streamlit run app.py

Este arquivo só monta a tela e chama os módulos de `volulab/`. Nenhum cálculo
é feito aqui. Módulos ainda não implementados levantam NotImplementedError,
e a tela mostra um aviso no lugar do resultado.
"""

import streamlit as st

from volulab.models import ESTRUTURAS
from volulab.visualization.plot3d import figura_monte_carlo, figura_solido
from volulab.volumetry.monte_carlo import erro_percentual, estimar_volume


def chamar(funcao, issue: str, *args, **kwargs):
    """Chama `funcao`; se o módulo ainda for esqueleto, avisa e devolve None."""
    try:
        return funcao(*args, **kwargs)
    except NotImplementedError:
        st.info(f"Módulo em desenvolvimento — Issue {issue}")
        return None


def formatar(valor, sufixo: str) -> str:
    return "—" if valor is None else f"{valor:,.3f} {sufixo}"


st.set_page_config(page_title="VoluLab 3D", layout="wide")
st.title("VoluLab 3D")
st.caption("Laboratório computacional para análise volumétrica de estruturas arquitetônicas")

with st.sidebar:
    st.header("Parâmetros")
    nome_estrutura = st.selectbox("Estrutura", list(ESTRUTURAS))
    comprimento = st.number_input("Comprimento (m)", min_value=0.1, value=8.0, step=0.5)
    largura = st.number_input("Largura (m)", min_value=0.1, value=5.0, step=0.5)
    altura = st.number_input("Altura (m)", min_value=0.1, value=3.0, step=0.5)

    st.header("Monte Carlo")
    n_amostras = st.slider(
        "Nº de amostras", min_value=1_000, max_value=200_000, value=50_000, step=1_000
    )
    usar_semente = st.checkbox("Semente fixa (resultado reprodutível)", value=True)
    semente = st.number_input("Semente", min_value=0, value=42, step=1, disabled=not usar_semente)

    calcular = st.button("Calcular volume", type="primary", use_container_width=True)

if not calcular:
    st.write("Ajuste os parâmetros na barra lateral e clique em **Calcular volume**.")
    st.stop()

try:
    solido = ESTRUTURAS[nome_estrutura](comprimento, largura, altura)
except ValueError as erro:
    st.error(str(erro))
    st.stop()

v_analitico = chamar(solido.volume_analitico, "#4")
resultado = chamar(
    estimar_volume, "#5", solido, n_amostras, int(semente) if usar_semente else None
)
v_estimado = resultado.volume_estimado if resultado else None
erro = (
    erro_percentual(v_estimado, v_analitico)
    if v_analitico is not None and v_estimado is not None
    else None
)

col1, col2, col3 = st.columns(3)
col1.metric("Volume matemático", formatar(v_analitico, "m³"))
col2.metric("Volume aproximado", formatar(v_estimado, "m³"))
col3.metric("Erro (%)", formatar(erro, "%"))

if resultado:
    st.caption(
        f"{resultado.n_dentro:,} de {resultado.n_amostras:,} pontos dentro · "
        f"caixa = {resultado.volume_caixa:,.3f} m³ · "
        f"erro padrão = ±{resultado.erro_padrao:,.3f} m³"
    )

st.subheader("Representação 3D")
if resultado:
    figura = chamar(figura_monte_carlo, "#6", solido, resultado.pontos, resultado.dentro)
else:
    figura = chamar(figura_solido, "#6", solido)
if figura is not None:
    st.plotly_chart(figura, use_container_width=True)
