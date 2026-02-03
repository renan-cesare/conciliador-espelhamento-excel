# Conciliador de Espelhamento de Acessos (Excel)

Ferramenta em Python para **conciliar espelhamentos de acesso entre duas bases Excel**, identificando **o que está faltando replicar** após reorganizações de times, mudanças de hierarquia ou ajustes em matrizes de permissão.

> **English (short):** Python tool to reconcile access mirroring between two Excel bases and detect missing replications after org/team changes.

---

## Principais recursos

* Leitura de **duas bases Excel** (origem vs. destino)
* Normalização de colunas e chaves (ex.: usuário, grupo, perfil, centro de custo etc.)
* Identificação de:

  * acessos presentes na origem e **ausentes no destino**
  * divergências por usuário/grupo (quando aplicável)
* Geração de **relatório consolidado** para ação (recriar/replicar acessos)
* Execução simples via `main.py`

---

## Contexto

Em ambientes corporativos, é comum existirem planilhas que representam:

* **acessos atuais**
* **espelhamentos desejados** (modelo de referência)
* alterações de estrutura (time/gestão/áreas)

Após mudanças organizacionais, surgem inconsistências:

* usuários que deveriam ter acesso e não têm
* espelhamentos incompletos
* diferenças entre bases “fonte” e “alvo”

Este projeto automatiza a conciliação e entrega um output claro para correção.

---

## Aviso importante (uso autorizado)

Este repositório é apresentado como **exemplo técnico/portfólio**.

* Utilize apenas **bases e ambientes autorizados**
* Não publique dados reais (nomes, e-mails, IDs internos, permissões sensíveis)
* Respeite LGPD e políticas internas

---

## Estrutura do projeto

```text
.
├─ main.py
├─ requirements.txt
├─ LICENSE
└─ README.md
```

---

## Requisitos

* Python 3.10+
* Leitura de Excel (via `pandas` + engine do Excel conforme seu ambiente)

---

## Instalação

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

---

## Uso

1. Coloque as planilhas de entrada (origem e destino) em um local seguro (fora do Git).

2. Execute:

```bash
python main.py
```

> Se seu script receber caminhos por parâmetro ou exigir ajustes, mantenha isso documentado no topo do `main.py`
> (por exemplo: `SOURCE_PATH`, `TARGET_PATH` e `OUTPUT_PATH`).

---

## Saídas geradas

* Relatório com itens **faltantes no destino** (base para replicação/recriação)
* (Opcional) abas auxiliares para auditoria (dependendo do script)

---

## Sanitização de dados

Este repositório **não contém dados reais**.

Recomendação:

* mantenha arquivos `.xlsx` fora do repositório
* suba apenas `example.xlsx` (fake) se quiser demonstrar formato futuramente

---

## Licença

MIT
