# 0002 — SymPy fora da stack do MVP

- **Data:** 24/09/2026
- **Status:** proposta (a confirmar com Gustavo na Issue #4)
- **Quem decidiu:** Maria Vitória (coordenação)

## Contexto
A branch `chore/reestrutura-conforme-pdf` calculava o volume do cômodo integrando simbolicamente com SymPy (`utils/volume.py`). A stack definida para o projeto é Python, NumPy, Plotly, Streamlit e pytest.

## Decisão
No Nível 1, a integral é resolvida à mão, documentada em `docs/matematica/`, e o resultado vira uma fórmula fechada em `volulab/utils/formulas.py` (ex.: `comprimento * largura * altura`). SymPy não entra no `requirements.txt` por enquanto.

## Por quê
- A resolução da integral é o conteúdo da disciplina e deve aparecer na documentação, não ficar escondida em uma chamada de biblioteca.
- A fórmula fechada é mais rápida, mais simples de testar e não acrescenta dependência.
- O trabalho simbólico do Gustavo continua útil: pode ser reaproveitado para **mostrar** a integral no app (ex.: LaTeX) ou nos Níveis 3–4 (derivadas parciais, Jacobiano). Se for adotado, registrar em uma nova decisão.
