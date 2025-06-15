import streamlit as st

def main():
    st.title("📚 Introdução à Contabilidade de Custos")
    
    with st.expander("📌 Objetivos da Unidade", expanded=True):
        st.markdown("""
        - Compreender terminologia básica de custos
        - Classificar custos por natureza e comportamento
        - Analisar o comportamento de custos
        """)
    
    st.subheader("🧠 Conceitos Fundamentais")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Classificação de Custos:**
        - Diretos vs. Indiretos
        - Fixos vs. Variáveis
        - Custos vs. Despesas
        """)
        
    with col2:
        st.markdown("""
        **Terminologia:**
        - Custo Primário
        - Custo de Transformação
        - Custo Total
        """)
    
    # Quiz interativo
    with st.expander("🧩 Teste Seu Conhecimento"):
        resposta = st.radio(
            "O salário do supervisor de produção é classificado como:",
            ["Custo Direto", "Custo Indireto", "Despesa"],
            index=None
        )
        if resposta:
            if resposta == "Custo Indireto":
                st.success("✅ Correto! É um custo indireto pois beneficia toda a produção.")
            else:
                st.error("❌ Revise a classificação de custos indiretos")

if __name__ == "__main__":
    main()
