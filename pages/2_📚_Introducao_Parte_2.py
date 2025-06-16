import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Ellipse
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

        plt.figure(figsize=(10, 8))
        ax = plt.gca()
        
        # Elementos principais
        ax.add_patch(Ellipse((0.5, 0.9), 0.3, 0.1, fill=True, color='lightblue'))
        plt.text(0.5, 0.9, 'Balanço Patrimonial', ha='center', va='center')
        
        # Linhas principais
        plt.plot([0.5, 0.3], [0.85, 0.7], 'k-')  # Esquerda
        plt.plot([0.5, 0.5], [0.85, 0.7], 'k-')  # Centro
        plt.plot([0.5, 0.7], [0.85, 0.7], 'k-')  # Direita
        
        # Caixas de nível 1
        ax.add_patch(Rectangle((0.2, 0.6), 0.2, 0.1, fill=True, color='lightgrey'))
        plt.text(0.3, 0.65, 'Custos', ha='center', va='center')
        
        ax.add_patch(Rectangle((0.4, 0.6), 0.2, 0.1, fill=True, color='lightgrey'))
        plt.text(0.5, 0.65, 'Investimentos', ha='center', va='center')
        
        ax.add_patch(Rectangle((0.6, 0.6), 0.2, 0.1, fill=True, color='lightgrey'))
        plt.text(0.7, 0.65, 'Gastos', ha='center', va='center')
        
        # Linhas para nível 2
        plt.plot([0.3, 0.2], [0.6, 0.45], 'k-')
        plt.plot([0.3, 0.3], [0.6, 0.45], 'k-')
        plt.plot([0.5, 0.4], [0.6, 0.45], 'k-')
        plt.plot([0.5, 0.6], [0.6, 0.45], 'k-')
        
        # Caixas de nível 2
        ax.add_patch(Rectangle((0.1, 0.35), 0.2, 0.1, fill=True, color='lightgrey'))
        plt.text(0.2, 0.4, 'Consumo associado\nao produto/serviço', ha='center', va='center', fontsize=8)
        
        ax.add_patch(Rectangle((0.25, 0.35), 0.2, 0.1, fill=True, color='lightgrey'))
        plt.text(0.35, 0.4, 'Produtos ou\nServiços elaborados', ha='center', va='center', fontsize=8)
        
        ax.add_patch(Rectangle((0.35, 0.35), 0.2, 0.1, fill=True, color='lightgrey'))
        plt.text(0.45, 0.4, 'Inventivos', ha='center', va='center', fontsize=8)
        
        ax.add_patch(Rectangle((0.55, 0.35), 0.2, 0.1, fill=True, color='lightgrey'))
        plt.text(0.65, 0.4, 'Concurso associado\nao período', ha='center', va='center', fontsize=8)
        
        plt.axis('off')
        plt.tight_layout()
        plt.show()
        
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
