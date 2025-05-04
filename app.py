import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Sprint7\vehicles_us.csv')

# Crear un botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma con Plotly
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)


# Crear boton para construir grafico de dispersion.
disp_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if disp_button: # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un gráfico de dispersión para el conjunto de datos del odómetro y la venta de coches')
            
    # crear un grafico de dispersion
    fig = px.scatter(car_data, x="odometer", y = "price")
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
