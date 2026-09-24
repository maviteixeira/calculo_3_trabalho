# Arquitetura do VoluLab

## Fluxo de toda estrutura

```text
Modelo matemático → Representação 3D → Integral (volume analítico)
                  → Método computacional (Monte Carlo) → Comparação (erro %)
```

## Como os módulos se conectam

```text
                         app.py  (Streamlit — só interface, nenhum cálculo)
                           │
                           │ 1. lê ESTRUTURAS e cria o sólido com os parâmetros
                           ▼
                    volulab/models/          ── contrato Solido (base.py)
                    ComodoRetangular, ...
                     │          │         │
     volume_analitico()   contem() +   malha()
                     │   caixa_delimitadora()
                     ▼          │         │
             volulab/utils/     │         │
             formulas.py        │         │
             (integral → Vref)  ▼         ▼
                   volulab/volumetry/   volulab/visualization/
                   monte_carlo.py       plot3d.py
                   (Vest, erro %)       (figura Plotly)
                           │                  │
                           └────────┬─────────┘
                                    ▼
                    app.py mostra métricas + figura 3D
```

Regras:

- `app.py` **não calcula nada**. Só lê os parâmetros, chama os módulos e mostra os resultados.
- `volumetry/` e `visualization/` **não conhecem estruturas específicas**. Trabalham com qualquer `Solido`.
- Fórmulas analíticas ficam **só** em `utils/formulas.py`. As classes em `models/` chamam essas funções e não copiam as fórmulas.

## O contrato `Solido` (`volulab/models/base.py`)

Toda estrutura herda de `Solido` e implementa:

| Método | Retorna | Quem usa |
|---|---|---|
| `nome` (atributo de classe) | nome de exibição, ex.: `"Cômodo retangular"` | app (menu) |
| `parametros()` | `dict[str, float]` com as dimensões (m) | app, testes |
| `volume_analitico()` | volume exato (m³), via `utils/formulas.py` | app, testes |
| `contem(x, y, z)` | array booleano: True onde o ponto está dentro (vetorizado) | Monte Carlo |
| `caixa_delimitadora()` | `((xmin, xmax), (ymin, ymax), (zmin, zmax))` | Monte Carlo |
| `malha()` | `Malha(x, y, z, i, j, k)`, no formato do `go.Mesh3d` | visualização |
| `volume_caixa()` | *(já implementado)* volume da caixa delimitadora | Monte Carlo |

Convenções:

- **Unidades:** metros (m) e metros cúbicos (m³).
- **Validação:** o construtor levanta `ValueError` para parâmetros inválidos (ex.: dimensão ≤ 0).
- **Fronteira:** `contem()` usa intervalos fechados. Um ponto na superfície conta como dentro.
- **Módulo em construção:** o método levanta `NotImplementedError`, e o app mostra "Módulo em desenvolvimento — Issue #N" em vez de quebrar.

O Monte Carlo usa a fórmula

```text
Vobj ≈ Vcaixa · Ndentro / Ntotal
```

com pontos sorteados uniformemente na caixa delimitadora.

## Pastas, responsáveis e issues

| Pasta / arquivo | Responsável | Issues |
|---|---|---|
| `volulab/utils/` | Gustavo (Matemática) | #4, #5 |
| `volulab/models/` | Rayssa (Modelagem 3D) | #5 (`contem`, com o Gustavo), #6 (`malha`) |
| `volulab/visualization/` | Rayssa (Modelagem 3D) | #6 |
| `volulab/volumetry/` | Marcelly (Volumetria) | #7 |
| `tests/`, `README.md`, `docs/` | Samuel (Testes + Documentação) | #8 |
| `app.py`, `requirements.txt`, integração | Maria Vitória (Interface + Coordenação) | #3, #9 |

## Como adicionar uma nova estrutura

Exemplo: um cilindro (Nível 4).

1. **Matemática:** documente a estrutura em `docs/matematica/` seguindo o modelo (Estrutura → Função → Região → Integral → Volume de referência). Depois crie a fórmula em `volulab/utils/formulas.py`, ex.: `volume_cilindro(raio, altura)`.
2. **Modelo:** crie `volulab/models/cilindro.py` com `class Cilindro(Solido)`:
   - `nome = "Cilindro"`;
   - `__init__` validando os parâmetros (`ValueError` se ≤ 0);
   - os seis métodos do contrato, com `volume_analitico()` chamando a fórmula de `utils`.
3. **Registro:** adicione a classe em `ESTRUTURAS` (`volulab/models/__init__.py`):

   ```python
   ESTRUTURAS = {
       ComodoRetangular.nome: ComodoRetangular,
       Cilindro.nome: Cilindro,
   }
   ```

4. **Testes:** crie `tests/test_cilindro.py` com pelo menos um volume analítico conhecido, parâmetros inválidos, `contem()` (dentro, fora e fronteira) e um Monte Carlo com semente fixa e erro < 2%.
5. **Interface:** se os parâmetros forem diferentes de comprimento/largura/altura, ajuste os campos da barra lateral em `app.py`. O Monte Carlo e a visualização não precisam de mudança.
