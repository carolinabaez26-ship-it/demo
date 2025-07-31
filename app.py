import streamlit as st
import openai

st.set_page_config(page_title="Evaluador Inteligente de Ofertas", layout="wide")

st.title("🤖 Evaluador Inteligente de Ofertas para Contrataciones Públicas")

openai.api_key = st.secrets["OPENAI_API_KEY"]

uploaded_file = st.file_uploader("📄 Sube el pliego en formato .txt", type=["txt"])

if uploaded_file:
    tender_text = uploaded_file.read().decode("utf-8")

    # Prompt 1: Resumen Ejecutivo
    st.subheader("📋 Resumen Ejecutivo")
    prompt1 = f"""
    Actúa como un asistente de contrataciones. Resume este pliego de condiciones incluyendo:
    1. Objeto del contrato
    2. Monto estimado
    3. Requisitos principales
    4. Plazo de ejecución
    5. Fecha límite de entrega

    Texto del pliego:
    {tender_text}
    """

    response1 = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt1}]
    )

    resumen = response1["choices"][0]["message"]["content"]
    st.text_area("Resumen:", resumen, height=200)