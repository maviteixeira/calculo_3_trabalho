# Fundamentação matemática

Cada estrutura do VoluLab ganha um arquivo nesta pasta (ex.: `comodo_retangular.md`), escrito com o modelo abaixo. O volume de referência obtido aqui é o que vai para `volulab/utils/formulas.py` e para os testes.

---

## Modelo

### 1. Estrutura

O que é, em termos arquitetônicos, e quais são os parâmetros, com unidades.

> Ex.: cômodo retangular com comprimento `a`, largura `b` e altura `h`, todos em metros e maiores que zero.

### 2. Função

A função integrada: `1` na integral tripla (volume) ou a altura `f(x, y)` na integral dupla.

> Ex.: f(x, y) = h (teto plano).

### 3. Região

A região de integração, com os limites de cada variável e o sistema de coordenadas usado. Se houver mudança de variáveis, indicar a transformação e o Jacobiano.

> Ex.: E = {(x, y, z) : 0 ≤ x ≤ a, 0 ≤ y ≤ b, 0 ≤ z ≤ h}, em coordenadas cartesianas.

### 4. Integral

A integral montada e a resolução passo a passo.

> Ex.: V = ∭_E 1 dV = ∫₀^a ∫₀^b ∫₀^h 1 dz dy dx = ∫₀^a ∫₀^b h dy dx = ∫₀^a b·h dx = a·b·h

### 5. Volume de referência

A fórmula final e pelo menos dois casos numéricos. Esses casos viram testes.

> Ex.: V = a·b·h → (8, 5, 3) ↦ 120 m³; (1, 1, 1) ↦ 1 m³.
