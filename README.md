# Evaluador Inteligente de Ofertas (Demo App)

Este prototipo permite subir un pliego de condiciones en texto plano (.txt) y utiliza GPT para generar:
- Un resumen ejecutivo
- Verificación de cumplimiento
- Análisis de riesgos
- Coincidencia con perfil de proveedor

## Requisitos
- Python 3.10+
- Streamlit
- OpenAI API Key

## Uso
1. Coloca tu clave de OpenAI en el archivo `.streamlit/secrets.toml`:
```
[OPENAI_API_KEY]
OPENAI_API_KEY = "sk-xxx"
```

2. Ejecuta localmente con:
```
streamlit run app.py
```

Este demo solo incluye el resumen. Puedes expandirlo con los otros prompts del guion original.