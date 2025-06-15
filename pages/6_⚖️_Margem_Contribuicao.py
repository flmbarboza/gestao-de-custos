import streamlit as st
import pandas as pd

def main():
    st.title("⚖️ Margem de Contribuição")
    
    st.markdown("""
    ### 📌 Conceito Fundamental
    ```
    MC = Receita - Custos Variáveis
    MCu = Preço - CVu
    ```
    """)
    
    # Simulador de múltiplos produtos
    st.subheader("📱 Simulador Multi-Produto")
    
    produtos = st.session_state.get("produtos", [{"nome": "", "preco": 0, "cvu": 0, "qtd": 0}])
    
    for i, prod in enumerate(produtos):
        with st.container(border=True):
            cols = st.columns(4)
            with cols[0]:
                produtos[i]["nome"] = st.text_input(f"Nome Produto {i+1}", prod["nome"])
            with cols[1]:
                produtos[i]["preco"] = st.number_input(f"Preço {i+1}", 0.0, 1000.0, prod["preco"])
            with cols[2]:
                produtos[i]["cvu"] = st.number_input(f"CVu {i+1}", 0.0, prod["preco"], prod["cvu"])
            with cols[3]:
                produtos[i]["qtd"] = st.number_input(f"Qtd {i+1}", 0, 1000, prod["qtd"])
    
    if st.button("➕ Adicionar Produto"):
        produtos.append({"nome": "", "preco": 0, "cvu": 0, "qtd": 0})
        st.session_state.produtos = produtos
        st.rerun()
    
    if st.button("Calcular MC"):
        df = pd.DataFrame(produtos)
        df["MCu"] = df["preco"] - df["cvu"]
        df["MC Total"] = df["MCu"] * df["qtd"]
        st.dataframe(df)
        
        st.metric("Margem de Contribuição Total", f"R$ {df['MC Total'].sum():.2f}")

if __name__ == "__main__":
    main()
