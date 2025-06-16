import streamlit as st
import matplotlib.pyplot as plt
from graphviz import Digraph
from utils import leitor_de_texto

def main():
    st.title("📚 Introdução à Contabilidade de Custos")
    
    # Criando abas para o submenu
    tab1, tab2, tab3, tab4 = st.tabs([
        "📌 Conceitos Básicos", 
        "📊 Classificação", 
        "📈 Comportamento", 
        "🧠 Quiz"
    ])
    
    with tab1:  # Conceitos Básicos
        st.header("Terminologia Fundamental")
       
        st.markdown("""
        Imagine que você vai abrir uma hamburgueria, um brechó online ou até um estúdio de criação digital. Antes de pensar no lucro, no preço que você vai cobrar ou no quanto vai ganhar, tem uma pergunta crucial:  
        
        > **“Quanto custa para eu fazer, oferecer ou entregar isso?”**  
        
        E é aí que entra o universo dos **custos**, que são muito mais do que números: são a chave para qualquer negócio ser viável, competitivo e lucrativo.
        """)

        col1 = st.columns(1)[0]
            
        with col1:
            st.markdown(
                """
                <div style="background-color:#FFD54F; padding:20px; border-radius:12px;
                box-shadow: 2px 2px 8px rgba(0,0,0,0.2)">
                    <h4 style="color:#BF360C;">📘 Terminologia:</h4>
                    <ul style="color:#212121;">
                        <li><b>Gastos</b>
                            <ul>
                                <li>Custos</li>
                                <li>Despesas</li>
                                <li>Investimentos</li>
                                <li>Perda</li>
                            </ul>
                        </li>
                        <li>Desembolso</li>
                    </ul>
                </div>
                """,
                unsafe_allow_html=True
            )

        # Função para gerar o diagrama com graphviz
        def generate_financial_diagram():
            dot = Digraph(comment='Diagrama Financeiro', format='png')
            dot.attr(rankdir='LR', nodesep='0.5', ranksep='1.0')  # Orientação de esquerda para direita e espaçamento entre nós
            dot.attr('node', shape='box', fontsize='12')
        
            # Cluster para o Balanço Patrimonial
            with dot.subgraph(name='cluster_balanço') as c:
                c.attr(label='Balanço Patrimonial', style='dashed')
                c.node('balanco_patrimonial', 'Balanço Patrimonial')
                c.node('custos', 'Custos')
                c.node('produtos_servicos', 'Produtos ou Serviços elaborados')
                c.node('investimentos', 'Investimentos')
        
            # Cluster para a Demonstração de Resultado do Período
            with dot.subgraph(name='cluster_resultado') as c:
                c.attr(label='Demonstração de\nResultado do\nPeríodo', style='dashed')
                c.node('demonstracao_resultado', 'Demonstração de\nResultado do\nPeríodo')
                c.node('despesas', 'Despesas')
        
            # Nó independente para Gastos
            dot.node('gastos', 'Gastos')
        
            # Arestas (setas) entre os nós
            dot.edge('balanco_patrimonial', 'custos', label='', arrowhead='vee', arrowsize='1.5')
            dot.edge('custos', 'produtos_servicos', label='', arrowhead='vee', arrowsize='1.5')
            dot.edge('produtos_servicos', 'investimentos', label='', arrowhead='vee', arrowsize='1.5')
            dot.edge('investimentos', 'gastos', label='', arrowhead='vee', arrowsize='1.5')
            dot.edge('demonstracao_resultado', 'despesas', label='', arrowhead='vee', arrowsize='1.5')
            dot.edge('despesas', 'gastos', label='', arrowhead='vee', arrowsize='1.5')
        
            # Notas explicativas
            dot.node('nota_consumo_produto', 'Consumo associado\nà elaboração do\nproduto ou serviço', shape='plaintext', fontsize='10')
            dot.node('nota_consumo_periodo', 'Consumo\nassociado\nao período', shape='plaintext', fontsize='10')
            dot.edge('custos', 'nota_consumo_produto', style='dashed', arrowhead='none')
            dot.edge('despesas', 'nota_consumo_periodo', style='dashed', arrowhead='none')
        
            return dot
        
        # Configurando o Streamlit
        st.title("Diagrama Financeiro")
        
        # Gerando o diagrama
        financial_diagram = generate_financial_diagram()
        
        # Exibindo o diagrama no Streamlit
        st.graphviz_chart(financial_diagram)
        
        # Adicionando uma breve descrição
        st.markdown(
            """
            **Descrição:**
            Este diagrama ilustra o fluxo de custos, despesas e investimentos em um contexto financeiro. 
            - O **Balanço Patrimonial** está relacionado aos custos associados à elaboração de produtos ou serviços.
            - A **Demonstração do Resultado do Período** aborda as despesas consumidas no período.
            - As setas indicam a direção dos fluxos, e as notas explicativas detalham os consumos associados.
            """
        )

        st.markdown("""
        - **Custo:** Gasto relativo à produção de bens/serviços
        - **Despesa:** Gasto com administração/vendas
        - **Investimento:** Gasto ativado (benefício futuro)
        """)
        
        if st.button("Ouvir explicação", key="audio1"):
            texto = "Terminologia: Custo é o gasto relativo à produção, Despesa é o gasto com administração"
            leitor_de_texto(texto)
    
    with tab2:  # Classificação
        st.header("Classificação de Custos")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            **Por Natureza:**
            - Matéria-prima
            - Mão de obra
            - Custos indiretos
            """)
        
        with col2:
            st.markdown("""
            **Por Comportamento:**
            - Fixos (não variam com produção)
            - Variáveis (variam proporcionalmente)
            - Mistos (parte fixa + parte variável)
            """)
        
        st.image("https://i.imgur.com/JQH90yl.png", width=400)
    
    with tab3:  # Comportamento
        st.header("Análise do Comportamento")
        st.markdown("""
        ```math
        Custo\ Total = Custo\ Fixo + (Custo\ Variável\ Unitário × Quantidade)
        ```
        """)
        
        cf = st.slider("Custo Fixo Total (R$):", 1000, 50000, 10000)
        cv = st.slider("Custo Variável Unitário (R$):", 1, 100, 15)
        q = st.slider("Quantidade Produzida:", 0, 1000, 200)
        
        ct = cf + (cv * q)
        st.metric("Custo Total Estimado", f"R$ {ct:,.2f}")
    
    with tab4:  # Quiz
        st.header("Teste Seu Conhecimento")
        
        respostas = st.session_state.get('respostas', {})
        
        # Pergunta 1
        q1 = st.radio(
            "1. O aluguel da fábrica é classificado como:",
            ["Custo Fixo", "Custo Variável", "Despesa Fixa"],
            index=None
        )
        
        # Pergunta 2
        q2 = st.radio(
            "2. Matéria-prima consumida na produção é:",
            ["Custo Direto Variável", "Custo Indireto", "Investimento"],
            index=None
        )
        
        if st.button("Verificar Respostas"):
            respostas['q1'] = q1 == "Custo Fixo"
            respostas['q2'] = q1 == "Custo Direto Variável"
            st.session_state.respostas = respostas
            
            if all(respostas.values()):
                st.success("✅ Parabéns! Todas corretas!")
            else:
                erros = [f"Pergunta {i+1}" for i, v in enumerate(respostas.values()) if not v]
                st.warning(f"Revise: {', '.join(erros)}")

if __name__ == "__main__":
    main()
