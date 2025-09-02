import streamlit as st
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google, safe_log_interacao

# Recupera o nome do usuário
nome_usuario = get_anon_user_id()
pagina_atual = "Bib"
chave_log = f"acessou_{pagina_atual}_registrado"

if not st.session_state.get(chave_log, False):
    log_acesso_google(nome_usuario, pagina_atual, f"acessou_{pagina_atual}")
    st.session_state[chave_log] = True

def main():
    st.title("📚 Bibliografia Recomendada")
    
    st.markdown("""
    ### 📕 Básica
    - MARTINS, Eliseu. **Contabilidade de Custos**. 10ª Ed. Atlas, 2010
    - HORNGREN, Charles et al. **Contabilidade de Custos** (Vol. I e II). 11ª Ed. Pearson, 2004
    
    ### 📘 Complementar
    - HANSEN, Don; MOWEN, Maryanne. **Gestão de custos**. Pioneira Thomson, 2003
    - ELDENBURG, Leslie. **Gestão de custos**. LTC, 2007
    """)
    
    st.subheader("🏛️ Informações Institucionais")
    st.markdown("""
    **Universidade Federal de Uberlândia**  
    Faculdade de Gestão e Negócios  
    Av. João Naves de Ávila, 2121 - Santa Mônica  
    Uberlândia/MG - CEP 38408-144
    """)

if __name__ == "__main__":
    main()
