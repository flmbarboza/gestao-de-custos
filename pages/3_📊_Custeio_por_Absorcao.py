import streamlit as st
import pandas as pd
from graphviz import Digraph 

def main():
    st.title("📊 Custeio por Absorção")

        # Lista de cards
    cards = [
        {"title": "Matéria-Prima (MP, ou MD - Material Direto)", "formula": "MP = EIMP + Compra MP - EFMP"},
        {"title": "Custo de Produção do Período (CPP)", "formula": "CPP = MP + MOD + CIF"},
        {"title": "Custo do Produto Acabado (CPA)", "formula": "CPA = CPP + EIPP - EFPP"},
        {"title": "Custo dos Produtos Vendidos (CPV)", "formula": "CPV = CPA + EIPA - EFPA"}
    ]

    # Renderização dos cards em 3 colunas
    cols = st.columns(2)
    
    for idx, card in enumerate(cards):
        with cols[idx % 2]:
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

    Veja a figura para entender o esquema:
    """)

    # Criação do diagrama
    dot = Digraph('CusteioPorAbsorcao')
    dot.attr(rankdir='LR', splines='curved', ranksep='2')  # ranksep maior para espaçar verticalmente
    
    node_attr = {'shape': 'box', 'style': 'rounded,filled', 'color': 'cyan', 'fontname': 'Arial'}
    
    # Nós principais
    dot.node('C', 'Custos', **node_attr)
    dot.node('D', 'Despesas', **node_attr)
    dot.node('V', 'Vendas', **node_attr)
    dot.node('R', 'Resultado', **node_attr)
    
    # Colocar CI e CD em ranks diferentes para espaçar verticalmente
    with dot.subgraph() as s1:
        s1.attr(rank='same')
        s1.node('CI', 'Indiretos', **node_attr)
    with dot.subgraph() as s2:
        s2.attr(rank='same')
        s2.node('CD', 'Diretos', **node_attr)
    
    # Agora forçar CD ficar um pouco acima e CI um pouco abaixo, criando nós invisíveis para "empurrar" verticalmente
    dot.node('invis_top', label='', shape='point', width='0', height='0', style='invis')
    dot.node('invis_bottom', label='', shape='point', width='0', height='0', style='invis')
    
    dot.edge('invis_top', 'CD', style='invis')
    dot.edge('CI', 'invis_bottom', style='invis')
    
    # Conectar C a CI e CD (sem alterar minlen, pq o foco é vertical)
    dot.edge('C', 'CI')
    dot.edge('C', 'CD')
    
    # Produtos
    dot.node('PA', 'Produto A', **node_attr)
    dot.node('PB', 'Produto B', **node_attr)
    dot.node('PC', 'Produto C', **node_attr)
    
    # Estoque e CPV
    dot.node('E', 'Estoque', **node_attr)
    dot.node('CPV', 'Custo dos Produtos Vendidos', **node_attr)
    
    # Fluxo de custos indiretos via rateio (curvas vermelhas)
    dot.edge('CI', 'PA', xlabel="Rateio", color="red", fontcolor="red", style='bold')
    dot.edge('CI', 'PB', xlabel="Rateio", color="red", fontcolor="red", style='bold')
    dot.edge('CI', 'PC', xlabel="Rateio", color="red", fontcolor="red", style='bold')
    
    # Fluxo de custos diretos: curvas azuis, grossas e arrowhead diferente
    dot.edge('CD', 'PA', color='blue', penwidth='2', arrowhead='vee', style='solid')
    dot.edge('CD', 'PB', color='blue', penwidth='2', arrowhead='vee', style='solid')
    dot.edge('CD', 'PC', color='blue', penwidth='2', arrowhead='vee', style='solid')
    
    # Produtos para Estoque
    dot.edge('PA', 'E')
    dot.edge('PB', 'E')
    dot.edge('PC', 'E')
    
    # Estoque para CPV
    dot.edge('E', 'CPV')
    
    # CPV para Resultado
    dot.edge('CPV', 'R')
    
    # Despesas para Resultado
    dot.edge('D', 'R')
    
    # Vendas para Resultado
    dot.edge('V', 'R')
    
    # Exibir no Streamlit
    st.graphviz_chart(dot)

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
