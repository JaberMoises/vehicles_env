# vehicles_env
# 🚗📊 Dashboard Interactivo de Vehículos

## 📌 Descripción

Este proyecto consiste en el desarrollo de una aplicación web interactiva para el análisis exploratorio de un dataset de anuncios de venta de vehículos en Estados Unidos.

La aplicación permite visualizar patrones, distribuciones y relaciones entre variables clave como precio, kilometraje, tipo de vehículo y características técnicas, facilitando la toma de decisiones basada en datos.

---

## 🎯 Objetivo

Desarrollar un dashboard interactivo que permita:

* Analizar la distribución de variables relevantes
* Explorar relaciones entre características del vehículo
* Comparar fabricantes según diferentes atributos
* Identificar patrones en el mercado de vehículos usados

---

## 📂 Dataset

El conjunto de datos contiene más de **50,000 registros** de vehículos en venta, incluyendo:

* Precio
* Año del modelo
* Marca y modelo
* Condición
* Kilometraje (odómetro)
* Tipo de combustible
* Transmisión
* Tipo de carrocería
* Color
* Tracción (4WD)
* Fecha de publicación

---

## 🧹 Preprocesamiento de datos

Se realizó limpieza y transformación de datos para asegurar consistencia y calidad:

* Separación de la columna `model` en:

  * `brand` (marca)
  * `model_car` (modelo)
* Manejo de valores nulos:

  * `paint_color` → reemplazado por `"unknown"`
  * `is_4wd` → valores nulos imputados como `0`
* Conversión de tipos:

  * `date_posted` → formato `datetime`
  * Variables numéricas ajustadas para análisis
* Normalización de datos categóricos

---

## 📊 Funcionalidades de la aplicación

### 🔹 Exploración de datos

* Histograma del kilometraje (odómetro)
* Gráfica de dispersión: **Precio vs Kilometraje**

### 🔹 Análisis por categoría

Gráfica de barras apiladas que permite analizar la cantidad de vehículos por fabricante, segmentados por:

* Cilindros
* Condición
* Combustible
* Transmisión
* Tipo de carrocería
* Color
* Tracción (4WD)

✔ Visualización dinámica mediante selector interactivo
✔ Segmentación por categorías con codificación por color
✔ Identificación de patrones por fabricante

---

## 🛠️ Tecnologías utilizadas

* Python
* pandas
* Plotly
* Streamlit
