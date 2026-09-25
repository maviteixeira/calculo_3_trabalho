# Reuniões

Reunião semanal toda **sexta-feira**. Cada reunião gera uma ata nesta pasta: `AAAA-MM-DD.md` (ex.: `2026-09-25.md`).

---

## Modelo de ata

```markdown
# Ata — DD/MM/AAAA

- **Presentes:**
- **Ausentes:**
- **Quem registrou:**

## 1. Abertura (5 min)
- Pendências da ata anterior: feitas / não feitas.
- Próximo marco e quanto falta (23/10 protótipo · 11/12 Mostra).

## 2. Rodada das frentes (3 min por pessoa)
| Frente | Pessoa | Fiz | Vou fazer | Bloqueios |
|---|---|---|---|---|
| Matemática (utils) | Gustavo | | | |
| Modelagem 3D (models, visualization) | Rayssa | | | |
| Volumetria (volumetry) | Marcelly | | | |
| Testes + Documentação | Samuel | | | |
| Interface + Coordenação | Maria Vitória | | | |

## 3. Integração
- PRs abertos e quem revisa cada um.
- O app roda na `develop`? `pytest` passa?
- Conflitos entre frentes (contratos, nomes, formatos).

## 4. Decisões
- Decisão → registrar em `docs/decisoes/` (quem registra).

## 5. Fechamento
| Tarefa | Responsável | Issue | Prazo |
|---|---|---|---|
| | | | |
```

---

## Modelo de status semanal

Cada pessoa envia no grupo até **quinta-feira à noite**, antes da reunião:

```markdown
**Status — [Nome] — semana de DD/MM**
- Issue(s): #N
- ✅ Feito:
- 🔄 Em andamento:
- ⛔ Bloqueios / preciso de ajuda com:
- 🔗 PR / branch:
```
