from altair.vegalite.v4.api import value
import streamlit as st
from streamlit.proto.RootContainer_pb2 import SIDEBAR
#APP con una regla de edad (linea) que con el aumento de la edad se pueda desplegar los
#riesgos mas importantes y como prevenirlos
st.image("medpost.jpeg")
st.sidebar.subheader("Coloca tu edad en la barra y se desplegarán los riesgos a la salud más importanes, así como recomendaciones actualizadas según las guias internacionales y de México")
edad=st.slider('Edad',1,100,value=None,step=1)
if edad==32:
    st.balloons()
    st."Felicidades te amo, viejita"