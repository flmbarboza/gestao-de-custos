import streamlit as st

st.set_page_config(
    page_title="Gestão de Custos - UFU",
    page_icon="📊",
    layout="wide"
)

# Menu sidebar
st.sidebar.title("📚 Menu da Disciplina")
pagina = st.sidebar.radio(
    "Selecione o conteúdo:",
    [
        "🏠 Home",
        "1️⃣ Introdução à Contabilidade de Custos",
        "2️⃣ Custeio por Absorção",
        "3️⃣ Custeio Variável (Gerencial)",
        "4️⃣ Precificação e Tributos",
        "5️⃣ Margem de Contribuição",
        "📚 Bibliografia"
    ]
)

# Footer
st.sidebar.markdown("---")
st.sidebar.caption("Disciplina de Gestão de Custos - FAGEN/UFU")

# Roteamento
if "Home" in pagina:
    st.switch_page("pages/1_🏠_Home.py")
elif "Introdução" in pagina:
    st.switch_page("pages/2_📚_Introducao.py")
elif "Absorção" in pagina:
    st.switch_page("pages/3_📊_Custeio_Absorcao.py")
elif "Variável" in pagina:
    st.switch_page("pages/4_📈_Custeio_Variavel.py")
elif "Precificação" in pagina:
    st.switch_page("pages/5_💰_Precificacao.py")
elif "Margem" in pagina:
    st.switch_page("pages/6_⚖️_Margem_Contribuicao.py")
else:
    st.switch_page("pages/7_📑_Bibliografia.py")
