# Análise de Dados de Biblioteca Universitária 📚

> 🚧 Projeto em desenvolvimento 🚧

## 📋 Sobre o Projeto

Este projeto consiste em um pipeline de ETL (Extract, Transform, Load) e Análise Exploratória de Dados (EDA) focado no sistema de empréstimos das bibliotecas da UFRN (Universidade Federal do Rio Grande do Norte). 

O objetivo é processar um grande volume de dados históricos (abrangendo o período de 2010 a 2020, com **mais de 2 milhões de registros**), limpar inconsistências e extrair insights sobre o comportamento dos usuários e a utilização do acervo, preparando a base para tomadas de decisão.

> **Nota:** Este projeto foi desenvolvido seguindo as diretrizes e propostas do desafio **#7DaysOfCode - Pandas**, promovido pela **Alura**.

## 🛠 Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Manipulação de Dados:** Pandas, NumPy
- **Visualização de Dados:** Matplotlib, Seaborn
- **Formatos de Arquivo:** CSV, Parquet
- **Ambiente de Desenvolvimento:** Google Colab / Jupyter Notebook

## 🚀 Funcionalidades e Etapas do Pipeline

**1. Coleta e Ingestão de Dados:**
- Importação de múltiplos arquivos CSV (dados de empréstimos divididos por semestres).
- Leitura de arquivos Parquet (dados cadastrais dos exemplares).
- Concatenação de DataFrames para consolidar o histórico completo.

**2. Limpeza e Pré-processamento:**
- Remoção de duplicatas para garantir a integridade das análises.
- Tratamento de valores nulos e inconsistentes.
- Conversão de tipos de dados (ex: formatação de strings para objetos `datetime`).

**3. Feature Engineering (Engenharia de Atributos):**
- Implementação da lógica **CDU (Classificação Decimal Universal)**: Criação de um algoritmo que categoriza os livros com base no código de localização (ex: códigos entre 600-699 são classificados como "Ciências Aplicadas").
- Criação de colunas derivadas para facilitar a análise temporal (ano, mês, etc.).

**4. Análise Exploratória (Em andamento):**
- Contagem e volume de empréstimos por ano.
- Identificação dos gêneros e temas literários mais populares (via classificação CDU).
- Análise de comportamento e tendências de renovações de exemplares.

## 📂 Estrutura do Notebook

O projeto está estruturado em um Jupyter Notebook (.ipynb) que documenta passo a passo o raciocínio analítico, desde a importação bruta até as visualizações finais.
##
Este projeto faz parte do meu portfólio de Ciência de Dados e demonstra habilidades em manipulação de grandes volumes de dados.