import plotly.express as px
import pandas as pd
import numpy as np
import streamlit as st

car_data = pd.read_csv(r'..\vehicles.csv')  # lendo os dados
fig = px.histogram(car_data, x="odometer")  # criar um histograma

st.header("Histograma de Odometro dos Veículos")  # título da aplicação

# criando abas
aba1, aba2 = st.tabs(['Botão', 'Checkbox'])

with aba1:  # criando uma aba
  hist_button = st.button('Criar histograma') # criar um botão
          
  if hist_button: # se o botão for clicado
    # escrever uma mensagem
      st.write('Criando o histograma')
              
              # criar um histograma
      fig = px.histogram(car_data, x="odometer")      
          
              # exibir um gráfico Plotly interativo
      st.plotly_chart(fig, width='content')

with aba2:  # criando outra aba
  build_histogram = st.checkbox('Criar um histograma')

  if build_histogram: # se a caixa de seleção for selecionada
    st.write('Criando o histograma')
    fig = px.histogram(car_data, x="odometer")      
    st.plotly_chart(fig, width='content')    
    