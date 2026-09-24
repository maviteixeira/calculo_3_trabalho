# Status do projeto — VoluLab

> Atualizado em **24/09/2026**. Atualize este arquivo a cada reunião de sexta.

## 🎯 Objetivo

Representar uma estrutura arquitetônica em 3D, permitir alterar suas medidas e calcular o volume de duas formas:

1. **Matemática:** integral (volume exato);
2. **Computacional:** Monte Carlo (volume aproximado);

e comparar as duas pelo **erro percentual**.

**Meta imediata (Nível 1):** cômodo retangular funcionando por completo no app.

| Data | Marco |
|---|---|
| **23/10/2026** | Apresentação parcial: pitch + protótipo funcional |
| **11/12/2026** | Mostra "Matemática em Código" |

---

## ✅ O que já foi feito

| Data | Quem | O quê |
|---|---|---|
| 21/08 | Maria Vitória | Criou o repositório e o README inicial |
| 16/09 | Marcelly | Atualizou o README e adicionou o link do relatório (`docs/relatorio_link`) |
| 17/09 | Marcelly | Primeira versão do **Monte Carlo** e do cálculo de erro percentual |
| 23/09 | Gustavo | Propôs uma reorganização de pastas e o volume do cômodo via integral simbólica (SymPy), na branch `chore/reestrutura-conforme-pdf` |
| 24/09 | Maria Vitória | **Arquitetura do projeto (Issue #3)**, na branch `chore/estrutura-inicial` — detalhes abaixo |

### Issue #3 — Arquitetura (o que ela entregou)

- **Organização do código:** tudo dentro da pasta `volulab/`, com uma subpasta por frente (`models`, `utils`, `volumetry`, `visualization`).
- **Contrato `Solido`:** a "regra" que toda estrutura segue (ter volume, dizer se um ponto está dentro, ter caixa delimitadora e malha 3D). Assim, estruturas novas funcionam com o resto do sistema sem mudanças.
- **Cômodo retangular:** criado, com validação das medidas (não aceita valor ≤ 0).
- **Monte Carlo da Marcelly:** adaptado para a nova organização e já funcionando.
- **App Streamlit:** já abre e roda. As partes que faltam mostram o aviso "Módulo em desenvolvimento — Issue #N".
- **Testes:** 25 testes escritos. 16 já passam; 9 esperam as próximas Issues.
- **Documentação:** arquitetura, roadmap, guia de contribuição (`CONTRIBUTING.md`), modelos de ata, de decisão e de Issue/PR, README atualizado.
- **Pasta `src/` antiga:** removida (o código útil foi aproveitado).

### Decisões tomadas (a confirmar no PR)

Registradas em [docs/decisoes/](decisoes/README.md):

1. Código organizado no pacote `volulab/`; a proposta de pastas da branch do Gustavo fica substituída.
2. SymPy fica fora do MVP: a integral é resolvida à mão e documentada.
3. O resultado do Monte Carlo guarda os pontos sorteados, para o gráfico 3D.
4. Pontos na parede contam como "dentro"; entradas inválidas geram erro; o sorteio usa semente (resultado reprodutível).

---

## 🔜 O que falta

### Para fechar a Issue #3

- [ ] Enviar as branches `develop` e `chore/estrutura-inicial` para o GitHub
- [ ] Abrir o PR para a `develop` e conseguir a revisão de outra pessoa
- [ ] Criar as Issues #4 a #9 no GitHub
- [ ] Avisar o Gustavo sobre a substituição da branch dele

### Nível 1 — até 23/10

| Issue | Quem | O que falta | Destrava no app |
|---|---|---|---|
| #4 | Gustavo | Fórmula do volume (integral) + documentação da integral | "Volume matemático" |
| #5 | Gustavo (apoio: Rayssa) | Função que diz se um ponto está dentro do cômodo | "Volume aproximado" e "Erro (%)" |
| #6 | Rayssa | Desenho 3D do cômodo e dos pontos do Monte Carlo | Figura 3D |
| #7 | Marcelly | Revisar a adaptação do Monte Carlo e documentar o método | — (já funciona) |
| #8 | Samuel | Tirar os `skip` dos testes e montar a tabela de resultados | — |
| #9 | Maria Vitória | Integrar tudo, preparar a demonstração e levar para a `main` | Protótipo completo |

**Ordem sugerida:** #4 e #5 primeiro (destravam os números), #6 em paralelo, depois #7 → #8 → #9.

### Depois do Nível 1

Níveis 2 a 4 (paredes, portas e janelas; análise de sensibilidade; cilindro, domo etc.). Ver [roadmap.md](roadmap.md). **Só começam quando o Nível 1 estiver completo e testado.**

---

## 📌 Como estamos trabalhando

- Ninguém mexe direto na `main` nem na `develop`: cada um trabalha na sua branch e abre Pull Request.
- Todo PR é revisado por outra pessoa e só entra com os testes passando.
- Reunião toda sexta, com ata em `docs/reunioes/`.
- Detalhes em [CONTRIBUTING.md](../CONTRIBUTING.md).
