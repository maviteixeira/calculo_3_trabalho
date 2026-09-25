# Roadmap do VoluLab

> **Diretriz:** o Nível 1 tem prioridade absoluta. Ele precisa estar completo, funcional e validado (testes passando, app rodando) antes de qualquer trabalho dos níveis seguintes. Cada nível novo reaproveita o contrato `Solido`, sem reescrever o que já funciona.

## Marcos

| Data | Marco |
|---|---|
| 23/10/2026 | Apresentação parcial: pitch + protótipo funcional (Nível 1) |
| 11/12/2026 | Mostra "Matemática em Código" |

## Nível 1 — MVP (em andamento)

Cômodo retangular (comprimento, largura, altura):

- [ ] Volume analítico pela integral tripla (#4)
- [ ] Região e função de pertencimento `contem()` (#5)
- [ ] Representação 3D com Plotly (#6)
- [ ] Monte Carlo (lógica pronta, falta revisão e validação) (#7)
- [ ] Erro percentual entre analítico e Monte Carlo
- [ ] Testes de referência sem `skip` (#8)
- [ ] Interface integrada, pronta para o protótipo (#9)

## Nível 2 — Cômodo realista

- Espessura das paredes
- Portas e janelas (volumes subtraídos)
- Volume bruto × volume útil

## Nível 3 — Análise

- Derivadas parciais do volume em relação aos parâmetros (∂V/∂comprimento, ...)
- Análise de sensibilidade: qual dimensão mais influencia o volume
- Convergência do Monte Carlo conforme o número de amostras (gráfico erro × N)

## Nível 4 — Outras formas

- Sólidos: cilindro, cone, esfera, elipsoide, paraboloide e formas compostas
  (mudança de variáveis e Jacobiano: coordenadas cilíndricas e esféricas)
- Etapas arquitetônicas previstas: teto inclinado, domo, estrutura curva e combinação de sólidos
