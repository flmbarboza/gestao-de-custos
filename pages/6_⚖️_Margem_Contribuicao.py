import streamlit as st
import pandas as pd
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google, safe_log_interacao

def main():
    st.title("⚖️ Margem de Contribuição")
    # Recupera o nome do usuário
    nome_usuario = get_anon_user_id()
    pagina_atual = "Margem"
    chave_log = f"acessou_{pagina_atual}_registrado"
    
    if not st.session_state.get(chave_log, False):
        log_acesso_google(nome_usuario, pagina_atual, f"acessou_{pagina_atual}")
        st.session_state[chave_log] = True
  
    st.markdown("""
    ### 📌 Conceito Fundamental
    ```
    MC = Receita - Custos Variáveis
    MCu = Preço - CVu
    ```
    """)
    
    # Inicializa a lista de produtos na session_state se não existir
    if 'produtos' not in st.session_state:
        st.session_state.produtos = [{"nome": "", "preco": 0.0, "cvu": 0.0, "qtd": 0}]
    
    # Simulador de múltiplos produtos
    st.subheader("📱 Simulador Multi-Produto")
    
    # Cria os campos para cada produto
    for i, prod in enumerate(st.session_state.produtos):
        with st.container(border=True):
            cols = st.columns(4)
            with cols[0]:
                st.session_state.produtos[i]["nome"] = st.text_input(
                    f"Nome Produto {i+1}", 
                    value=st.session_state.produtos[i]["nome"],
                    key=f"nome_{i}"
                )
            with cols[1]:
                st.session_state.produtos[i]["preco"] = st.number_input(
                    f"Preço {i+1} (R$)", 
                    min_value=0.0, 
                    max_value=10000.0, 
                    value=float(st.session_state.produtos[i]["preco"]),
                    step=0.01,
                    key=f"preco_{i}"
                )
            with cols[2]:
                st.session_state.produtos[i]["cvu"] = st.number_input(
                    f"Custo Variável {i+1} (R$)", 
                    min_value=0.0, 
                    max_value=float(st.session_state.produtos[i]["preco"]),
                    value=float(st.session_state.produtos[i]["cvu"]),
                    step=0.01,
                    key=f"cvu_{i}"
                )
            with cols[3]:
                st.session_state.produtos[i]["qtd"] = st.number_input(
                    f"Quantidade {i+1}", 
                    min_value=0, 
                    max_value=10000, 
                    value=int(st.session_state.produtos[i]["qtd"]),
                    key=f"qtd_{i}"
                )
    
    # Botões de ação
    col1, col2 = st.columns(2)
    with col1:
        if st.button("➕ Adicionar Produto"):
            st.session_state.produtos.append({"nome": "", "preco": 0.0, "cvu": 0.0, "qtd": 0})
            st.rerun()
    
    with col2:
        if st.button("🧹 Limpar Tudo"):
            st.session_state.produtos = [{"nome": "", "preco": 0.0, "cvu": 0.0, "qtd": 0}]
            st.rerun()
    
    if st.button("📊 Calcular Margem de Contribuição", type="primary"):
        try:
            df = pd.DataFrame(st.session_state.produtos)
            df["MCu"] = df["preco"] - df["cvu"]
            df["MC Total"] = df["MCu"] * df["qtd"]
            
            st.subheader("Resultados")
            st.dataframe(df.style.format({
                "preco": "R$ {:.2f}",
                "cvu": "R$ {:.2f}",
                "MCu": "R$ {:.2f}",
                "MC Total": "R$ {:.2f}"
            }))
            
            st.metric("Margem de Contribuição Total", 
                     f"R$ {df['MC Total'].sum():.2f}",
                     delta=f"{df['MC Total'].sum()/df['preco'].sum()*100:.1f}% sobre receita total")
        
        except Exception as e:
            st.error(f"Erro nos cálculos: {str(e)}")

if __name__ == "__main__":
    main()
