import streamlit as st
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google

def main():
    st.title("🏦 Gestão de Custos - FAGEN/UFU")

    # Recupera o nome do usuário do session_state (da home)
    nome_usuario = get_anon_user_id()
    pagina_atual = "Inicio"

    # Texto de boas-vindas
    texto_boas_vindas = """
    Bem-vindo à plataforma interativa da disciplina Gestão de Custos. Aqui você aprenderá:
    - Os fundamentos da contabilidade de custos
    - Métodos de custeio (absorção e variável)
    - Técnicas de precificação
    - Análise de margem de contribuição
    - E muito mais!
    """
    st.markdown(texto_boas_vindas)

    # Expander normal
    with st.expander("🎯 Objetivos da Disciplina", expanded=False):
        st.markdown("""
        - Apresentar conceitos de registro, apuração e controle de custos
        - Fornecer visão ampla da contabilidade financeira e gerencial
        - Analisar impactos tributários em custos e preços
        - Desenvolver habilidades para tomada de decisão com restrições
        """)
    
        # ✅ BOTÃO INVISÍVEL PARA DETECTAR A ABERTURA
        if st.button("✅ Marcar: Visualizei os objetivos", key="btn_objetivos"):
            # Registra no Google Sheets
            log_interacao_google(nome_usuario, pagina_atual, "expandiu_objetivos")
            st.toast("Obrigado por explorar os objetivos! 🎯", icon="💡")
            
    # Ementa interativa
    st.subheader("📚 Programa da Disciplina")
    cols = st.columns(3)
    unidades = [
        ("1️⃣ Introdução a Custos", "Terminologia, Classificação e Comportamento de Custos"),
        ("2️⃣ Custeio por Absorção", "CPP, CPA, CPV, Rateio de CIF, DRE"),
        ("3️⃣ Custeio Variável", "Margem de Contribuição, Ponto de Equilíbrio"),
        ("4️⃣ Precificação", "Método Mark-up, Impacto Tributário"),
        ("5️⃣ Margem de Contribuição", "Limitações na Capacidade Produtiva")
    ]

    for i, (unidade, desc) in enumerate(unidades):
        botao_key = f"botao_unidade_{i}"
        if cols[i % 3].button(unidade, help=desc, use_container_width=True, key=botao_key):
            # Registra o clique
            log_interacao_google(nome_usuario, pagina_atual, f"clicou_unidade_{i+1}")
            st.toast(f"Ótimo! Você selecionou: {unidade}", icon="✅")

    # Botão de áudio (exemplo futuro)
    # if st.button("🎧 Ouvir Apresentação"):
    #     log_interacao(nome_usuario, pagina_atual, "ouviu_apresentacao")
    #     texto_audio = texto_boas_vindas + "\nObjetivos: " + " ".join([
    #         "Apresentar conceitos, ",
    #         "Fornecer visão ampla, ",
    #         "Analisar impactos..."
    #     ])
    #     leitor_de_texto(texto_audio)
    #     st.success("Áudio reproduzido!")

if __name__ == "__main__":
    main()
