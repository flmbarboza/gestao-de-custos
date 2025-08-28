import streamlit as st
from datetime import datetime
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google

# Configuração da página
st.set_page_config(
    page_title="Gestão de Custos Academy",
    page_icon="🏦",
    layout="centered"  # Layout mais clean para a página inicial
)

# === REGISTRA O ACESSO À PÁGINA (APENAS UMA VEZ POR SESSÃO) ===
user_id = get_anon_user_id()

if 'home_acessada' not in st.session_state:
    # ✅ Registra que a home foi acessada
    log_acesso_google(nome_usario,"home", acao="acessou_home")  # ← Registro silencioso de visualização
    st.session_state.home_acessada = True
    # Não mostra nada, só registra

# ===============================================================

# Mensagem de boas-vindas (aparece apenas na root URL)
if not st.session_state.get('redirecionado'):
    st.session_state.redirecionado = True

    st.title("🏦 Bem-vindo ao Gestão de Custos Academy!")
    st.markdown("""
    ## 👋 Olá, [futuro] Gestor de Custos!
    
    Esta plataforma foi desenvolvida para auxiliar no desenvolvimento de análises e na tomada de decisão de custos
    por meio de fundamentos associados a tema, no âmbito do curso superior em Administração.
    """)

    st.image("pages/figs/welcome.png")

    # ✅ Gera um ID anônimo para este visitante
    user_id = get_anon_user_id()

    # ✅ Registra o acesso no Google Sheets
    log_acesso_google(
        nome=user_id,
        email="anonimo",  # ou deixe vazio
        pagina="home"
    )

   # ✅ Mensagem de boas-vindas anônima
    st.success(f"✅ Sua sessão foi iniciada! ID: {user_id}")
    st.info("Seus dados de uso serão coletados de forma anônima para melhorar a plataforma.")

    # ✅ Link para continuar
    st.markdown("""
    ### Como começar?
    1. Clique no botão abaixo
    2. Siga o fluxo de estudos
    3. Explore as ferramentas interativas
    """)

      # Mensagem de privacidade
    st.markdown("""
    ---
    <p style="font-size: 12px; color: gray; text-align: center;">
        **Disclosure**: Este site coleta dados de uso de forma anônima para fins educacionais. 
        Nenhum dado pessoal é solicitado ou armazenado sem consentimento.
    </p>
    """, unsafe_allow_html=True)

if st.button("➡️ Ir para o INÍCIO da jornada", key="btn_inicio"):
    # Gera ou recupera o ID anônimo
    user_id = get_anon_user_id()
    
    # Registra a intenção de navegar
    log_interacao_google(
        nome=user_id,
        pagina="home",
        acao="clicou_link_inicio"
    )
    
    # Redireciona
    st.switch_page("pages/1_🏠_Inicio.py")
    
# Footer (aparece em todas as páginas)
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    Gestão de Custos Academy (versão beta)<br>
    Desenvolvido para a disciplina de <br>
    Gestão de Custos <br>
    FAGEN/UFU
</div>
""", unsafe_allow_html=True)
