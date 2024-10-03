import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from PIL import Image

# Estilos personalizados con tipografías Lexend e Inter
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lexend:wght@400;700&display=swap');
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');

    .title {
        font-family: 'Lexend', sans-serif;
        font-weight: 700;
        text-align: center;
    }

    .text {
        font-family: 'Inter', sans-serif;
        text-align: justify;
    }
    </style>
    """, unsafe_allow_html=True)

# Título
st.markdown('<h1 class="title">Uso de TextBlob</h1>', unsafe_allow_html=True)

translator = Translator()

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
        Polaridad: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
        Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
        
        Subjetividad: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo
        (hechos). Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    if text1:
        blob = TextBlob(text1)
       
        st.write('Polaridad: ', round(blob.sentiment.polarity, 2))
        st.write('Subjetividad: ', round(blob.sentiment.subjectivity, 2))
        x = round(blob.sentiment.polarity, 2)

        # Cargar imágenes
        if x >= 0.5:
            image = Image.open('Positivo.jpg')  # Asegúrate de tener la imagen "Positivo.jpg"
            st.image(image, caption='Sentimiento Positivo 😊')
        elif x <= -0.5:
            image = Image.open('Negativo.jpg')  # Asegúrate de tener la imagen "Negativo.jpg"
            st.image(image, caption='Sentimiento Negativo 😔')
        else:
            image = Image.open('Neutral.jpg')  # Asegúrate de tener la imagen "Neutral.jpg"
            st.image(image, caption='Sentimiento Neutral 😐')

with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
