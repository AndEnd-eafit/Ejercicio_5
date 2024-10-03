import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from PIL import Image

translator = Translator()
st.title('Uso de TextBlob')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    ("""
    Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
    Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.

    Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
    (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        st.write('Texto ingresado: ', text1)  # Mostrar el texto ingresado

        blob = TextBlob(text1)
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        st.write('Polaridad: ', polarity)
        st.write('Subjetividad: ', subjectivity)
        
        if polarity >= 0.5:
            image = Image.open('Positivo.png')  
            st.image(image, caption='Sentimiento Positivo 😊')
        elif polarity <= -0.5:
            image = Image.open('Negativo.png')  
            st.image(image, caption='Sentimiento Negativo 😔')
        else:
            image = Image.open('Neutral.png')  
            st.image(image, caption='Sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
