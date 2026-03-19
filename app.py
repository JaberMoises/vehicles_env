import streamlit as st  # Importación de streamlit como st
import pandas as pd  # Importación de pandas como pd
import plotly.graph_objects as go  # Importación de plotly.graph_objects como go


# Leer los datos del archivo CSV
car_data = pd.read_csv('car_data.csv')

st.title('Dashboard Interactivo de Vehículos')


st.header('Exploración de distribución y relaciones')
st.write('Utiliza los botones para visualizar la distribución del odómetro y la relación entre precio y kilometraje.')

col1, col2 = st.columns([1, 2])

with col1:
    # Crear un botón en la aplicación para generación de histograma
    hist_button = st.button('Histograma')

with col2:
    # Crear un botón en la aplicación para generación de grafica de disperción
    scatter_button = st.button('Gráfica de dispersión')


# Lógica a ejecutar cuando se hace clic en el botón de histograma
if hist_button:
    # Escribir un mensaje en la aplicación
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma utilizando plotly.graph_objects
    # Se crea una figura vacía y luego se añade un rastro de histograma
    fig = go.Figure(data=[go.Histogram(x=car_data['odometer'])])

    # se añade un título al gráfico
    fig.update_layout(title_text='Distribución del Odómetro')

    # Mostrar el gráfico Plotly interactivo en la aplicación Streamlit
    # 'use_container_width=True' ajusta el ancho del gráfico al contenedor
    st.plotly_chart(fig, use_container_width=True)


# Lógica a ejecutar cuando se hace clic en el botón de gráfica dispersión
if scatter_button:
    st.write('Relación entre precio y odómetro')

    fig = go.Figure(
        data=[
            go.Scatter(
                x=car_data['odometer'],
                y=car_data['price'],
                mode='markers'
            )
        ]
    )

    fig.update_layout(
        title='Precio vs Odómetro',
        xaxis_title='Odómetro',
        yaxis_title='Precio'
    )

    st.plotly_chart(fig, use_container_width=True)


st.header('Análisis de vehículos por categoría')
st.write('Selecciona una categoría para analizar la distribución de vehículos por fabricante.')

# Creación de selector para las categorias de la grafica
option = st.selectbox(
    'Selecciona una categoría:',
    [
        'Cilindros',
        'Condición',
        'Combustible',
        'Transmisión',
        'Carrocería',
        'Color',
        '4WD'
    ]
)

# Diccionario con referencia cruzada selector - dataset
mapping = {
    'Cilindros': 'cylinders',
    'Condición': 'condition',
    'Combustible': 'fuel',
    'Transmisión': 'transmission',
    'Carrocería': 'type',
    'Color': 'paint_color',
    '4WD': 'is_4wd'
}

selected_column = mapping[option]

# Agrupación de dataset por brand + selección
grouped = car_data.groupby(['brand', selected_column]
                           ).size().reset_index(name='count')

fig = go.Figure()

# Obtener categorías únicas
categories = sorted(grouped[selected_column].dropna().unique())

for category in categories:
    df_cat = grouped[grouped[selected_column] == category]

    fig.add_trace(go.Bar(
        x=df_cat['brand'],
        y=df_cat['count'],
        name=str(category),
        text=df_cat['count'],
        textposition='inside'
    ))

order = car_data['brand'].value_counts().index
fig.update_layout(
    barmode='stack',  # barras apiladas
    title=f"{option} por fabricante",
    xaxis_title="Fabricante",
    yaxis_title="Cantidad",
    xaxis_tickangle=45,
    xaxis={'categoryorder': 'array', 'categoryarray': order}
)

st.plotly_chart(fig, use_container_width=True)
