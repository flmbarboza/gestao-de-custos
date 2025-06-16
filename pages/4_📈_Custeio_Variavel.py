import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    st.title("📈 Custeio Variável (Gerencial)")
    
    # Teoria com abas
    tab1, tab2, tab3 = st.tabs(["Conceitos", "DRE Comparativa", "Simulador"])
    
    with tab1:
        st.markdown("""
        ### 💡 Princípios do Custeio Variável
        - **Custos Fixos:** tratados como despesa do período
        - **Margem de Contribuição:** Receita - Custos Variáveis
        - **Fórmula:**
        ```
        MC = PV - CV
        Resultado = MC - CF
        ```
        """)
    
    with tab2:
        st.subheader("🔍 Comparativo DRE")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("**Custeio Absorção**")
            st.table(pd.DataFrame({
                "Item": ["Receita", "CPV", "Lucro Bruto", "Despesas", "Lucro Líquido"],
                "Valor": [100000, 60000, 40000, 15000, 25000]
            }))
        
        with col2:
            st.markdown("**Custeio Variável**")
            st.table(pd.DataFrame({
                "Item": ["Receita", "Custos Variáveis", "Margem Contribuição", "Custos Fixos", "Lucro"],
                "Valor": [100000, 50000, 50000, 30000, 20000]
            }))
    
    with tab3:
        st.subheader("🧮 Simulador Ponto de Equilíbrio")
        preco = st.slider("Preço Unitário (R$):", 10, 200, 50)
        cv = st.slider("Custo Variável Unitário (R$):", 1, 150, 30)
        cf = st.slider("Custos Fixos Totais (R$):", 1000, 50000, 20000)
        
        # Cálculos
        mc = preco - cv
        qe = cf / mc if mc != 0 else 0
        
        # Gráfico
        q_range = np.linspace(0, qe*2, 100)
        rt = preco * q_range
        ct = cf + cv * q_range
        
        fig, ax = plt.subplots()
        ax.plot(q_range, rt, label='Receita Total')
        ax.plot(q_range, ct, label='Custo Total')
        ax.axvline(x=qe, color='r', linestyle='--', label='Ponto de Equilíbrio')
        ax.set_xlabel("Quantidade")
        ax.set_ylabel("R$")
        ax.legend()
        st.pyplot(fig)
        
        st.metric("Ponto de Equilíbrio", f"{qe:.0f} unidades")

if __name__ == "__main__":
    main()
