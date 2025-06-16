import streamlit as st
import graphviz
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, FancyBboxPatch
from utils import leitor_de_texto

def main():
    st.title("📚 Introdução à Contabilidade de Custos")
    with st.expander("🎯 Objetivos da Unidade", expanded=False):
            st.markdown("""
            - Compreender terminologia básica de custos
            - Classificar custos por natureza e comportamento
            - Analisar o comportamento de custos
            """)    
    
    # Criando abas para o submenu
    tab0, tab1, tab2, tab3, tab4 = st.tabs([
        "💡 Ideação", "📌 Conceitos Básicos", 
        "📊 Classificação", 
        "📈 Comportamento", 
        "🧠 Quiz"
    ])
    
    with tab0:  # Conceitos Básicos    
        st.markdown("""
            # 💥 Qual é o problema?
            
            Imagine que você está no comando.  
            Pode ser de uma indústria. De um e-commerce. De um salão de beleza, uma startup de tecnologia, um restaurante, uma clínica ou até mesmo de uma repartição pública.
            
            Tudo parece andar: clientes chegando, produto sendo entregue, dinheiro entrando...
            
            Mas, de repente, a realidade bate:  
            📉 **O lucro não aparece.**  
            📊 **Os números não fecham.**  
            💸 **Os recursos evaporam.**
            
            E aí vem a pergunta que assombra muitos gestores:  
            **“Estamos vendendo bem… mas por que estamos no vermelho?”**
            
            ---
            
            ## 🎯 A resposta muitas vezes está em uma palavra: **custos**.
            
            Saber seus custos **não é opcional**.  
            É questão de **sobrevivência**.  
            É o que separa negócios sustentáveis daqueles que apagam as luzes antes de completar o segundo ano.
            
            Sem gestão de custos, você:
            
            - ✅ Precifica seus produtos ou serviços **de forma errada**.  
            - ✅ **Investe mal**, alocando recursos onde não há retorno.  
            - ✅ **Desperdiça** dinheiro, tempo e energia.  
            - ✅ **Perde competitividade** e mercado.  
            - ✅ **Pode quebrar** — mesmo com vendas em alta!
            
            ---
            
            ## 🚨 Um alerta baseado em dados:
            
            > Segundo o [BigDataCorp](https://blog.bigdatacorp.com.br/brasil-abriu-mais-de-60-milhoes-de-empresas-aponta-pesquisa/), **quase 80% das empresas brasileiras fecham em até 4 anos**, e um dos principais motivos é a **falta de controle e análise de custos**.
            
            Isso acontece porque muitos confundem **faturamento com lucro**.  
            Outros nem sabem quanto realmente custa **produzir, vender ou entregar seu serviço**.
            
            > 🔍 **Comentário acadêmico:** Pesquisas como a de [Artuzo et al. (2018)](https://doi.org/10.7819/rbgn.v20i2.3192) demonstram que até em setores altamente estruturados, como o agronegócio de milho e soja, a **ausência de práticas adequadas de gestão de custos leva produtores a enfrentar sérios desafios de rentabilidade, competitividade e sustentabilidade.**  
            > O estudo revela que muitos tomam decisões com base na experiência ou na intuição, mas **sem dados precisos sobre seus custos, ficam vulneráveis às oscilações de mercado, ao aumento dos insumos e às pressões por preços.**  
            > Se isso ocorre em negócios com grande escala e tradição, imagine nas empresas de serviços, comércio, startups ou organizações públicas.
            
            ---
            
            ## 🧭 Custo não é só número. É estratégia.
            
            Gerenciar custos é:
            
            - 🔍 Entender **onde e como o dinheiro é consumido**.  
            - 🎯 Decidir com inteligência — **produzir mais? terceirizar? mudar preço? demitir? investir?**  
            - 🏆 Alcançar **lucro com sustentabilidade**.  
            - 📈 Tornar sua organização **mais eficiente, competitiva e resiliente**.
            
            ---
            
            ## 🚀 Pronto para dominar esse tema?
            
            Neste módulo, você vai aprender:
            
            - ✔️ 🔍 Em detalhes, a terminologia completa que envolve a gestão de custos.
            - ✔️ 📋 Classificar os custos por natureza (origem) e comportamento (volume).
            - ✔️ 📈 Analisar como os custos se comportam em diferentes níveis de atividade.
            
            Vamos juntos transformar números em **decisões estratégicas**.
            
            Porque custo **não é um problema de contabilidade**.  
            É uma **ferramenta de gestão inteligente**.

            Vá para o topo dessa página e clique em **📌 Conceitos Básicos** para continuar!
        """)
        
    with tab1:  # Conceitos Básicos    
        st.header("Terminologia")
       
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
            Imagine dirigir uma empresa — seja uma indústria, um comércio, um negócio digital, um restaurante, uma clínica ou até uma repartição pública.  
            **Saber seus custos não é uma opção. É uma questão de sobrevivência.**
            
            Sem isso, você:
            
            - Preço errado seus produtos ou serviços.
            - Desperdiça recursos.
            - Perde competitividade.
            - E, pior, corre risco de quebrar... mesmo vendendo muito.
            
            👉 Vamos começar entendendo, de forma prática e direta, **o que são custos, despesas e investimentos.**
            """)
            
        # ✅ Integração do vídeo
        st.video("https://youtu.be/9GUog7H4Bgk")
        
        st.markdown(""" Precisa ler mais sobre isso? Tem um texto do [Blog Razonet](https://razonet.com.br/blog/post/diferentes-tipos-de-gastos-custo-despesa-investimento-e-perda) que pode ser útil.
            """)
            
        st.divider()
        
        # 🎯 Atividade Interativa 1: Verdadeiro ou Falso
        st.subheader("🎯 Quebre seus mitos sobre custos")
        
        with st.expander("🔍 Clique aqui para testar seus conhecimentos"):
            perguntas = {
                "1️⃣ Custos e despesas são a mesma coisa.": False,
                "2️⃣ Custos estão diretamente ligados à operação do produto ou serviço.": True,
                "3️⃣ Investimentos entram no cálculo de custos mensais.": False,
                "4️⃣ Uma empresa pública não precisa se preocupar com custos.": False
            }
        
            respostas = {}
            for pergunta, correta in perguntas.items():
                respostas[pergunta] = st.radio(pergunta, ["Verdadeiro", "Falso"], index=None, key=pergunta)
        
            if st.button("🔍 Verificar respostas"):
                acertos = 0
                for pergunta, correta in perguntas.items():
                    resposta_usuario = respostas[pergunta] == ("Verdadeiro" if correta else "Falso")
                    if resposta_usuario:
                        acertos += 1
                        st.success(f"✅ {pergunta} ✔️ Correto!")
                    else:
                        st.error(f"❌ {pergunta} ❌ Incorreto.")
        
                st.info(f"🎯 Você acertou {acertos} de {len(perguntas)}.")
        
        st.divider()

        # 📚 Resumo visual
        st.subheader("🗺️ Mapa Mental de Custos")
        st.subheader("🔍 Entendendo os conceitos fundamentais de **Gastos, Custos, Despesas, Investimentos e Perdas**")
    
        st.markdown("""
        > Na gestão de custos, é fundamental compreender como os diferentes tipos de gastos impactam a saúde financeira de qualquer organização — seja ela uma indústria, comércio, serviço ou setor público.
        
        """)
        
        st.divider()
        
        st.subheader("📊 **Mapa Conceitual dos Gastos**")
        
        # Criando o diagrama
        grafico = graphviz.Digraph()
        
        grafico.attr('node', shape='box', style='rounded, filled', fillcolor='#e8f4f8')
        
        grafico.node('G', 'Gastos')
        grafico.node('I', 'Investimentos\n(Gastos que ainda serão usados para gerar receita)')
        grafico.node('C', 'Custo\n(Gastos que são usados diretamente na operação)')
        grafico.node('D', 'Despesa\n(Gastos que foram usados para gerar receita)')
        grafico.node('P', 'Perda\n(Gastos que não geraram receita)')
        
        # Ligações principais
        grafico.edge('G', 'I', label='ainda serão usados')
        grafico.edge('G', 'C', label='uso na operação')
        grafico.edge('C', 'D', label='foram usados para gerar receita')
        grafico.edge('C', 'P', label='não geraram receita')
        
        # Adicionando impacto no resultado
        grafico.node('R', 'Receita e Resultado\n(impacto financeiro)')
        grafico.edge('D', 'R', style='dashed')
        grafico.edge('P', 'R', style='dashed')
        grafico.edge('C', 'R', style='dashed')
        
        st.graphviz_chart(grafico)
        
        st.divider()
        
        # 🏗️ Cenários por setor
        st.subheader("🏢 E na prática? Como isso aparece em diferentes setores?")
        
        setor = st.selectbox(
            "Escolha o setor para explorar:",
            ["Indústria", "Comércio", "Serviços", "Administração Pública"]
        )
        
        if setor == "Indústria":
            st.markdown("""
        - 🏭 **Custos:** Matéria-prima, mão de obra da fábrica, energia da produção, manutenção das máquinas.  
        - 💸 **Despesas:** Marketing, vendas, administrativo, RH, aluguel do escritório.  
        - 💼 **Investimentos:** Compra de máquinas, galpões, tecnologia de produção.  
        """)
        elif setor == "Comércio":
            st.markdown("""
        - 🏪 **Custos:** Compra de mercadorias para revenda, transporte dos produtos, armazenamento.  
        - 💸 **Despesas:** Vendedores, propaganda, aluguel da loja, sistemas de gestão.  
        - 💼 **Investimentos:** Reformas, expansão de lojas, aquisição de equipamentos.  
        """)
        elif setor == "Serviços":
            st.markdown("""
        - 👩‍⚕️ **Custos:** Salário dos profissionais diretamente envolvidos na entrega (médicos, professores, consultores), materiais usados na prestação do serviço.  
        - 💸 **Despesas:** Publicidade, atendimento, suporte, administração, aluguel do escritório.  
        - 💼 **Investimentos:** Softwares, equipamentos especializados, estrutura física.  
        """)
        else:
            st.markdown("""
        - 🏛️ **Custos:** Recursos diretamente aplicados em serviços públicos (salários de médicos de hospitais públicos, professores de escolas públicas, manutenção dos espaços de atendimento).  
        - 💸 **Despesas:** Atividades administrativas, suporte, gestão, auditoria, comunicação.  
        - 💼 **Investimentos:** Obras públicas, compra de veículos, construção de hospitais, sistemas tecnológicos.  
        """)

        if st.button("Ouvir explicação", key="audio1"):
            texto = "Terminologia: Custo é o gasto relativo à produção, Despesa é o gasto com administração"
            leitor_de_texto(texto)

        st.divider()
        
        # 🚀 Desafio Prático
        st.subheader("🚀 Mini Desafio: Classifique corretamente")
        
        with st.expander("🧠 Clique para participar"):
            st.markdown("**Dado o seguinte item, como você classificaria?**")
            item = st.selectbox(
                "Item:",
                ["Compra de um veículo para transporte na empresa",
                 "Conta de energia elétrica da fábrica",
                 "Salário do gerente administrativo",
                 "Compra de mercadorias para revenda",
                 "Desenvolvimento de um novo software interno"]
            )
        
            classificacao = st.radio(
                "Classificação:",
                ["Custo", "Despesa", "Investimento"]
            )
        
            if st.button("✅ Verificar classificação"):
                respostas_certas = {
                    "Compra de um veículo para transporte na empresa": "Investimento",
                    "Conta de energia elétrica da fábrica": "Custo",
                    "Salário do gerente administrativo": "Despesa",
                    "Compra de mercadorias para revenda": "Custo",
                    "Desenvolvimento de um novo software interno": "Investimento"
                }
        
                correta = respostas_certas[item]
                if classificacao == correta:
                    st.success(f"🎉 Correto! {item} é classificado como **{correta}**.")
                else:
                    st.error(f"❌ Ops! {item} é na verdade **{correta}**.")
        
        st.divider()
        
        st.subheader("🚀 **Desafio Rápido!**")
        
        pergunta = st.radio(
            "📌 Imagine que sua empresa comprou um notebook para ser usado pela equipe de vendas. Isso é:",
            ("Investimento", "Custo", "Despesa", "Perda"),
                index=None
        )
        
        if pergunta:
            if pergunta == "Investimento":
                st.success("✅ Correto! Inicialmente é um investimento, pois o bem ainda não foi consumido.")
            else:
                st.error("❌ Não é bem isso. Quando compramos um notebook, ele ainda não foi usado, portanto é um investimento.")
        
        st.markdown("---")
        
        st.subheader("🧠 **Quer testar mais seu conhecimento?**")
        
        if st.button("Clique para mais desafios"):
            st.info("👉 Em breve você poderá acessar quizzes mais completos nesta plataforma!")
        st.markdown(" ")
        
        st.markdown("Vá para o topo dessa página e clique em **📊 Classificação** para continuar!")
        
    with tab2:  # Classificação
        st.header("Classificação de Custos")
        
        st.markdown(
        """
        <div style="background-color:#4FC3F7; padding:20px; border-radius:12px;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.2)">
            <h4 style="color:#01579B;">📗 O que vamos diferenciar?</h4>
            <ul style="color:#212121;">
                <li>Natureza: Diretos vs. Indiretos</li>
                <li>Volume: Fixos vs. Variáveis</li>
                <li>Aplicação: Custos vs. Despesas</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
        )

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
