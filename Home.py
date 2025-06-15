import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Gestão de Custos - UFU",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estado de sessão para controle
if 'pagina_atual' not in st.session_state:
    st.session_state.pagina_atual = "Home"

# Menu sidebar
with st.sidebar:
    st.title("📚 Menu da Disciplina")
    
    # Botões de navegação personalizados
    if st.button("🏠 Home", use_container_width=True):
        st.session_state.pagina_atual = "Home"
    
    if st.button("📚 Introdução à Contabilidade de Custos", use_container_width=True):
        st.session_state.pagina_atual = "Introducao"
    
    if st.button("📊 Custeio por Absorção", use_container_width=True):
        st.session_state.pagina_atual = "Absorcao"
    
    if st.button("📈 Custeio Variável", use_container_width=True):
        st.session_state.pagina_atual = "Variavel"
    
    if st.button("💰 Precificação", use_container_width=True):
        st.session_state.pagina_atual = "Precificacao"
    
    if st.button("⚖️ Margem de Contribuição", use_container_width=True):
        st.session_state.pagina_atual = "Margem"
    
    if st.button("📑 Bibliografia", use_container_width=True):
        st.session_state.pagina_atual = "Bibliografia"
    
    st.markdown("---")
    st.caption("Gestão de Custos - FAGEN/UFU")

# Sistema de roteamento seguro
if st.session_state.pagina_atual == "Home":
    from pages import 1_🏠_Home as page
elif st.session_state.pagina_atual == "Introducao":
    from pages import 2_📚_Introducao as page
elif st.session_state.pagina_atual == "Absorcao":
    from pages import 3_📊_Custeio_Absorcao as page
elif st.session_state.pagina_atual == "Variavel":
    from pages import 4_📈_Custeio_Variavel as page
elif st.session_state.pagina_atual == "Precificacao":
    from pages import 5_💰_Precificacao as page
elif st.session_state.pagina_atual == "Margem":
    from pages import 6_⚖️_Margem_Contribuicao as page
else:
    from pages import 7_📑_Bibliografia as page

# Renderiza a página selecionada
page.main()
