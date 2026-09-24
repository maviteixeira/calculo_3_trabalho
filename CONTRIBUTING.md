# Como contribuir com o VoluLab

## Ciclo de trabalho

```text
Issue → Branch → Código → Commit → Pull Request → Revisão → Merge → Teste
```

1. **Issue:** todo trabalho começa em uma Issue, com responsável e critério de pronto.
2. **Branch:** crie a branch a partir da `develop` atualizada:
   ```bash
   git switch develop
   git pull
   git switch -c feature/calculos
   ```
3. **Código:** mexa só nos arquivos da sua Issue. Se precisar mudar um contrato (`Solido`, `ResultadoMonteCarlo`...), avise a equipe antes.
4. **Commit:** commits pequenos, um por alteração (ver prefixos abaixo).
5. **Pull Request:** abra o PR **para a `develop`**, preencha o modelo e cite a Issue (`Closes #N`).
6. **Revisão:** outra pessoa da equipe revisa e aprova. Ninguém aprova o próprio PR.
7. **Merge:** só depois da aprovação e com os testes passando.
8. **Teste:** depois do merge, rode a `develop` (testes + app) para confirmar que nada quebrou.

> **Ninguém trabalha direto na `main` nem na `develop`.**
> **Nada de merge sem testar:** `pytest` passando e `streamlit run app.py` abrindo sem erro.

## Branches

| Branch | Uso |
|---|---|
| `main` | versão estável (apresentações e entregas) |
| `develop` | integração: recebe os PRs das frentes |
| `feature/modelagem` | modelos 3D e `contem()` (`volulab/models/`) |
| `feature/calculos` | fórmulas e Monte Carlo (`volulab/utils/`, `volulab/volumetry/`) |
| `feature/visualizacao` | figuras Plotly (`volulab/visualization/`) |
| `feature/testes` | testes (`tests/`) |
| `docs/documentacao` | documentação (`docs/`, `README.md`) |

Para tarefas pontuais, use o mesmo padrão com um nome curto: `fix/erro-percentual`, `chore/estrutura-inicial`.

## Prefixos de commit

| Prefixo | Quando usar | Exemplo |
|---|---|---|
| `feat:` | funcionalidade nova | `feat: volume analítico do cômodo retangular` |
| `fix:` | correção de erro | `fix: contem() aceita pontos na fronteira` |
| `docs:` | documentação | `docs: integral do cômodo em docs/matematica` |
| `test:` | testes | `test: remove skip dos testes de volume` |
| `chore:` | configuração, dependências, estrutura | `chore: atualiza versão do plotly` |

## Preparar o ambiente

Requer Python 3.11 ou superior.

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux/macOS
source .venv/bin/activate

pip install -r requirements-dev.txt
```

## Rodar os testes

```bash
pytest
```

Testes marcados com `skip` ("aguardando #N") dependem de uma Issue ainda aberta. Quem fecha a Issue **remove o `skip`** no mesmo PR e confirma que o teste passa.

## Rodar o app

```bash
streamlit run app.py
```

Partes ainda não implementadas aparecem como "Módulo em desenvolvimento — Issue #N". Isso é esperado.

## Padrão de código

- Código, comentários e docstrings em português. Nomes de variáveis e funções em português, sem acento, em `snake_case`.
- Cada função com docstring: entradas, saídas, unidades (m, m³) e um exemplo.
- Nenhum cálculo dentro de `app.py`.
- Fórmulas analíticas só em `volulab/utils/formulas.py`.
- Nova estrutura? Siga o passo a passo em [docs/arquitetura.md](docs/arquitetura.md#como-adicionar-uma-nova-estrutura).
