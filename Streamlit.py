import streamlit as st
import pandas as pd
import plotly.express as px
import datetime as dt

data = pd.read_csv('Precios2.txt',delimiter=';',names=['fecha','Huawei Watch Fit 2','Huawei Watch Fit New','Dolar Blue','Dolar Oficial'])

data['month'] = pd.DatetimeIndex(data['fecha']).month
data['year'] = pd.DatetimeIndex(data['fecha']).year

data = data.sort_values("fecha",ascending=False)

data2 = data.iloc[:, [0,3,4,5,6]]

st.set_page_config(
     page_title="Cotizacion Dolar",
     page_icon=":dollar:")

st.title(":dollar: Evolucion de Precios")

data3=data2.head(2)
data5 = int(data3["Dolar Blue"].iloc[-2])
data4 = int(data3["Dolar Blue"].iloc[-1])
data6 = (data5-data4)
st.metric(label="Dolar Blue", value=data5, delta=data6)

data7=data2.head(2)
data8 = float(data7["Dolar Oficial"].iloc[-2])
data9 = float(data7["Dolar Oficial"].iloc[-1])
data10 = round((data8-data9),2)
st.metric(label="Dolar Oficial", value=data8, delta=data10)

st.header(":money_with_wings:Dolar Oficial Vs Dolar Blue")
st.markdown("##")

st.sidebar.header("Filtros:")
month = st.sidebar.multiselect(
    "Seleccionar mes:",
    options=data2["month"].unique(),
    default=data2["month"].unique(),
)


year = st.sidebar.multiselect(
    "Seleccionar año:",
    options=data2["year"].unique(),
    default=data2["year"].unique(),
)


data2_selection = data2.query("year == @year", inplace=True)
data3_selection = data2.query("month == @month")

st.dataframe(data3_selection)

st.markdown("##")

grafico = st.checkbox("Ver Grafico")

x1 = data2["fecha"].iloc[0]
print(x1)

if grafico:
    fig = px.line(data3_selection, x='fecha',y="Dolar Blue",title='Evolucion de Precios', template='plotly_dark')
    st.write(fig)
    fig = px.line(data3_selection, x='fecha',y="Dolar Oficial",title='Evolucion de Precios', template='plotly_dark')
    fig.update_traces(line_color="#32CD32")
    st.write(fig)



#data2_selection.columns
