import streamlit as st
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

        # Criação do diagrama
        dot = Digraph(comment='Balanço Patrimonial', format='png')
        dot.attr(rankdir='TB', size='8,5')
        
        # Configurações gerais
        dot.attr('node', shape='box', style='filled', fillcolor='lightgrey', fontname='Helvetica')
        dot.attr('edge', fontname='Helvetica')
        
        # Nó principal
        dot.node('BP', 'Balanço Patrimonial', shape='ellipse', fillcolor='lightblue')
        
        # Nós de nível 1
        dot.node('Custos', 'Custos')
        dot.node('Invest', 'Investimentos')
        dot.node('Gastos', 'Gastos')
        
        # Conexões do nível 1
        dot.edge('BP', 'Custos')
        dot.edge('BP', 'Invest')
        dot.edge('BP', 'Gastos')
        
        # Nós de nível 2 - Custos
        dot.node('Consumo', 'Consumo associado à elaboração\ndo produto ou serviço')
        dot.node('Produtos', 'Produtos ou Serviços\nelaborados')
        
        # Conexões Custos
        dot.edge('Custos', 'Consumo')
        dot.edge('Custos', 'Produtos')
        
        # Nós de nível 2 - Investimentos
        dot.node('Inventivos', 'Inventivos')
        dot.node('Concurso', 'Concurso associado ao período')
        
        # Conexões Investimentos
        dot.edge('Invest', 'Inventivos')
        dot.edge('Invest', 'Concurso')
        
        # Renderizar o gráfico
        dot.render('balanco_patrimonial', view=True)
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
