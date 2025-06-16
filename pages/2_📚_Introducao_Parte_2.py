import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
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
        with st.expander("📌 Objetivos da Unidade", expanded=True):
        st.markdown("""
        - Compreender terminologia básica de custos
        - Classificar custos por natureza e comportamento
        - Analisar o comportamento de custos
        """)

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

        plt.figure(figsize=(12, 10))
        ax = plt.gca()
        ax.axis('off')  # Desligar eixos
        
        # Título principal
        plt.text(0.5, 0.95, 'Classificações dos Desembolsos', 
                 ha='center', va='center', fontsize=16, weight='bold')
        
        # Cores para categorias
        colors = ['#FFD54F', '#4FC3F7', '#AED581', '#7986CB', '#F06292']
        
        # Categorias principais (agrupando os itens fornecidos)
        categorias = {
            'Deduções': ['Impostos', 'Fretes', 'Devoluções'],
            'Custos': {
                'Diretos': ['Matéria-prima', 'Insumos'],
                'Indiretos': ['Energia elétrica', 'Manutenção']
            },
            'Despesas': ['Administrativas', 'Comerciais', 'Financeiras'],
            'Investimentos': ['Ativos Financeiros', 'Ativos Operacionais'],
            'Outros': ['Institutos', 'Disposições']
        }
        
        # Posicionamento das categorias
        positions = [(0.2, 0.7), (0.5, 0.7), (0.8, 0.7), (0.35, 0.4), (0.65, 0.4)]
        
        for (x, y), (cat_name, items), color in zip(positions, categorias.items(), colors):
            # Caixa principal da categoria
            main_box = FancyBboxPatch((x-0.15, y-0.05), 0.3, 0.1, 
                                     boxstyle="round,pad=0.03", 
                                     fc=color, ec='black', alpha=0.8)
            ax.add_patch(main_box)
            plt.text(x, y, cat_name, ha='center', va='center', fontsize=12, weight='bold')
            
            # Subitens
            if isinstance(items, dict):  # Para Custos que tem subcategorias
                for i, (subcat, subitems) in enumerate(items.items()):
                    # Linha de conexão
                    plt.plot([x, x-0.1+i*0.1], [y-0.05, y-0.15], 'k-', lw=0.5)
                    
                    # Caixa da subcategoria
                    sub_box = FancyBboxPatch((x-0.12+i*0.1, y-0.2), 0.15, 0.08,
                                           boxstyle="round,pad=0.02",
                                           fc=color, ec='black', alpha=0.6)
                    ax.add_patch(sub_box)
                    plt.text(x-0.05+i*0.1, y-0.16, subcat, ha='center', va='center', fontsize=9)
                    
                    # Itens da subcategoria
                    for j, item in enumerate(subitems):
                        plt.text(x-0.05+i*0.1, y-0.25-j*0.05, item, 
                                ha='center', va='center', fontsize=8)
            else:
                # Para categorias sem subníveis
                for i, item in enumerate(items):
                    plt.plot([x, x], [y-0.05, y-0.15-i*0.05], 'k-', lw=0.5)
                    plt.text(x, y-0.2-i*0.05, item, ha='center', va='center', fontsize=9)
        
        # Adicionar legenda explicativa
        legenda = """Legenda:
        • Deduções: Gastos para realizar a venda
        • Custos: Gastos na produção de bens/serviços
        • Despesas: Gastos com manutenção da empresa
        • Investimentos: Expectativa de benefícios futuros"""
        plt.text(0.05, 0.1, legenda, ha='left', va='top', fontsize=9, 
                 bbox=dict(facecolor='white', alpha=0.8, edgecolor='gray'))
        
        plt.tight_layout()
        plt.savefig('classificacao_desembolsos.png', dpi=300, bbox_inches='tight')
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
