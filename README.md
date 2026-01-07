# Análise de Dados de Biblioteca Universitária 📚

> 🚧 Projeto em desenvolvimento 🚧

## 📋 Sobre o Projeto

Este projeto consiste em um pipeline de ETL (Extract, Transform, Load) e Análise Exploratória de Dados (EDA) focado no sistema de empréstimos de uma biblioteca universitária.

O objetivo é processar um grande volume de dados históricos (2010 a 2020), limpar inconsistências e extrair insights sobre o comportamento dos usuários e o acervo, preparando a base para tomadas de decisão.

## 🛠 Tecnologias Utilizadas

- Linguagem: Python 3

- Manipulação de Dados: Pandas, NumPy

- Visualização: Matplotlib, Seaborn

- Formatos de Arquivo: CSV, Parquet

- Ambiente: Google Colab / Jupyter Notebook

## 🚀 Funcionalidades e Etapas

**Coleta e Ingestão de Dados:**

- Importação de múltiplos arquivos CSV (dados de empréstimos divididos por semestres).

- Leitura de arquivos Parquet (dados dos exemplares).

- Concatenação de DataFrames para consolidar o histórico completo.

**Limpeza e Pré-processamento:**

- Remoção de duplicatas para garantir a integridade dos dados.

- Tratamento de dados nulos.

- Conversão de tipos de dados (ex: strings para datetime).

**Feature Engineering (Engenharia de Atributos):**

- Implementação da lógica CDU (Classificação Decimal Universal): Algoritmo que categoriza os livros baseada no código de localização (ex: código entre 600-699 -> "Ciências Aplicadas").

- Criação de colunas derivadas para facilitar a análise temporal.

**Análise Exploratória (Em andamento):**

- Contagem e volume de empréstimos por ano.

- Identificação dos gêneros literários mais populares via CDU.

- Análise de comportamento de renovações.

## 📂 Estrutura do Notebook

O projeto está estruturado em um Jupyter Notebook (.ipynb) que documenta passo a passo o raciocínio analítico, desde a importação bruta até as visualizações finais.
##
Este projeto faz parte do meu portfólio de Ciência de Dados e demonstra habilidades em manipulação de grandes volumes de dados.