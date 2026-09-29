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
#REVISIÓN DE LAS VARIABLES DISPONIBLES
###############################################################################

st.title("GAC")
st.subheader("Revisión de variables disponibles")

Bases={
    "Marketing":df_marketing,
    "Citas Digital":df_citas,
    "Funnel":df_funnel,
    "Bitácora de Piso":df_bitacora,
    "Volumen de Leads":df_volumen,
    "TOPS MKT":df_topsmkt,
    "TOPS TDH":df_topstdh,
    "Principales Canales":df_canales,
    "SDC":df_sdc,
    "Resumen":df_resumen
}

Base=st.selectbox("Selecciona una base",list(Bases.keys()))

st.write("Columnas disponibles:")
st.write(Bases[Base].columns.tolist())

st.write("Vista previa:")
st.dataframe(Bases[Base].head())