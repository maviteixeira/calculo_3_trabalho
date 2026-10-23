import plotly.graph_objects as go
import numpy as np

def criar_figura_comodo_3d(largura: float, comprimento: float, altura: float, volume_ref: float):
    """
    Cria a figura base do Plotly 3D para o cômodo retangular (paralelepípedo)
    com base na modelagem geométrica.
    """
    x = [0, largura, largura, 0, 0, largura, largura, 0]
    y = [0, 0, comprimento, comprimento, 0, 0, comprimento, comprimento]
    z = [0, 0, 0, 0, altura, altura, altura, altura]

    # Vértices das faces do paralelepípedo
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
        title=f"Visualização 3D - Cômodo (Volume Ref: {volume_ref:.2f} m³)",
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

    return fig

def adicionar_pontos_monte_carlo(fig, px, py, pz, dentro, max_pontos=2000):
    """
    Adiciona os pontos estocásticos do método de Monte Carlo na figura 3D existente,
    diferenciando os pontos de dentro (laranja) e de fora (cinza/azul).
    """
    n_total = len(px)
    max_plot = min(max_pontos, n_total)
    
    # Amostragem para otimizar a performance gráfica no navegador
    idx_plot = np.random.choice(n_total, max_plot, replace=False)

    fig.add_trace(go.Scatter3d(
        x=px[idx_plot], 
        y=py[idx_plot], 
        z=pz[idx_plot],
        mode='markers',
        marker=dict(
            size=2,
            color=np.where(dentro[idx_plot], 'orange', 'lightgray'),
            opacity=0.6
        ),
        name='Amostras Monte Carlo'
    ))
    
    return fig