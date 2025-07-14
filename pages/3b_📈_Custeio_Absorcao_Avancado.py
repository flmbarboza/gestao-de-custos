import streamlit as st
import pandas as pd

def main():
    st.title("📈 Custeio por Absorção - Avançado")
    st.write("""
    **Departamentalização e critérios de rateio**  
    Distribuição dos custos indiretos por centros de custo e produtos.
    """)
    
    st.subheader("🏭 Departamentalização")
    col1, col2 = st.columns(2)
    with col1:
        st.selectbox("Critério de Rateio 1", ["Horas-Máquina", "Mão-de-Obra"])
    with col2:
        st.selectbox("Critério de Rateio 2", ["Área", "Produção Equivalente"])
    
    # Exemplo prático de rateio
    with st.expander("📝 Exemplo Completo de Rateio"):
        custos = pd.DataFrame({
            "Departamento": ["Montagem", "Acabamento", "Administração"],
            "Custo Direto": [15000, 12000, 8000],
            "Horas-Máquina": [200, 150, 50]
        })
        st.dataframe(custos)
        
        if st.button("Calcular Rateio"):
            custos["Rateio"] = custos["Horas-Máquina"] / custos["Horas-Máquina"].sum()
            st.success("Custos rateados proporcionalmente às horas-máquina")

    if st.button("⬅️ Voltar para Versão Básica"):
        st.switch_page("pages/3_📊_Custeio_Absorcao.py")

if __name__ == "__main__":
    main()
