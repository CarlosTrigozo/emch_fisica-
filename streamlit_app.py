import streamlit as st
import random

# Función para generar ejercicios de cinemática
def generar_ejercicio():
    # Lista de ejemplos de problemas de cinemática
    problemas = [
        {"enunciado": "Un coche parte del reposo y acelera uniformemente hasta 20 m/s en 5 segundos. ¿Cuál es su aceleración?", 
         "respuesta": 4},  # Respuesta en m/s^2 (aceleración)
        
        {"enunciado": "Una pelota es lanzada hacia arriba con una velocidad de 15 m/s. ¿Cuánto tiempo tarda en alcanzar su altura máxima? (g=9.8 m/s^2)", 
         "respuesta": 1.53},  # Respuesta en segundos

        {"enunciado": "Un objeto en movimiento rectilíneo recorre 100 metros en 20 segundos. ¿Cuál es su velocidad promedio?", 
         "respuesta": 5},  # Respuesta en m/s
    ]
    return random.choice(problemas)

# Interfaz de la aplicación
st.title('Generador de Ejercicios de Cinemática')

# Generar un nuevo ejercicio
ejercicio = generar_ejercicio()

st.subheader("Ejercicio:")
st.write(ejercicio["enunciado"])

# Entrada del usuario para la respuesta
respuesta_usuario = st.number_input("Introduce tu respuesta (en unidades correctas):", min_value=0.0)

# Verificar la respuesta cuando el botón es presionado
if st.button('Verificar respuesta'):
    # Verificar si la respuesta está dentro de un margen de error razonable (para posibles errores de redondeo)
    if abs(respuesta_usuario - ejercicio["respuesta"]) < 0.1:
        st.success("¡Correcto! La respuesta es {:.2f}".format(ejercicio["respuesta"]))
    else:
        st.error("Incorrecto. La respuesta correcta es {:.2f}".format(ejercicio["respuesta"]))
