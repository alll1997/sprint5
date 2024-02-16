import pandas as pd
import plotly_express as px
import streamlit as st

data = pd.read_csv("vehicles_us.csv")
data['manufacture'] = data['model'].str.split().str[0]

# Visualización del dataframe
st.title(':black[Anuncios de venta de vehículos]')
data_checkbox= st.checkbox('Visualizador de datos')

if data_checkbox:
    st.write(data.head(10))

# Modulo de histograma
st.header('Condición del vehículo VS Año del modelo')
st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    
# crear un histograma
fig_hist = px.histogram(data, x="model_year", color="condition")
fig_hist.update_traces(opacity=0.75)

# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig_hist, use_container_width=True)


# Modulo de diagrama de barras
st.header('Tipos modelos de cada marca')
st.write('Creación de un diagrama de barras de los tipos de vehículo que fabrica cada marca')

# crear un digrama de barras
fig_bar = px.bar(data, x="manufacture", color="type")
    
# mostrar un gráfico Plotly interactivo
st.plotly_chart(fig_bar, use_container_width=True)


# Modulo de diagrama de dispersión
st.header('Impacto del odometro VS Valor del vehículo')
# Obtener las opciones únicas de una columna
unique_manufacture = data['manufacture'].unique()  
# Crear desplegables
opcion_seleccionada_1 = st.selectbox('Selecciona la manufactura 1', unique_manufacture, key=1)
opcion_seleccionada_2 = st.selectbox('Selecciona la manufactura 2', unique_manufacture, key=2)
# Filtrar el DataFrame basado en las opciones seleccionadas
df_filtrado = data[(data['manufacture'] == opcion_seleccionada_1) | (data['manufacture'] == opcion_seleccionada_2)]

build_scatter = st.checkbox('Construir un scatter')

# crear un histograma
if build_scatter:
    fig_scatter = px.scatter(df_filtrado, x="odometer", y="price", color='manufacture')
    fig_scatter.update_traces(opacity=0.75)
        
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig_scatter, use_container_width=True) 