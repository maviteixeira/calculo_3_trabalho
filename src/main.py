import streamlit as st
import numpy as np
import plotly.graph_objects as go

# --- Função Monte Carlo (Gustavo & Marcelly) ---
def monte_Carlo(funcao_pertence, x_lim, y_lim, z_lim, n_amostras=10000):
    dx = x_lim[1] - x_lim[0]
    dy = y_lim[1] - y_lim[0]
    dz = z_lim[1] - z_lim[0]

    v_caixa = dx * dy * dz

    x = np.random.uniform(x_lim[0], x_lim[1], n_amostras)
    y = np.random.uniform(y_lim[0], y_lim[1], n_amostras)
    z = np.random.uniform(z_lim[0], z_lim[1], n_amostras)

    pontos_dentro = funcao_pertence(x, y, z)
    n_dentro = np.sum(pontos_dentro)

    v_estimado = v_caixa * (n_dentro / n_amostras)
    return v_estimado, x, y, z, pontos_dentro

def calcular_erro_percentual(v_estimado, v_referencia):
    if v_referencia == 0:
        return 0.0
    return (abs(v_estimado - v_referencia) / v_referencia) * 100.0

# --- Frente da Rayssa (Modelagem 3D do Cômodo) ---
def gerar_modelo_comodo(largura, comprimento, altura):
    volume_ref = largura * comprimento * altura

    x = [0, largura, largura, 0, 0, largura, largura, 0]
    y = [0, 0, comprimento, comprimento, 0, 0, comprimento, comprimento]
    z = [0, 0, 0, 0, altura, altura, altura, altura]

    i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2]
    j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 7, 6]
    k = [0, 7, 5, 6, 6, 2, 1, 5, 7, 3, 4, 5]

    fig = go.Figure(data=[
        go.Mesh3d(
            x=x, y=y, z=z,
            i=i, j=j, k=k,
            color='rgba(100, 150, 250, 0.4)',
            opacity=0.5,
            flatshading=True,
            name='Cômodo 3D'
        )
    ])

    fig.update_layout(
        title=f"Modelo 3D: Cômodo Retangular (Volume Ref: {volume_ref:.2f} m³)",
        scene=dict(
            xaxis_title='Largura (X)',
            yaxis_title='Comprimento (Y)',
            zaxis_title='Altura (Z)',
            xaxis=dict(range=[0, max(largura * 1.2, 5)]),
            yaxis=dict(range=[0, max(comprimento * 1.2, 5)]),
            zaxis=dict(range=[0, max(altura * 1.2, 5)]),
        ),
        margin=dict(l=0, r=0, b=0, t=40)
    )

    return fig, volume_ref

# --- Configuração da Interface (Maria Vitória) ---
# Usando ícones nativos do Streamlit (substituindo os emojis)
st.set_page_config(page_title="VoluLab 3D - Cálculo III", page_icon="cube", layout="wide")

st.title("VoluLab 3D: Modelagem e Volumetria Computacional")
st.markdown("Aplicação desenvolvida para a disciplina de **Cálculo III (UNIR)**[cite: 1, 5].")

# Sidebar com parâmetros
st.sidebar.header("Parâmetros do Cômodo")
largura = st.sidebar.slider("Largura (X)", 1.0, 10.0, 5.0, 0.5)
comprimento = st.sidebar.slider("Comprimento (Y)", 1.0, 10.0, 8.0, 0.5)
altura = st.sidebar.slider("Altura (Z)", 1.0, 5.0, 3.0, 0.5)

st.sidebar.header("Parâmetros de Monte Carlo")
n_amostras = st.sidebar.selectbox("Amostras Monte Carlo", [1000, 5000, 10000, 50000], index=2)

# Regra de pertinência baseada nos sliders
regra_comodo = lambda x, y, z: (x >= 0) & (x <= largura) & (y >= 0) & (y <= comprimento) & (z >= 0) & (z <= altura)

# Execução dos modelos e cálculos
figura_3d, v_real = gerar_modelo_comodo(largura, comprimento, altura)
v_est, px, py, pz, dentro = monte_Carlo(
    funcao_pertence=regra_comodo,
    x_lim=(0, largura),
    y_lim=(0, comprimento),
    z_lim=(0, altura),
    n_amostras=n_amostras
)

erro = calcular_erro_percentual(v_est, v_real)

# Exibição de Métricas na Tela
col1, col2, col3 = st.columns(3)
col1.metric("Volume Referência (Analítico)", f"{v_real:.2f} m³")
col2.metric("Volume Estimado (Monte Carlo)", f"{v_est:.2f} m³")
col3.metric("Erro Percentual", f"{erro:.3f}%", delta_color="inverse")

st.markdown("---")

# Adicionando os pontos de Monte Carlo no gráfico 3D
max_plot = min(2000, n_amostras)
idx_plot = np.random.choice(n_amostras, max_plot, replace=False)

figura_3d.add_trace(go.Scatter3d(
    x=px[idx_plot], y=py[idx_plot], z=pz[idx_plot],
    mode='markers',
    marker=dict(
        size=2,
        color=np.where(dentro[idx_plot], 'orange', 'lightgray'),
        opacity=0.6
    ),
    name='Pontos Monte Carlo'
))

st.plotly_chart(figura_3d, use_container_width=True)