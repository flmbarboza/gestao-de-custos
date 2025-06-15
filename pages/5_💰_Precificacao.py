import streamlit as st

def main():
    st.title("💰 Precificação e Tributos")
    
    # Abordagem por abas
    tab1, tab2 = st.tabs(["Método Mark-up", "Impacto Tributário"])
    
    with tab1:
        st.markdown("""
        ### 🧮 Fórmula do Mark-up
        ```
        Preço = Custo / (1 - %Mark-up)
        ```
        """)
        
        custo = st.number_input("Custo do Produto (R$):", 1.0, 1000.0, 100.0)
        markup = st.slider("% Mark-up desejado:", 10, 200, 50)
        
        if st.button("Calcular Preço"):
            preco = custo / (1 - markup/100)
            st.success(f"Preço de Venda: R$ {preco:.2f}")
    
    with tab2:
        st.subheader("📊 Composição do Preço")
        
        col1, col2 = st.columns(2)
        with col1:
            icms = st.number_input("% ICMS:", 0.0, 100.0, 18.0)
            pis = st.number_input("% PIS:", 0.0, 100.0, 1.65)
        
        with col2:
            cofins = st.number_input("% COFINS:", 0.0, 100.0, 7.6)
            lucro = st.number_input("% Lucro:", 0.0, 100.0, 15.0)
        
        if st.button("Calcular Estrutura"):
            impostos = icms + pis + cofins
            custo_percent = 100 - impostos - lucro
            data = {
                "Componente": ["Custo", "Impostos", "Lucro"],
                "Percentual": [custo_percent, impostos, lucro]
            }
            st.bar_chart(data, x="Componente", y="Percentual")

if __name__ == "__main__":
    main()
