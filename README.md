# 📚 Análise de Dados de Biblioteca Universitária (UFRN)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red?style=for-the-badge&logo=streamlit&logoColor=white)
![Status](https://img.shields.io/badge/Status-Concluído-success?style=for-the-badge)

## 📋 Sobre o Projeto

Este projeto consiste em um pipeline de **ETL (Extract, Transform, Load)** e **Análise Exploratória de Dados (EDA)** focado no sistema de empréstimos das bibliotecas da UFRN (Universidade Federal do Rio Grande do Norte).

O projeto evoluiu de uma análise estática em Jupyter Notebook para um **Dashboard Interativo**, permitindo a visualização dinâmica dos dados históricos (2010-2020).

> **Contexto:** Este projeto foi desenvolvido seguindo as diretrizes do desafio **#7DaysOfCode - Pandas**, promovido pela **Alura**.

---

## 📊 Dashboard Interativo

Acesse a aplicação em tempo real para explorar os gráficos e filtros:

> 🔗 **[Clique aqui para acessar o Dashboard Online](https://dashboard-emprestimo.streamlit.app/)**

---

## 🚀 Funcionalidades e Etapas do Pipeline

**1. Coleta e Ingestão de Dados:**
- Importação de múltiplos arquivos CSV (dados de empréstimos divididos por semestres).
- Consolidação de **mais de 2 milhões de registros** em um único dataset.

**2. Limpeza e Pré-processamento:**
- Remoção de duplicatas e tratamento de valores nulos.
- **Engenharia de Atributos (Feature Engineering):** - Implementação da lógica **CDU (Classificação Decimal Universal)** para categorizar livros por tema.
    - Extração temporal (Ano, Mês, Hora) para análise de sazonalidade.

**3. Visualização de Dados:**
- Análise de tendências temporais (Empréstimos por Ano/Mês).
- Estudo de horários de pico e perfil dos usuários.
- Gráficos interativos com **Plotly**.

---

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Manipulação de Dados:** Pandas, NumPy
- **Visualização (Notebook):** Matplotlib, Seaborn
- **Visualização (Dashboard):** Plotly Express, Streamlit
- **Formatos de Arquivo:** CSV, Parquet

---