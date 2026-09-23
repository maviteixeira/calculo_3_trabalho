from utils.volume import volume_referencia, funcao_pertence_retangular
from volumetry.monte_carlo import monte_Carlo, calcular_erro_percentual


def rodar_teste(a, b, h, n_amostras=50_000):
    v_ref = volume_referencia(a, b, h)
    regra = funcao_pertence_retangular(a, b, h)

    v_est, x, y, z, dentro = monte_Carlo(
        funcao_pertence=regra,
        x_lim=(0, a),
        y_lim=(0, b),
        z_lim=(0, h),
        n_amostras=n_amostras,
    )

    erro = calcular_erro_percentual(v_est, v_ref)

    print(f"Dimensões: a={a}, b={b}, h={h} | amostras={n_amostras}")
    print(f"Volume referência (Gustavo):     {v_ref:.3f} m³")
    print(f"Volume estimado (Marcelly):      {v_est:.3f} m³")
    print(f"Erro percentual:                 {erro:.3f}%\n")

    return v_ref, v_est, erro


if __name__ == "__main__":
    # caso1: mesmo exemplo do mockup da interface 
    rodar_teste(a=5.0, b=8.0, h=3.0)

    # caso2: mesmo exemplo usado no teste local da marcelly
    rodar_teste(a=4.0, b=5.0, h=3.0)

    # verificação: com 50k amostras num cômodo retangular simples,
    # o erro deve ficar bem baixo (poucos %) — se não ficar, é sinal
    # de que a bounding box ou a função de pertencimento estão erradas.
    _, _, erro1 = rodar_teste(a=5.0, b=8.0, h=3.0, n_amostras=200_000)
    assert erro1 < 2.0, "Erro muito alto para um caso trivial — revisar integração."
    print("OK: integração Gustavo + Marcelly validada.")
