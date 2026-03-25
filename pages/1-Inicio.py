import streamlit as st                  


st.sidebar.title("Menú de Navegación")
opcion = st.sidebar.radio(
    "Selecciona una opción:",
    ("Inicio", "Análisis de Datos", "Configuración", "Ayuda")
)

if opcion == "Inicio":
    st.title("Página de Inicio")
    st.write("Bienvenido a la aplicación.")
elif opcion == "Análisis de Datos":
    st.title("Análisis de Datos")
    # Contenido de análisis...


tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
   st.header("A cat")
   st.image("https://static.streamlit.io/examples/cat.jpg")

with tab2:
   st.header("A dog")
   st.image("https://static.streamlit.io/examples/dog.jpg")

with tab3:
   st.header("An owl")
   st.image("https://static.streamlit.io/examples/owl.jpg")





menu = ["Inicio", "Calculadora", "Acerca de"]
choice = st.selectbox("Menú de Navegación", menu)

if choice == "Inicio":
    st.title("Página Principal")
elif choice == "Calculadora":
    st.title("Calculadora")
    # Contenido de la calculadora...





col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Inicio"):
        st.session_state.page = "home"
with col2:
    if st.button("Productos"):
        st.session_state.page = "products"
with col3:
    if st.button("Contacto"):
        st.session_state.page = "contact"

if "page" not in st.session_state:
    st.session_state.page = "home"

if st.session_state.page == "home":
    st.title("Bienvenido")
elif st.session_state.page == "products":
    st.title("Nuestros Productos")




with st.sidebar:
    with st.expander("Sección 1"):
        option1 = st.checkbox("Opción 1.1")
        option2 = st.checkbox("Opción 1.2")

    with st.expander("Sección 2"):
        option3 = st.radio("Selecciona", ["A", "B", "C"])



st.markdown("""
<style>
    .menu {
        display: flex;
        gap: 10px;
        padding: 10px;
        background-color: #f0f2f6;
        border-radius: 5px;
    }
    .menu-item {
        padding: 8px 16px;
        cursor: pointer;
    }
    .menu-item:hover {
        background-color: #ddd;
    }
</style>

<div class="menu">
    <div class="menu-item" onclick="alert('Inicio')">Inicio</div>
    <div class="menu-item" onclick="alert('Productos')">Productos</div>
    <div class="menu-item" onclick="alert('Contacto')">Contacto</div>
</div>
""", unsafe_allow_html=True)