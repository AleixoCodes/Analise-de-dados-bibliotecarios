import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Configuração inicial da página
st.set_page_config(page_title="Dashboard Bibliotecas UFRN", page_icon="📚", layout="wide")

st.title("📚 Dashboard de Empréstimos - Bibliotecas UFRN")
st.markdown("""
Este dashboard interativo foi desenvolvido para analisar os dados de empréstimos do acervo 
do sistema de bibliotecas da UFRN. Você pode interagir com os gráficos passando o mouse e usando os filtros laterais.
""")

# 2. Função para carregar os dados (o @st.cache_data ajuda o dashboard a não carregar o CSV toda hora)
@st.cache_data
def load_data():
    # Lê o dataset gerado no final do seu Jupyter Notebook
    df = pd.read_csv("DadosCompletos.csv", sep=";")
    
    # Converte a coluna de data para o formato datetime correto do pandas
    df['data_emprestimo'] = pd.to_datetime(df['data_emprestimo'], errors='coerce')
    
    # Extrai Ano, Mês e Hora para facilitar na criação dos gráficos
    df['Ano'] = df['data_emprestimo'].dt.year
    df['Mes'] = df['data_emprestimo'].dt.month
    df['Hora'] = df['data_emprestimo'].dt.hour
    
    return df

with st.spinner("Carregando base de dados..."):
    df = load_data()

# 3. Criando uma Barra Lateral (Sidebar) com Filtros
st.sidebar.image("https://dhg1h5j42swfq.cloudfront.net/2021/04/15210438/ufrn.png", width=150)
st.sidebar.header("Filtros Interativos")

anos_disponiveis = df['Ano'].dropna().astype(int).unique()
anos_disponiveis.sort()
ano_selecionado = st.sidebar.multiselect("Filtre por Ano(s):", anos_disponiveis, default=anos_disponiveis)

# Aplicando o filtro no DataFrame
if ano_selecionado:
    df_filtrado = df[df['Ano'].isin(ano_selecionado)]
else:
    df_filtrado = df

# 4. Criando as Estatísticas Gerais (KPIs)
st.markdown("### 📊 Estatísticas Gerais")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total de Empréstimos", f"{len(df_filtrado):,}".replace(",", "."))
col2.metric("Usuários Únicos", f"{df_filtrado['matricula_ou_siape'].nunique():,}".replace(",", "."))
col3.metric("Exemplares Únicos", f"{df_filtrado['id_exemplar'].nunique():,}".replace(",", "."))
col4.metric("Bibliotecas na Rede", f"{df_filtrado['biblioteca'].nunique()}")

st.divider()

# 5. GRÁFICOS INTERATIVOS COM PLOTLY

st.markdown("### 📈 Tendências de Empréstimos ao Longo do Tempo")
col_ano, col_mes = st.columns(2)

with col_ano:
    emprestimos_por_ano = df_filtrado.groupby('Ano').size().reset_index(name='Quantidade')
    fig_ano = px.line(emprestimos_por_ano, x='Ano', y='Quantidade', markers=True,
                      title="Quantidade de empréstimos por Ano",
                      color_discrete_sequence=['#1f77b4'])
    fig_ano.update_xaxes(type='category') # Evita que o gráfico mostre números como "2012.5"
    st.plotly_chart(fig_ano, use_container_width=True)

with col_mes:
    emprestimos_por_mes = df_filtrado.groupby('Mes').size().reset_index(name='Quantidade')
    # Trocando números pelos nomes dos meses
    meses_map = {1:'Jan', 2:'Fev', 3:'Mar', 4:'Abr', 5:'Mai', 6:'Jun', 
                 7:'Jul', 8:'Ago', 9:'Set', 10:'Out', 11:'Nov', 12:'Dez'}
    emprestimos_por_mes['Mês'] = emprestimos_por_mes['Mes'].map(meses_map)
    fig_mes = px.line(emprestimos_por_mes, x='Mês', y='Quantidade', markers=True,
                      title="Quantidade de empréstimos por Mês",
                      color_discrete_sequence=['#ff7f0e'])
    st.plotly_chart(fig_mes, use_container_width=True)

st.divider()

st.markdown("### ⏰ Análise de Horários e Público")

col_hora, col_vinculo = st.columns(2)

with col_hora:
    emprestimos_por_hora = df_filtrado.groupby('Hora').size().reset_index(name='Quantidade')
    fig_hora = px.bar(emprestimos_por_hora, x='Hora', y='Quantidade', 
                      title="Quantidade de empréstimos por Faixa Horária",
                      color='Quantidade', color_continuous_scale='Blues')
    st.plotly_chart(fig_hora, use_container_width=True)

with col_vinculo:
    freq_vinculo = df_filtrado['tipo_vinculo_usuario'].value_counts(normalize=True).reset_index()
    freq_vinculo.columns = ['Tipo de Vínculo', 'Porcentagem']
    freq_vinculo['Porcentagem'] = round(freq_vinculo['Porcentagem'] * 100, 2)
    
    fig_vinculo = px.bar(freq_vinculo, x='Tipo de Vínculo', y='Porcentagem', 
                         title="Frequência por Tipo de Vínculo de Usuário (%)",
                         color='Porcentagem', color_continuous_scale='Teal',
                         text='Porcentagem')
    fig_vinculo.update_traces(textposition='outside')
    st.plotly_chart(fig_vinculo, use_container_width=True)

# Gráfico de CDU na largura inteira (pois os nomes das classificações são grandes)
st.divider()
st.markdown("### 📚 Assuntos Mais Procurados")

if 'CDU' in df_filtrado.columns:
    freq_cdu = df_filtrado['CDU'].value_counts(normalize=True).reset_index()
    freq_cdu.columns = ['Classificação Decimal Universal', 'Porcentagem']
    freq_cdu['Porcentagem'] = round(freq_cdu['Porcentagem'] * 100, 2)
    
    fig_cdu = px.bar(freq_cdu, x='Classificação Decimal Universal', y='Porcentagem', 
                     title="Frequência de Empréstimos por Classificação Decimal Universal (CDU) (%)",
                     color='Porcentagem', color_continuous_scale='Purp',
                     text='Porcentagem')
    fig_cdu.update_traces(textposition='outside')
    st.plotly_chart(fig_cdu, use_container_width=True)
else:
    st.warning("A coluna 'CDU' não foi encontrada no dataset.")


# Gráficos de distribuição de empréstimos mensais por tipos de alunos

st.markdown("### 🎓 Empréstimos Mensais por Tipo de Aluno")

if 'tipo_vinculo_usuario' in df_filtrado.columns:
    emprestimos_mes_vinculo = df_filtrado.groupby(['Mes', 'tipo_vinculo_usuario']).size().reset_index(name='Quantidade')
    emprestimos_mes_vinculo['Mês'] = emprestimos_mes_vinculo['Mes'].map(meses_map)
    
    fig_mes_vinculo = px.bar(emprestimos_mes_vinculo, x='Mês', y='Quantidade', color='tipo_vinculo_usuario',
                             title="Empréstimos Mensais por Tipo de Aluno",
                             color_discrete_sequence=px.colors.qualitative.Set2)
    st.plotly_chart(fig_mes_vinculo, use_container_width=True)
st.markdown("---")
st.markdown("Desenvolvido para análise de dados.")