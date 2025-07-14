import streamlit as st
import pandas as pd
import plotly.express as px
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
    dot.attr(rankdir='LR', splines='curved')
    
    node_attr = {'shape': 'box', 'style': 'rounded,filled', 'color': 'cyan', 'fontname': 'Arial', 'fontsize': '6'}

    # Criar cluster para 1o passo
    with dot.subgraph(name='cluster_1') as c:
        c.attr(label='1o. passo', fontsize='20', fontname='Arial', labelloc='t', style='dashed')
        # Nós alinhados verticalmente (rank=same para alinhamento horizontal, mas aqui, com rankdir=LR, 'same' alinha vertical)
        c.attr(rank='same')
    
        c.node('C', 'Custos', **node_attr)
        c.node('x', label='vs', shape='none')
        c.node('D', 'Despesas', **node_attr)

    # Nós principais
    #dot.node('C', 'Custos', **node_attr)
    #dot.node('D', 'Despesas', **node_attr)
    dot.node('V', 'Vendas', **node_attr)
    dot.node('R', 'Resultado', **node_attr)
    
    # Nós CD e CI
    dot.node('CI', 'Indiretos', **node_attr)
    dot.node('CD', 'Diretos', **node_attr)
    
    # Conexões C -> CD e CI (sem minlen para não alongar aqui)
    dot.edge('C', 'CI')
    dot.edge('C', 'CD')
    
    # Produtos
    dot.node('PA', 'Produto A', **node_attr)
    dot.node('PB', 'Produto B', **node_attr)
    dot.node('PC', 'Produto C', **node_attr)
    
    # Estoque e CPV
    dot.node('E', 'Estoque', **node_attr)
    dot.node('CPV', 'Custo dos\nProdutos\nVendidos', **node_attr)
    
    # Edges que saem de CD — também com minlen maior para alongar
    dot.edge('CD', 'PA', color='blue', penwidth='2', arrowhead='vee', style='solid', minlen='3')
    dot.edge('CD', 'PB', color='blue', penwidth='2', arrowhead='vee', style='solid', minlen='3')
    dot.edge('CD', 'PC', color='blue', penwidth='2', arrowhead='vee', style='solid', minlen='3')
    
    # Edges que saem de CI — com minlen maior para alongar só essas arestas
    dot.edge('CI', 'PA', xlabel="Rateio", color="red", fontcolor="red", style='bold', minlen='3')
    dot.edge('CI', 'PB', xlabel="Rateio", color="red", fontcolor="red", style='bold', minlen='3')
    dot.edge('CI', 'PC', xlabel="Rateio", color="red", fontcolor="red", style='bold', minlen='3')
    
    # Produtos para Estoque
    dot.edge('PA', 'E')
    dot.edge('PB', 'E')
    dot.edge('PC', 'E')
    
    # Estoque para CPV
    dot.edge('E', 'CPV')
    
    # CPV para Resultado
    dot.edge('CPV', 'R')
    
    # Despesas para Resultado
    dot.edge('D', 'R', minlen='2')
    
    # Vendas para Resultado
    dot.edge('V', 'R')
    
    # Exibir no Streamlit
    st.graphviz_chart(dot)

    # Simulador interativo
    st.subheader("📱 Simulador de Custeio")

    with st.expander("🔧 Simulador Interativo de Custeio por Absorção", expanded=False):
        # Container principal
        with st.container():
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("**Matéria-Prima**")
                eimp = st.number_input("Estoque Inicial MP (R$):", min_value=0, value=2000, step=100)
                compras_mp = st.number_input("Compras MP (R$):", min_value=0, value=8000, step=100)
                efmp = st.number_input("Estoque Final MP (R$):", min_value=0, value=1000, step=100)
                mp = eimp + compras_mp - efmp
                st.metric("Matéria-Prima Calculada", f"R$ {mp:,.2f}", 
                         delta=f"EIMP + Compras - EFMP = {eimp} + {compras_mp} - {efmp}")
                
            with col2:
                st.markdown("**Custos de Produção**")
                mod = st.number_input("Mão de Obra Direta (R$):", min_value=0, value=5000, step=100)
                cif = st.number_input("Custos Indiretos (R$):", min_value=0, value=3000, step=100)
                eipp = st.number_input("Estoque Inicial PP (R$):", min_value=0, value=1500, step=100)
                efpp = st.number_input("Estoque Final PP (R$):", min_value=0, value=1000, step=100)
                
            with col3:
                st.markdown("**Produtos Acabados**")
                eipa = st.number_input("Estoque Inicial PA (R$):", min_value=0, value=2000, step=100)
                efpa = st.number_input("Estoque Final PA (R$):", min_value=0, value=1500, step=100)
                unidades_vendidas = st.number_input("Unidades Vendidas:", min_value=0, value=800, step=10)
        
        # Cálculos
        if st.button("🔢 Calcular", type="primary"):
            cpp = mp + mod + cif
            cpa = cpp + eipp - efpp
            cpv = cpa + eipa - efpa
            custo_unitario = cpv / unidades_vendidas if unidades_vendidas > 0 else 0
            
            resultados = pd.DataFrame({
                "Indicador": ["CPP (Custo de Produção do Período)", 
                             "CPA (Custo de Produção Acumulado)", 
                             "CPV (Custo dos Produtos Vendidos)",
                             "Custo Unitário"],
                "Valor (R$)": [cpp, cpa, cpv, custo_unitario],
                "Fórmula": [
                    "MP + MOD + CIF",
                    "CPP + EIPP - EFPP",
                    "CPA + EIPA - EFPA",
                    "CPV / Unidades Vendidas"
                ],
                "Cálculo": [
                    f"{mp} + {mod} + {cif}",
                    f"{cpp} + {eipp} - {efpp}",
                    f"{cpa} + {eipa} - {efpa}",
                    f"{cpv} / {unidades_vendidas}" if unidades_vendidas > 0 else "N/A"
                ]
            })
            
            # Exibição dos resultados
            st.success("🎯 Resultados do Custeio por Absorção")
            
            col_res1, col_res2, col_res3 = st.columns(3)
            with col_res1:
                st.metric("CPP", f"R$ {cpp:,.2f}")
            with col_res2:
                st.metric("CPA", f"R$ {cpa:,.2f}")
            with col_res3:
                st.metric("CPV", f"R$ {cpv:,.2f}")
            
            st.dataframe(resultados.style.format({"Valor (R$)": "R$ {:,.2f}"}), hide_index=True)
            
            # Gráfico
            fig = px.bar(resultados.iloc[:3], 
                         x="Indicador", 
                         y="Valor (R$)",
                         title="Indicadores de Custeio",
                         text_auto='.2f',
                         color="Indicador")
            st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # Exemplos setoriais
    st.subheader("📌 Exemplos Práticos por Setor")
    st.write("Explore como o custeio por absorção é aplicado em diferentes setores:")
    
    with st.expander("🔧 Simulador Interativo de Custeio por Absorção", expanded=True):

        exemplos = [
            {
                "setor": "🏭 Indústria (Fábrica de Móveis)",
                "dados": {
                    "EIMP": 5000,
                    "Compras_MP": 20000,
                    "EFMP": 3000,
                    "MOD": 15000,
                    "CIF": 8000,
                    "EIPP": 4000,
                    "EFPP": 2000,
                    "EIPA": 6000,
                    "EFPA": 3000,
                    "Unidades_Vendidas": 500
                },
                "descricao": "Cálculo completo para indústria com todos os estoques: Matéria-Prima, Produtos em Processo e Acabados."
            },
            {
                "setor": "🛒 Comércio (Distribuidora)",
                "dados": {
                    "EIMP": 0,
                    "Compras_MP": 0,
                    "EFMP": 0,
                    "MOD": 8000,
                    "CIF": 5000,
                    "EIPP": 0,
                    "EFPP": 0,
                    "EIPA": 15000,
                    "EFPA": 8000,
                    "Unidades_Vendidas": 1
                },
                "descricao": "Adaptação para comércio (sem produção, apenas estoque de produtos acabados)."
            },
            {
                "setor": "👨‍⚕️ Serviços (Clínica Médica)",
                "dados": {
                    "EIMP": 1000,
                    "Compras_MP": 2000,
                    "EFMP": 500,
                    "MOD": 25000,
                    "CIF": 12000,
                    "EIPP": 0,
                    "EFPP": 0,
                    "EIPA": 0,
                    "EFPA": 0,
                    "Unidades_Vendidas": 600
                },
                "descricao": "Serviços com pequeno estoque de materiais (sem produtos em processo ou acabados)."
            }
        ]
    
        tabs = st.tabs([exemplo["setor"] for exemplo in exemplos])
        
        for i, tab in enumerate(tabs):
            with tab:
                exemplo = exemplos[i]
                dados = exemplo['dados']
                
                # Cálculos completos
                mp = dados['EIMP'] + dados['Compras_MP'] - dados['EFMP']
                cpp = mp + dados['MOD'] + dados['CIF']
                cpa = cpp + dados['EIPP'] - dados['EFPP']
                cpv = cpa + dados['EIPA'] - dados['EFPA']
                custo_unit = cpv / dados['Unidades_Vendidas'] if dados['Unidades_Vendidas'] > 0 else 0
                
                col1, col2 = st.columns(2)
                with col1:
                    st.markdown("**Dados de Entrada:**")
                    st.json({
                        "Matéria-Prima": {
                            "EIMP": dados['EIMP'],
                            "Compras MP": dados['Compras_MP'],
                            "EFMP": dados['EFMP']
                        },
                        "Produção": {
                            "MOD": dados['MOD'],
                            "CIF": dados['CIF'],
                            "EIPP": dados['EIPP'],
                            "EFPP": dados['EFPP']
                        },
                        "Produtos Acabados": {
                            "EIPA": dados['EIPA'],
                            "EFPA": dados['EFPA']
                        },
                        "Unidades Vendidas": dados['Unidades_Vendidas']
                    })
                
                with col2:
                    st.markdown("**Cálculos Detalhados:**")
                    
                    st.markdown(f"""
                    **1. Matéria-Prima (MP)**  
                    `MP = EIMP + Compras - EFMP`  
                    `= {dados['EIMP']} + {dados['Compras_MP']} - {dados['EFMP']} = **{mp:,.2f}**`
                    
                    **2. Custo Produção Período (CPP)**  
                    `CPP = MP + MOD + CIF`  
                    `= {mp:,.2f} + {dados['MOD']} + {dados['CIF']} = **{cpp:,.2f}**`
                    
                    **3. Custo Produto Acabado (CPA)**  
                    `CPA = CPP + EIPP - EFPP`  
                    `= {cpp:,.2f} + {dados['EIPP']} - {dados['EFPP']} = **{cpa:,.2f}**`
                    
                    **4. Custo Produtos Vendidos (CPV)**  
                    `CPV = CPA + EIPA - EFPA`  
                    `= {cpa:,.2f} + {dados['EIPA']} - {dados['EFPA']} = **{cpv:,.2f}**`
                    
                    **5. Custo Unitário**  
                    `= CPV / Unidades = {cpv:,.2f} / {dados['Unidades_Vendidas']} = **{custo_unit:,.2f}**`
                    """)
                
                # Gráfico de estoques
                estoques = pd.DataFrame({
                    "Tipo": ["Matéria-Prima", "Prod. Processo", "Prod. Acabados"],
                    "Estoque Inicial": [dados['EIMP'], dados['EIPP'], dados['EIPA']],
                    "Estoque Final": [dados['EFMP'], dados['EFPP'], dados['EFPA']]
                })
                
                fig = px.bar(estoques, 
                            x="Tipo", 
                            y=["Estoque Inicial", "Estoque Final"],
                            title="Movimentação de Estoques",
                            barmode='group',
                            labels={"value": "Valor (R$)", "variable": "Tipo de Estoque"})
                st.plotly_chart(fig, use_container_width=True)
    
    st.divider()    
    if st.button("👉 Avançar para o próximo tópico: Conhecer o Método de Custeio Variável"):
        st.switch_page("pages/4_📈_Custeio_Variavel.py")


if __name__ == "__main__":
    main()
