# 📐 Modelagem e Volumetria Computacional

## 🏫 Informações Institucionais

* **Instituição:** Fundação Universidade Federal de Rondônia (UNIR)
* **Curso:** Bacharelado em Ciência da Computação
* **Disciplina:** Cálculo III (DIN00018)
* **Professor:** Prof. Esp. Rodrigo Duarte de Oliveira Tolêdo
* **Período:** 2026.2

### 👥 Integrantes do Grupo

* **Ana Julia Santiago** — GitHub: [@anajsv](https://github.com/anajsv)
* **Cauã Henrique Feitosa de Souza** — GitHub: [@cahenq](https://github.com/cahenq)
* **Gustavo Amaral Dias** — GitHub: [@pacmanmg](https://github.com/pacmanmg)
* **Marcelly Yasmim Portela Trindade** — GitHub: [@EllyMarc](https://github.com/EllyMarc)
* **Samuel Gomes Cunha** — GitHub: [@Samuel-Amadio](https://github.com/Samuel-Amadio)
* **Maria Vitória Teixeira e Silva** — GitHub: [@maviteixeira](https://github.com/maviteixeira)
* **Rayssa Rabelo Feitosa** — GitHub: [@rayrabelo007](https://github.com/rayrabelo007)

---

## 🔍 Visão Geral do Projeto

Este projeto acadêmico, desenvolvido no âmbito da disciplina de **Cálculo III**, tem como tema **Modelagem e Volumetria Computacional**.

A proposta consiste em aplicar conceitos de Cálculo Multivariável para desenvolver uma solução computacional capaz de representar, analisar e/ou calcular propriedades geométricas de objetos e regiões no espaço tridimensional.

O projeto busca estabelecer uma relação entre os conceitos matemáticos estudados em Cálculo III e sua aplicação prática na Ciência da Computação, utilizando recursos computacionais para auxiliar na visualização e resolução de problemas relacionados à volumetria.

> **Observação:** O problema específico, o modelo matemático e o escopo final da aplicação serão definidos durante a etapa de modelagem do projeto.

---

## 🎯 Objetivo

Desenvolver uma aplicação computacional baseada em conceitos de **Cálculo III**, com foco em **modelagem e volumetria**, possibilitando a aplicação prática de integrais múltiplas e outros conceitos relacionados ao estudo de regiões e objetos tridimensionais.

### Objetivos Específicos

* Aplicar conceitos de Cálculo III na modelagem de problemas tridimensionais;
* Utilizar integrais duplas e/ou triplas na determinação de volumes;
* Explorar mudanças de variáveis e o conceito de Jacobiano, quando aplicável;
* Desenvolver uma representação computacional dos modelos estudados;
* Permitir a visualização dos resultados obtidos;
* Relacionar a fundamentação matemática com uma aplicação prática em Ciência da Computação;
* Documentar o desenvolvimento matemático e computacional do projeto.

---

## 📐 Conceitos de Cálculo Aplicados

### 1. Modelagem Matemática

Nesta etapa será definida a região, superfície ou objeto tridimensional que será utilizado como problema de estudo.

Serão apresentadas as funções, limites de integração e demais elementos matemáticos necessários para representar o problema.

> **A definir durante a etapa de modelagem.**

### 2. Integrais Duplas

Serão utilizadas integrais duplas para representar e calcular propriedades de regiões bidimensionais e/ou superfícies, conforme o problema escolhido.

[
\iint_D f(x,y),dA
]

A aplicação específica da integral será definida de acordo com o modelo desenvolvido pelo grupo.

### 3. Integrais Triplas

Quando aplicável ao problema escolhido, serão utilizadas integrais triplas para determinar o volume ou outras propriedades de uma região tridimensional:

[
\iiint_E f(x,y,z),dV
]

Para o cálculo de volume, poderá ser utilizada a forma:

[
V = \iiint_E 1,dV
]

### 4. Mudança de Variáveis e Jacobiano

Caso seja necessária uma mudança de sistema de coordenadas, será utilizado o conceito de **Jacobiano** para realizar a transformação da integral.

[
dV = |J|,du,dv,dw
]

A escolha do sistema de coordenadas e da transformação utilizada será definida durante o desenvolvimento do modelo.

### 5. Modelagem Computacional

Os modelos matemáticos serão traduzidos para uma solução computacional, permitindo a realização dos cálculos e, quando aplicável, a visualização gráfica das regiões e objetos analisados.

---

## 🛠️ Tecnologias e Dependências

> **As tecnologias definitivas serão definidas durante a etapa de desenvolvimento.**

Possível stack inicial:

* **Linguagem:** Python
* **Cálculo Numérico:** NumPy
* **Visualização:** Matplotlib
* **Visualização 3D:** Matplotlib 3D e/ou biblioteca a ser definida
* **Controle de versão:** Git e GitHub

---

## 📂 Estrutura do Repositório

A estrutura inicial do projeto será organizada da seguinte forma:

```text
├── src/
│   ├── main.py
│   ├── calculus.py
│   ├── model.py
│   └── visualization.py
│
├── docs/
│   └──
│
├── tests/
│   └──
│
├── README.md
├── requirements.txt
└── .gitignore
```

### Descrição inicial

* `src/` — Código-fonte da aplicação;
* `main.py` — Ponto de entrada do programa;
* `calculus.py` — Implementação dos cálculos matemáticos;
* `model.py` — Definição do modelo matemático e/ou geométrico;
* `visualization.py` — Recursos de visualização gráfica e tridimensional;
* `docs/` — Documentação e materiais complementares;
* `tests/` — Testes da aplicação;
* `requirements.txt` — Dependências do projeto;
* `README.md` — Documentação principal do projeto.

> A estrutura poderá ser modificada conforme o escopo da aplicação for definido.

---

## 🚀 Como Executar o Projeto

> **Esta seção será atualizada após a implementação do protótipo.**

### 1. Clonar o Repositório

```bash
git clone https://github.com/[organização-ou-usuario]/[nome-do-repositorio].git
cd [nome-do-repositorio]
```

### 2. Criar o Ambiente Virtual

```bash
python -m venv venv
```

No Windows:

```bash
venv\Scripts\activate
```

No Linux/macOS:

```bash
source venv/bin/activate
```

### 3. Instalar as Dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a Aplicação

```bash
python src/main.py
```

---

## 📊 Funcionamento da Aplicação

> **Seção a ser desenvolvida após a definição do problema e implementação do protótipo.**

A aplicação deverá receber os parâmetros necessários para representar o modelo matemático definido pelo grupo e realizar os cálculos relacionados à volumetria.

Dependendo do escopo final, o sistema poderá apresentar:

* representação da região ou objeto tridimensional;
* limites de integração;
* cálculo do volume;
* representação gráfica;
* comparação entre resultado analítico e computacional;
* resultados numéricos;
* outros parâmetros definidos durante o desenvolvimento.

---

## 📈 Resultados

> **Seção reservada para os resultados obtidos durante a implementação.**

Nesta seção serão apresentados os resultados dos cálculos realizados pela aplicação, acompanhados de gráficos, representações tridimensionais, tabelas e/ou comparações que sejam relevantes para a análise do modelo.

### Exemplo de resultado

> Esta seção será preenchida após a definição do modelo matemático e execução dos primeiros testes.

---

## 🧪 Testes e Validação

A aplicação será submetida a testes para verificar a consistência dos resultados computacionais em relação aos resultados matemáticos esperados.

Serão considerados, conforme aplicável:

* testes com diferentes parâmetros;
* validação dos limites de integração;
* comparação com resultados analíticos;
* verificação dos cálculos numéricos;
* análise de possíveis erros e limitações;
* testes de representação gráfica.

---

## 💡 Conclusão e Aprendizados

> **Seção a ser concluída ao final do projeto.**

O desenvolvimento do projeto deverá permitir relacionar os conceitos de **Cálculo III** com aplicações computacionais, demonstrando como ferramentas matemáticas podem ser utilizadas na modelagem e resolução de problemas tridimensionais.

Serão discutidos os resultados obtidos, as dificuldades encontradas durante o desenvolvimento, as limitações da solução e os principais conhecimentos adquiridos pelo grupo.

---

## 📚 Referências

As referências utilizadas durante o desenvolvimento serão adicionadas nesta seção.

Entre as referências previstas no projeto de extensão estão:

* GUIDORIZZI, H. L. *Um Curso de Cálculo*. Vol. 2 e 3. 5. ed. Rio de Janeiro: LTC, 2002.
* THOMAS, G. B. *Cálculo*. Vol. 2. 10. ed. São Paulo: Addison-Wesley, 2002.
* STEWART, J. *Cálculo*. Vol. 2. 8. ed. São Paulo: Cengage Learning, 2016.

---

## 📌 Status do Projeto

**Em desenvolvimento — Fase 1: Concepção e Modelagem Matemática.**

### Próximas etapas

* [ ] Definir o problema específico de volumetria;
* [ ] Definir o modelo matemático;
* [ ] Definir as funções e limites de integração;
* [ ] Definir as tecnologias;
* [ ] Estruturar o repositório;
* [ ] Dividir as tarefas entre os integrantes;
* [ ] Desenvolver o protótipo inicial;
* [ ] Realizar testes e validação;
* [ ] Elaborar a documentação técnica;
* [ ] Preparar a apresentação do projeto.

---

## 📅 Cronograma

O desenvolvimento seguirá o cronograma geral estabelecido para o projeto de extensão de Cálculo III.

A primeira etapa envolve a definição temática, modelagem matemática e estruturação inicial do repositório GitHub. Posteriormente ocorrerão as etapas de desenvolvimento do produto, documentação, testes e apresentação pública.
