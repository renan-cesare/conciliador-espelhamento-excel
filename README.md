# Conciliador de Espelhamento (Excel)

Ferramenta simples em Python para **conciliar espelhamentos de acesso** (“quem visualiza quem”) entre duas bases no Excel.

Este projeto nasceu de um cenário comum em operações: após mudanças de times/hierarquia, é necessário **reconstruir e validar** uma base de espelhamentos. O script compara uma base “antiga” com uma base “recriada” e gera exatamente o que ainda falta revisar.

> Projeto profissional sanitizado: sem dados reais, nomes ou informações internas.

---

## O que ele faz

Lê um arquivo Excel com duas bases (por padrão na mesma aba):

- **Base A (antiga)**: colunas **A:B**
- **Base B (recriada)**: colunas **D:E**

E gera um Excel de saída com duas abas:

- **faltando_recriar** → itens que estavam na Base A e não estão na Base B (A − B)
- **novos_na_base_b** → itens que estão na Base B e não existiam na Base A (B − A)

---

## Formato esperado

Cada base deve conter dois campos:

- **Visualiza** (quem tem acesso / quem visualiza)
- **Visualizado** (quem é visualizado)

O script normaliza os dados (string + trim) e remove linhas vazias/duplicadas.

---

## Como usar

### 1) Instalar dependências
```bash
pip install -r requirements.txt
