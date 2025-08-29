import streamlit as st
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google, safe_log_interacao

def main():
    st.title("💰 Precificação e Tributos")
    # Recupera o nome do usuário
    nome_usuario = get_anon_user_id()
    pagina_atual = "Markup"
    
    # Registra o acesso
    if 'page5_acessada' not in st.session_state:
        log_acesso_google(nome_usuario, pagina_atual, f"acessou_{pagina_atual}")
        st.session_state.page5_acessada = True

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
   
    st.divider()
    
    if st.button("👉 Avançar para o próximo tópico: Entender a Margem de Contribuição"):
        st.switch_page("pages/6_⚖️_Margem_Contribuicao.py")


if __name__ == "__main__":
    main()
