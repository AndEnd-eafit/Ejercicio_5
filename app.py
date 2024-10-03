import streamlit as st
from textblob import TextBlob
from PIL import Image
import os

st.title('Uso de TextBlob')

st.subheader("Por favor, escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.write(
        """
        **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
        
        **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
        """
    )

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        blob = TextBlob(text1)

        # Mostrar polaridad y subjetividad
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)
        
        st.write('Polaridad: ', polarity)
        st.write('Subjetividad: ', subjectivity)

        # Mostrar imagen según la polaridad
        if polarity >= 0.5:
            image_path = 'Positivo.jpg'
            caption = 'Sentimiento Positivo 😊'
        elif polarity <= -0.5:
            image_path = 'Negativo.jpg'
            caption = 'Sentimiento Negativo 😔'
        else:
            image_path = 'Neutral.jpg'
            caption = 'Sentimiento Neutral 😐'

        if os.path.exists(image_path):
            image = Image.open(image_path)
            st.image(image, caption=caption)
        else:
            st.error(f"La imagen '{image_path}' no se encontró.")

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())

    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
