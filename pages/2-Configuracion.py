import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# st.set_page_config must be called in the main page (App.py) or as the very first command.
# Since it's already in App.py, we don't necessarily need it, but it's okay to have page-specific setups if it's the first command.
# However, Streamlit usually complains if set_page_config is called multiple times. We'll skip it here to be safe and just use UI elements.

st.title("⚙️ Configuración del Dashboard")

st.markdown("Ajusta los parámetros visuales y de datos aquí. Los cambios se reflejarán instantáneamente en el gráfico de abajo usando **Matplotlib**.")

# Columnas para organizar los controles
col1, col2 = st.columns(2)

with col1:
    st.subheader("Configuración Visual")
    color = st.color_picker("Color Principal del Gráfico", "#1E88E5")
    tipo_grafico = st.selectbox("Tipo de Gráfico", ["Línea", "Dispersión (Scatter)", "Barras"])

with col2:
    st.subheader("Configuración de Datos")
    num_puntos = st.slider("Número de Datos", min_value=10, max_value=500, value=100)
    ruido = st.slider("Nivel de Ruido", min_value=0.0, max_value=2.0, value=0.5, step=0.1)

# Generación de datos simulados
np.random.seed(42)
x = np.linspace(0, 10, num_puntos)
y = np.sin(x) + np.random.normal(0, ruido, num_puntos)

st.divider()

# Creación del gráfico con Matplotlib
st.subheader("Vista Previa del Gráfico")

fig, ax = plt.subplots(figsize=(10, 4))
fig.patch.set_facecolor('none') # Fondo transparente para que combine con tema oscuro/claro de Streamlit
ax.set_facecolor('none')

if tipo_grafico == "Línea":
    ax.plot(x, y, color=color, linewidth=2)
elif tipo_grafico == "Dispersión (Scatter)":
    ax.scatter(x, y, color=color, alpha=0.7)
elif tipo_grafico == "Barras":
    # Limitamos los puntos si son muchos para gráficos de barra
    puntos_barra = min(50, num_puntos)
    x_bar = x[:puntos_barra]
    y_bar = y[:puntos_barra]
    ancho = 10 / max(1, len(x_bar)) * 0.8
    ax.bar(x_bar, y_bar, color=color, width=ancho)

ax.set_title("Efecto de la Configuración en Tiempo Real", color="gray")
ax.set_xlabel("Tiempo (s)", color="gray")
ax.set_ylabel("Amplitud", color="gray")

# Estilizar bordes y texto para que se vea moderno
ax.tick_params(colors="gray")
for spine in ax.spines.values():
    spine.set_color("lightgray")
    
ax.grid(True, linestyle="--", alpha=0.3, color="gray")

# Mostrar gráfico en la aplicación de Streamlit
st.pyplot(fig)
