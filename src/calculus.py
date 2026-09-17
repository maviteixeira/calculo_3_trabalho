# Frente do Gustavo e Marcelly (Cálculos de Volume + Monte Carlo)
import numpy as np

# Função monte carlo recebe como parâmetro:
# outra função (funcao_pertence), os limites e num padrão de amostras
def monte_Carlo (funcao_pertence, x_lim, y_lim, z_lim, n_amostras=10000):

    # Dimensões da Bounding Box (caixa delimitadora)
    dx = x_lim[1] - x_lim[0]
    dy = y_lim[1] - y_lim[0]
    dz = z_lim[1] - z_lim[0]

    # Calculo de volume total da caixa
    v_caixa = dx*dy*dz

    #Sorteio de pontos aleatórios
    x = np.random.uniform(x_lim[0], x_lim[1], n_amostras)
    y = np.random.uniform(y_lim[0], y_lim[1], n_amostras)
    z = np.random.uniform(z_lim[0], z_lim[1], n_amostras)

    # Validação de pontos x, y, z para função de regra que retorna um vetor booleano
    pontos_dentro = funcao_pertence(x, y, z)
    # soma esse vetor e diz quantos pontos caíram dentro da caixa
    n_dentro = np.sum(pontos_dentro)

    #Calcula o volume estimado 
    v_estimado = v_caixa * (n_dentro / n_amostras)

    # Retorna os valores
    return v_estimado, x, y, z, pontos_dentro

# função que calcula o erro percentual
def calcular_erro_percentual(v_estimado, v_referencia):
    if v_referencia == 0:
        return 0.0
    return (abs(v_estimado - v_referencia) / v_referencia) * 100.0

            
# bloco de teste local (Esse bloco de teste só vai funcionar nesse arquivo aqui)
if __name__ == "__main__":
    print("Testezinho")

    regra_comodo_simples = lambda x, y, z : (z <= 3.0)
    v_real = 60.0
    v_est, px, py, pz, dentro = monte_Carlo(funcao_pertence=regra_comodo_simples,
    x_lim=(0,4),
    y_lim=(0,5), 
    z_lim=(0,3),
    n_amostras=50000
    )

    erro = calcular_erro_percentual(v_est, v_real)

    print(f"Volume referencia (Analítico): {v_real: .2f} m³")
    print(f"Volume estimado (Monte Carlo): {v_est: .2f} m³")
    print(f"Erro percentual obtido: {erro: .3f}%\n")
