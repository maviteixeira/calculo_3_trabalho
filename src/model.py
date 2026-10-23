import numpy as np
import plotly.graph_objects as go

def gerar_modelo_comodo(largura: float, comprimento: float, altura: float):
    """
    Gera a representação tridimensional de um cômodo retangular (paralelepípedo)
    utilizando Plotly, com base nos parâmetros fornecidos.
    
    Parâmetros:
    - largura (float): Dimensão no eixo X (ex: de 0 a largura).
    - comprimento (float): Dimensão no eixo Y (ex: de 0 a comprimento).
    - altura (float): Dimensão no eixo Z (ex: de 0 a altura).
    
    Retorna:
    - fig: Objeto de figura do Plotly contendo a malha 3D do cômodo.
    - volume_ref: Volume analítico de referência (Largura * Comprimento * Altura).
    """
    
    # Volume analítico exato (para validação e comparação com o Monte Carlo)
    volume_ref = largura * comprimento * altura

    # Coordenadas dos vértices da caixa (cômodo retangular)
    # Definindo os limites X, Y, Z
    x = [0, largura, largura, 0, 0, largura, largura, 0]
    y = [0, 0, comprimento, comprimento, 0, 0, comprimento, comprimento]
    z = [0, 0, 0, 0, altura, altura, altura, altura]

    # Definição das faces do paralelepípedo para o Plotly Mesh3d
    # Cada face é triangulada para formar a malha 3D sólida/transparente
    i = [7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2]
    j = [3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 7, 6]
    k = [0, 7, 5, 6, 6, 2, 1, 5, 7, 3, 4, 5]

    fig = go.Figure(data=[
        go.Mesh3d(
            x=x,
            y=y,
            z=z,
            i=i,
            j=j,
            k=k,
            color='rgba(100, 150, 250, 0.5)',  # Cor translúcida para visualização interna
            opacity=0.6,
            flatshading=True,
            name='Cômodo 3D'
        )
    ])

    # Configuração do layout do gráfico 3D
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

# Função de pertinência para o método de Monte Carlo (frente do Gustavo/Marcelly)
def criar_regra_comodo(largura: float, comprimento: float, altura: float):
    """
    Retorna uma função lambda que valida se um ponto (x, y, z) 
    pertasta ao interior do cômodo retangular parametrizado.
    """
    return lambda x, y, z: (x >= 0) & (x <= largura) & (y >= 0) & (y <= comprimento) & (z >= 0) & (z <= altura)


# Bloco de teste local da modelagem 3D
if __name__ == "__main__":
    print("Testando a modelagem 3D da Rayssa...")
    figura, vol = gerar_modelo_comodo(largura=5.0, comprimento=8.0, altura=3.0)
    print(f"Volume de referência calculado: {vol} m³")
    # figura.show() # Descomentar caso queira testar a abertura da janela do gráfico localmente