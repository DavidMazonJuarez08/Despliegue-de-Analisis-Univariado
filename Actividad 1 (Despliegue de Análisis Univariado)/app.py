#####################################################
#Importamos librerias
import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np
#####################################################

#Cargamos las bases que utilizaremos para el Dashboard
#Estas bases ya contienen las variables trabajadas anteriormente
df_marketing=pd.read_csv("Marketing_limpio.csv")
df_citas=pd.read_csv("Citas_Digital_limpio.csv")
df_funnel=pd.read_csv("Funnel_limpio.csv")
df_bitacora=pd.read_csv("Bitacora_limpio.csv")
df_volumen=pd.read_csv("Volumen_Leads_limpio.csv")
df_topsmkt=pd.read_csv("TOPS_MKT_limpio.csv")
df_topstdh=pd.read_csv("TOPS_TDH_limpio.csv")
df_canales=pd.read_csv("Principales_Canales_limpio.csv")
df_sdc=pd.read_csv("SDC_limpio.csv")
df_resumen=pd.read_csv("Resumen_limpio.csv")

###############################################################################
#CREAMOS EL DICCIONARIO CON LAS 15 VARIABLES CATEGÓRICAS
###############################################################################

Variables={
    "Nivel de Leads":df_marketing["Nivel de Leads"],
    "Prueba de Manejo":df_citas["PDM_categoria"],
    "Estatus de Lead":df_citas["Estatus de Lead"],
    "Potencial de Compra":df_citas["Potencial_categoria"],
    "Asesor Asignado":df_citas["Asesor Asignado"],
    "Canal del Funnel":df_funnel["Canal"],
    "Etapa del Funnel":df_funnel["Item"],
    "Asesor de Bitácora":df_bitacora["Asesor"],
    "Volumen de Leads":df_volumen["Volumen_Leads"],
    "Nivel de Afluencia":df_topsmkt["Categoria_Afluencia"],
    "Tamaño de Plantilla":df_topstdh["Categoria_Plantilla"],
    "Canal Principal":df_canales["Canal"],
    "Intervalo de Leads":df_canales["Categoria_Leads"],
    "Solicitudes Generadas":df_sdc["Categoria_Generadas"],
    "Leads del Resumen":df_resumen["Intervalo_Leads"]
}

#Lista con los nombres de las variables
Lista=list(Variables.keys())

###############################################################################
#CREACIÓN DEL DASHBOARD
###############################################################################

#Generamos los encabezados para la barra lateral
st.sidebar.title("GAC")

#Widget 1: Selectbox
#Menu desplegable de opciones de las páginas seleccionadas
View=st.sidebar.selectbox(label="Tipo de Análisis",
                          options=["Extracción de Características"])

###############################################################################
#CONTENIDO DE LA VISTA 1
###############################################################################

if View=="Extracción de Características":

    #EXTRACCIÓN DE CARACTERÍSTICAS

    #Select box para seleccionar una de las 15 variables
    Variable_Cat=st.sidebar.selectbox(label="Variables",options=Lista)

    #Obtenemos la variable seleccionada
    Variable=Variables[Variable_Cat]

    #Obtenemos las frecuencias de las categorías
    Tabla_frecuencias=Variable.value_counts().reset_index()

    #Ajustamos los nombres de las columnas
    Tabla_frecuencias.columns=["categorias","frecuencia"]

    #Calculamos el total
    total=Tabla_frecuencias["frecuencia"].sum()

    #Obtenemos la categoría con mayor frecuencia
    categoria_principal=Tabla_frecuencias.iloc[0]["categorias"]
    frecuencia_principal=Tabla_frecuencias.iloc[0]["frecuencia"]
    porcentaje_principal=(frecuencia_principal/total)*100

    #Generamos los encabezados para el dashboard
    st.title("GAC")
    st.subheader("Extracción de Características")
    st.write("Análisis univariado de variables categóricas")

    ###########################################################################
    #INDICADORES
    ###########################################################################

    Contenedor_1,Contenedor_2,Contenedor_3=st.columns(3)

    with Contenedor_1:
        st.metric("Total de registros",total)

    with Contenedor_2:
        st.metric("Número de categorías",len(Tabla_frecuencias))

    with Contenedor_3:
        st.metric("Categoría principal",str(categoria_principal))

    ###########################################################################
    #FILA 1
    ###########################################################################

    Contenedor_A,Contenedor_B=st.columns(2)

    with Contenedor_A:

        st.write("Grafico de Barras")

        #GRAPH 1: BARPLOT
        figure1=px.bar(data_frame=Tabla_frecuencias,
                       x="categorias",
                       y="frecuencia",
                       title="Frecuencia por categoría",
                       color="frecuencia",
                       color_continuous_scale="Reds")

        figure1.update_xaxes(automargin=True)
        figure1.update_yaxes(automargin=True)
        figure1.update_layout(height=300)

        st.plotly_chart(figure1,use_container_width=True)

    with Contenedor_B:

        st.write("Grafico de Pastel")

        #GRAPH 2: PIEPLOT
        figure2=px.pie(data_frame=Tabla_frecuencias,
                       names="categorias",
                       values="frecuencia",
                       title="Frecuencia por categoría",
                       color_discrete_sequence=["darkred","red","firebrick",
                                                "indianred","lightcoral","gray"])

        figure2.update_layout(height=300)

        st.plotly_chart(figure2,use_container_width=True)

    ###########################################################################
    #FILA 2
    ###########################################################################

    Contenedor_C,Contenedor_D=st.columns(2)

    with Contenedor_C:

        st.write("Grafico de anillo o dona")

        #GRAPH 3: DONUT PLOT
        figure3=px.pie(data_frame=Tabla_frecuencias,
                       names="categorias",
                       values="frecuencia",
                       hole=0.4,
                       title="Frecuencia por categoría",
                       color_discrete_sequence=["darkred","red","firebrick",
                                                "indianred","lightcoral","gray"])

        figure3.update_layout(height=300)

        st.plotly_chart(figure3,use_container_width=True)

    with Contenedor_D:

        st.write("Grafico de area")

        #GRAPH 4: AREA PLOT
        figure4=px.area(data_frame=Tabla_frecuencias,
                        x="categorias",
                        y="frecuencia",
                        title="Frecuencia por categoría")

        figure4.update_traces(line_color="darkred",fillcolor="lightcoral")
        figure4.update_layout(height=300)

        st.plotly_chart(figure4,use_container_width=True)

    ###########################################################################
    #WIDGET ADICIONAL: TABLA
    ###########################################################################

    st.write("Tabla de Frecuencias")

    #Calculamos el porcentaje de cada categoría
    Tabla_frecuencias["porcentaje"]=(Tabla_frecuencias["frecuencia"]/total)*100
    Tabla_frecuencias["porcentaje"]=Tabla_frecuencias["porcentaje"].round(2)

    st.dataframe(Tabla_frecuencias,use_container_width=True)

    ###########################################################################
    #HALLAZGO PRINCIPAL
    ###########################################################################

    st.write("Hallazgo principal")

    st.write("La categoría con mayor frecuencia es",categoria_principal,
             "con",frecuencia_principal,"registros, que representan",
             round(porcentaje_principal,2),"% del total.")
