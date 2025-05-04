import pandas as pd
import streamlit as st
import plotly.express as px

car_data = pd.read_csv(r'C:\Users\HP\OneDrive\Desktop\Sprint7\vehicles_us.csv')

# Crear un encabezado.
st.header('Visualización de Vehiculos.')

# Crear un subtítulo para car_data.
st.subheader('Muestra de los primeros 20 Datos de Vehículos.')

# Creamos una sección para ver el df 'car_data'
st.dataframe(car_data.head(20))

# Crear un botón para construir el histograma
hist_button = st.button('Construir histograma')

if hist_button:  # Al hacer clic en el botón
    st.write('Este histograma muestra la cantidad de vehículos en venta agrupados por rangos de kilometraje. Permite identificar cuántos autos se encuentran en cada nivel de uso.')

    # Crear un histograma con Plotly
    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribución de Vehículos por Kilometraje",
        labels={"odometer": "Kilometraje (km/millas)", "count": "Cantidad de Vehículos"}
        )
        
    # Mostrar el gráfico interactivo
    st.plotly_chart(fig, use_container_width=True)


# Crear boton para construir grafico de dispersion.
disp_button = st.button('Construir gráfico de dispersión') # crear un botón
        
if disp_button: # al hacer clic en el botón

    # escribir un mensaje
    st.write('Este gráfico de dispersión muestra la relación entre el kilometraje de los vehículos y su precio de venta.')

    # crear un grafico de dispersion
    fig = px.scatter(
        car_data,
        x="odometer",
        y = "price",
        title="Relación entre Kilometraje y Precio de Venta",
        labels={"odometer": "Kilometraje (km/millas)", "price": "Precio de Venta (USD)"}
    )
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
