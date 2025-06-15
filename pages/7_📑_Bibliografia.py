import streamlit as st

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
