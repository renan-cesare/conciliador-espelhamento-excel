# Conciliador de Espelhamento de Acessos (Excel)

Ferramenta em **Python** para **conciliar e validar espelhamentos de acesso** ("quem visualiza quem") entre duas bases no Excel.

Este projeto atende um cenário comum em **operações, risco e compliance**: após mudanças de estrutura, permissões ou equipes, é necessário **reconstruir uma base de espelhamentos** e verificar, de forma objetiva, **o que ainda precisa ser ajustado ou validado**.

> Projeto sanitizado para portfólio: não contém dados reais, nomes internos ou informações sensíveis.

---

## Problema que resolve

Em ambientes operacionais, espelhamentos de acesso costumam ser:

* reconstruídos manualmente
* comparados de forma visual
* suscetíveis a erro humano

Este script elimina esse risco ao **comparar automaticamente** uma base antiga com uma base recriada, entregando **diferenças claras, rastreáveis e auditáveis**.

---

## O que o projeto faz

A partir de um arquivo Excel contendo duas bases:

* **Base A (antiga)**
* **Base B (recriada)**

O script:

* normaliza os dados (remoção de espaços, padronização de strings)
* elimina duplicidades
* compara os pares *Visualiza → Visualizado*
* gera um arquivo Excel final com as diferenças encontradas

### Saída gerada

Um novo arquivo Excel com duas abas:

* **faltando_recriar**
  Registros que existiam na Base A, mas **não aparecem** na Base B (A − B)

* **novos_na_base_b**
  Registros que surgiram na Base B e **não existiam** na Base A (B − A)

---

## Formato esperado do Excel

Cada base deve conter **duas colunas**:

* **Visualiza** → usuário que possui o acesso
* **Visualizado** → usuário que é visualizado

### Layout padrão do arquivo

* **Base A (antiga)**: colunas **A:B**
* **Base B (recriada)**: colunas **D:E**

> O layout pode ser ajustado diretamente no código, caso necessário.

---

## Como rodar o projeto

### 1) Clonar o repositório

```bash
git clone <url-do-repositorio>
cd conciliador-espelhamento-excel
```

### 2) Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

### 3) Instalar dependências

```bash
pip install -r requirements.txt
```

### 4) Executar

```bash
python main.py
```

O script irá:

* ler o arquivo Excel configurado no código
* processar as bases
* gerar o arquivo de saída com as abas de conciliação

---

## Estrutura do projeto

```
conciliador-espelhamento-excel/
├── main.py
├── requirements.txt
├── README.md
├── LICENSE
└── .gitignore
```

---

## Decisões de projeto

* Uso de **Python + pandas** para rapidez e clareza na manipulação de Excel
* Estrutura propositalmente enxuta, focada em uso operacional
* Comparação baseada em pares normalizados para evitar falsos positivos

---

## Limitações conhecidas

* Layout do Excel é fixo por padrão
* Execução via script (sem interface gráfica)
* Sempre gera um novo arquivo de saída

---

## Possíveis melhorias futuras

* [ ] Tornar o layout configurável via parâmetros
* [ ] Adicionar logs estruturados
* [ ] Criar interface simples (CLI ou GUI)
* [ ] Validações adicionais de consistência

---

## Licença

MIT
