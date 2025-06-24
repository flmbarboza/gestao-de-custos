import streamlit as st
import pandas as pd

def main():
    st.title("📊 Custeio por Absorção")

        # Lista de cards
    cards = [
        {"title": "Matéria-Prima (MP)", "formula": "MP = EIMP + Compra MP - EFMP"},
        {"title": "Custo de Produção do Período (CPP)", "formula": "CPP = MP + MOD + CIF"},
        {"title": "Custo do Produto Acabado (CPA)", "formula": "CPA = CPP + EIPP - EFPP"},
        {"title": "Custo dos Produtos Vendidos (CPV)", "formula": "CPV = CPA + EIPA - EFPA"}
    ]

    # Renderização dos cards em 3 colunas
    cols = st.columns(3)
    
    for idx, card in enumerate(cards):
        with cols[idx % 3]:
            st.markdown(
                f"""
                <div style="background-color: #f0f2f6; padding: 20px; border-radius: 10px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); margin-bottom: 20px;">
                    <h4 style="color: #0e1117;">{card['title']}</h4>
                    <p style="font-size: 18px; color: #262730;"><strong>{card['formula']}</strong></p>
                </div>
                """,
                unsafe_allow_html=True
            )
    st.markdown("""
    ### 🧮 Esquema Básico
    ```
    1o. Passo) Separar Custos e Despesas
    2o. Passo) Apropriar dos Custos Diretos
    3o. Passo) Rateio dos Custos Indiretos
    ```
    """)
    
    # Simulador interativo
    st.subheader("📱 Simulador de Custeio")
    col1, col2 = st.columns(2)
    
    with col1:
        mp = st.number_input("Matéria-Prima (R$):", 1000, 100000, 5000)
        mod = st.number_input("Mão de Obra (R$):", 1000, 100000, 3000)
    
    with col2:
        cif = st.number_input("Custos Indiretos (R$):", 1000, 100000, 2000)
        ei = st.number_input("Estoque Inicial (R$):", 0, 100000, 0)
        ef = st.number_input("Estoque Final (R$):", 0, 100000, 1000)
    
    if st.button("Calcular"):
        cpp = mp + mod + cif
        cpa = cpp + ei - ef
        
        resultados = pd.DataFrame({
            "Conceito": ["CPP", "CPA"],
            "Valor (R$)": [cpp, cpa]
        })
        
        st.bar_chart(resultados.set_index("Conceito"))
        st.table(resultados)
    
    st.divider()
    
    if st.button("👉 Avançar para o próximo tópico: Conhecer o Método de Custeio Variável"):
        st.switch_page("pages/4_📈_Custeio_Variavel.py")


if __name__ == "__main__":
    main()
