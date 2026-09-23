import sympy as sp


def modelo_matematico_retangular():
    """
    Monta simbolicamente o modelo matemático do cômodo retangular:
    função de altura, região de integração e a integral dupla.

    Retorna um dicionário com cada peça do caminho
    Estrutura -> Funcao -> Regiao -> Integral
    """
    x, y = sp.symbols("x y", real=True, nonnegative=True)
    a, b, h = sp.symbols("a b h", positive=True)

    f = h

    limites_x = (x, 0, a)
    limites_y = (y, 0, b)

    # Integral dupla
    integral = sp.Integral(f, limites_y, limites_x)
    volume_expr = integral.doit()

    return {
        "variaveis": {"x": x, "y": y, "a": a, "b": b, "h": h},
        "funcao_altura": f,
        "regiao": {"x": limites_x, "y": limites_y},
        "integral_simbolica": integral,
        "volume_formula": sp.simplify(volume_expr),
    }


def volume_referencia(a: float, b: float, h: float) -> float:
    """
    Calcula o volume de referência (matemático) do cômodo retangular
    a partir da fórmula obtida por integração simbólica.
    Retorna:
    float : volume de referência (V_ref), usado para
    calcular o erro percentual do método de Monte Carlo:
        Erro (%) = |V_est - V_ref| / V_ref * 100
    """
    modelo = modelo_matematico_retangular()
    a_s, b_s, h_s = (modelo["variaveis"][k] for k in ("a", "b", "h"))
    volume = modelo["volume_formula"].subs({a_s: a, b_s: b, h_s: h})
    return float(volume)


def dentro_do_solido(ponto, a: float, b: float, h: float) -> bool:
    """
    Função de pertencimento (versão escalar): diz se um único ponto
    (x, y, z) está dentro do cômodo retangular. 

    Parâmetros:
    ponto : tupla (x, y, z)
    a, b, h : dimensões do cômodo (largura, comprimento, altura)
    """
    x, y, z = ponto
    return (0 <= x <= a) and (0 <= y <= b) and (0 <= z <= h)


def funcao_pertence_retangular(a: float, b: float, h: float):
    """
    Fábrica de função de pertencimento VETORIZADA, no formato que o
    monte_Carlo(funcao_pertence, ...):

        funcao_pertence(x, y, z) -> vetor booleano (numpy)

    onde x, y, z são arrays do numpy (um valor por amostra sorteada).

    """
    def regra(x, y, z):
        return (
            (x >= 0) & (x <= a)
            & (y >= 0) & (y <= b)
            & (z >= 0) & (z <= h)
        )
    return regra


if __name__ == "__main__":
    #conferência rápida do modelo
    modelo = modelo_matematico_retangular()

    print("Função de altura f(x, y):", modelo["funcao_altura"])
    print("Integral simbólica:", modelo["integral_simbolica"])
    print("Fórmula do volume:", modelo["volume_formula"])

    # caso de teste com os valores do mockup da interface:
    # largura = 5.0, comprimento = 8.0, altura = 3.0 -> volume esperado = 120
    a_teste, b_teste, h_teste = 5.0, 8.0, 3.0
    v_ref = volume_referencia(a_teste, b_teste, h_teste)
    print(f"\nTeste: a={a_teste}, b={b_teste}, h={h_teste}")
    print("Volume de referência calculado:", v_ref)
    assert v_ref == a_teste * b_teste * h_teste, "Volume não bate com o esperado!"
    print("OK: volume bate com a*b*h.")

    # Teste da função de pertencimento
    ponto_dentro = (2.0, 3.0, 1.0)
    ponto_fora = (6.0, 3.0, 1.0)
    print(f"\nPonto {ponto_dentro} está dentro?", dentro_do_solido(ponto_dentro, a_teste, b_teste, h_teste))
    print(f"Ponto {ponto_fora} está dentro?", dentro_do_solido(ponto_fora, a_teste, b_teste, h_teste))
