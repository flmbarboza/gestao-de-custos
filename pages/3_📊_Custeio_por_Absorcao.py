import streamlit as st
import pandas as pd

def main():
    st.title("📊 Custeio por Absorção")

        # Lista de cards
    cards = [
        {"title": "Custo Direto Unitário (CDU)", "formula": "CDU = Custos Diretos Totais ÷ Quantidade Produzida"},
        {"title": "Custo Indireto Unitário (CIU)", "formula": "CIU = Custos Indiretos Totais ÷ Base de Rateio"},
        {"title": "Custo de Produção Unitário (CPU)", "formula": "CPU = CDU + CIU"},
        {"title": "Custo de Produção Total (CPT)", "formula": "CPT = CPU × Quantidade Produzida"},
        {"title": "Custo dos Produtos Vendidos (CPV)", "formula": "CPV = CPT - Estoques Finais"},
        {"title": "Resultado Bruto", "formula": "Resultado Bruto = Receita - CPV"},
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
    MP (ou MD) = EIMP + Compra MP - EFMP
    CPP = MP + MOD + CIF
    CPA = CPP + EIPP - EFPP
    CPV = CPA + EIPA - EFPA
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
