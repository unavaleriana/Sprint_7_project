import streamlit as st
import pandas
import plotly_express

# Crear encabezado
st.header('Construir Gráficas')

# Leer datos de un archivo CSV
cars_data = pandas.read_csv("vehicles_us.csv")

# Histograma
hist_button = st.button('Construir histograma') # crear un botón

if hist_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
    # crear un histograma
    fig = plotly_express.histogram(cars_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersion
disp_button = st.button('Construir gráfico de dispersion') # crear un botón
     
if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
         
    # crear un gráfico de dispersión 
    fig = plotly_express.scatter(cars_data, x="odometer", y="price")
    
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
