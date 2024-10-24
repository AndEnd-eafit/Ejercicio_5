import streamlit as st
from textblob import TextBlob
from googletrans import Translator
from PIL import Image

# Inicializar el traductor
translator = Translator()
st.title('Uso de TextBlob para Análisis de Sentimiento')

st.subheader("Por favor escribe en el campo de texto la frase que deseas analizar")

with st.sidebar:
    st.subheader("Polaridad y Subjetividad")
    st.markdown("""
        - **Polaridad**: Indica si el sentimiento expresado en el texto es positivo, negativo o neutral. 
          Su valor oscila entre -1 (muy negativo) y 1 (muy positivo), con 0 representando un sentimiento neutral.
        
        - **Subjetividad**: Mide cuánto del contenido es subjetivo (opiniones, emociones, creencias) frente a objetivo (hechos). 
          Va de 0 a 1, donde 0 es completamente objetivo y 1 es completamente subjetivo.
    """)

# Análisis de polaridad y subjetividad
with st.expander('Analizar Polaridad y Subjetividad en un texto'):
    text1 = st.text_area('Escribe por favor: ')
    
    if text1:
        # Traducir el texto al inglés si es necesario
        translation = translator.translate(text1, src="es", dest="en")
        translated_text = translation.text
        st.write(f"Texto traducido: {translated_text}")

        # Crear el objeto TextBlob con el texto traducido
        blob = TextBlob(translated_text)

        # Obtener polaridad y subjetividad
        polarity = round(blob.sentiment.polarity, 2)
        subjectivity = round(blob.sentiment.subjectivity, 2)

        # Mostrar polaridad y subjetividad
        st.write('Polaridad: ', polarity)
        st.write('Subjetividad: ', subjectivity)

        # Mostrar imagen según la polaridad
        if polarity >= 0.5:
            st.image('Positivo.png', caption='Sentimiento Positivo 😊', use_column_width=True)
        elif polarity <= -0.5:
            st.image('Negativo.png', caption='Sentimiento Negativo 😔', use_column_width=True)
        else:
            st.image('Neutral.png', caption='Sentimiento Neutral 😐', use_column_width=True)

# Corrección en inglés
with st.expander('Corrección en inglés'):
    text2 = st.text_area('Escribe por favor: ', key='4')
    
    if text2:
        blob2 = TextBlob(text2)
        st.write(blob2.correct())
