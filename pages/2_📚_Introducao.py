import streamlit as st
import numpy as np
import pandas as pd
import graphviz
import matplotlib.pyplot as plt
import plotly.express as px
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
        "🧠 Quiz (em breve)"
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

        Entretanto, nem tudo que se gasta é chamado de custo. Assim, vamos conhecer os termos corretos.
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
                        <li><b>Desembolso* </b></li>
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
        #plt.savefig('classificacao_desembolsos.png', dpi=300, bbox_inches='tight')
        plt.show()

        st.divider()

        st.markdown("""
            *De acordo como Alves et al. (2018) "O gasto resulta em “desembolso”, no entanto, vale destacar que ambos possuem conceitos distintos, ou seja, nem todo o desembolso é um gasto."
        
            Imagine dirigir uma empresa — seja uma indústria, um comércio, um negócio digital, um restaurante, uma clínica ou até uma repartição pública.  
            **Saber seus custos não é uma opção. É uma questão de sobrevivência.**
            
            Sem isso, você:
            
            - Preço errado seus produtos ou serviços.
            - Desperdiça recursos.
            - Perde competitividade.
            - E, pior, corre risco de quebrar... mesmo vendendo muito.
            
            👉 Vamos começar entendendo, de forma prática e direta, **o que são custos, despesas e investimentos.**

            Ah! Só pra constar... Alves et al. (2018) é um livro e sua referência completa é: ALVES, Aline et al. **Análise de custo**. Porto Alegre: SAGAH, 2018.
        
            """)
            
        # ✅ Integração do vídeo
        st.video("https://youtu.be/9GUog7H4Bgk")
        
        st.markdown("""             
            Mais detalhes você pode ver [outro vídeo que mostra a diferença entre esses termos. **Clique aqui para acessar**](https://youtu.be/wvAMk9qGhoE?si=JzH89zq0ND1ij3Wt)

            Precisa ler mais sobre isso? Tem um texto do [Blog Razonet](https://razonet.com.br/blog/post/diferentes-tipos-de-gastos-custo-despesa-investimento-e-perda) que pode ser útil.
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
        st.subheader("🔍 Entendendo os conceitos fundamentais de **Gastos (Custos, Despesas, Investimentos e Perdas)**")
    
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
        grafico.node('D', 'Despesa\n(Gastos não associados a atividade fim)')
        grafico.node('P', 'Perda\n(Gastos inesperados ou extraordinários.)')
        
        # Ligações principais
        grafico.edge('G', 'I', label='ainda serão usados')
        grafico.edge('G', 'C', label='uso na operação')
        grafico.edge('G', 'D', label='foram usados para gerar receita')
        grafico.edge('G', 'P', label='não geraram receita')
        
        # Adicionando impacto no resultado
        grafico.node('B', 'Balanço Patrimonial\n(Bens, direitos e obrigações)')
        grafico.edge('I', 'B', style='dashed')
        grafico.edge('C', 'B', style='dashed')
        
        # Adicionando impacto no resultado
        grafico.node('R', 'Dem. Resultado do Exdercício\n(impacto financeiro)')
        grafico.edge('D', 'R', style='dashed')
        grafico.edge('P', 'R', style='dashed')
        
        st.graphviz_chart(grafico)
        
        st.divider()
        
        # 🏗️ Cenários por setor
        st.subheader("🏢 E na prática? Como isso aparece em diferentes setores?")
        
        setor = st.selectbox(
            "Escolha o setor para explorar:",
            ["Indústria", "Comércio", "Serviços", "Administração Pública"], index=None
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
        elif setor == "Administração Pública":
            st.markdown("""
        - 🏛️ **Custos:** Recursos diretamente aplicados em serviços públicos (salários de médicos de hospitais públicos, professores de escolas públicas, manutenção dos espaços de atendimento).  
        - 💸 **Despesas:** Atividades administrativas, suporte, gestão, auditoria, comunicação.  
        - 💼 **Investimentos:** Obras públicas, compra de veículos, construção de hospitais, sistemas tecnológicos.  
        """)
        else:
            st.markdown("""
            """)

        if st.button("Ouvir explicação", key="audio1"):
            texto = "Terminologia: Custo é o gasto relativo à produção, Despesa é o gasto com administração"
            leitor_de_texto(texto)

        st.divider()
        
        # 🚀 Desafio Prático
        st.subheader("🚀 Mini Desafio: Identifique corretamente")
        
        with st.expander("🧠 Clique para participar"):
            st.markdown("**Dado o seguinte item, como você denominaria?**")
            item = st.selectbox(
                "Item:",
                ["Compra de um veículo para transporte na empresa",
                 "Conta de energia elétrica da fábrica",
                 "Salário do gerente administrativo",
                 "Compra de mercadorias para revenda",
                 "Desenvolvimento de um novo software interno"], index=None
            )
        
            classificacao = st.radio(
                "Denominação:",
                ["Custo", "Despesa", "Investimento"], index=None
            )
        
            if st.button("✅ Verificar a denominação"):
                respostas_certas = {
                    "Compra de um veículo para transporte na empresa": "Investimento",
                    "Conta de energia elétrica da fábrica": "Custo",
                    "Salário do gerente administrativo": "Despesa",
                    "Compra de mercadorias para revenda": "Custo",
                    "Desenvolvimento de um novo software interno": "Investimento"
                }
        
                correta = respostas_certas[item]
                if classificacao == correta:
                    st.success(f"🎉 Correto! {item} é denominado como **{correta}**.")
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
            - Custos Diretos
            - Custos indiretos
            """)
        
        with col2:
            st.markdown("""
            **Por Comportamento:**
            - Fixos (não variam com produção)
            - Variáveis (variam proporcionalmente)
            - Mistos (parte fixa + parte variável)
            """)

        # Introdução interativa
        with st.expander("🔍 Por que classificar custos?", expanded=True):
            st.markdown("""
            **A classificação adequada dos custos permite:**
            - Tomada de decisão mais precisa
            - Cálculo correto do custo dos produtos
            - Identificação de oportunidades de redução
            - Melhor planejamento orçamentário
            """)
            st.image("https://cdn-icons-png.flaticon.com/512/3144/3144456.png", width=100)
        
        # Abas para diferentes classificações
        tb1, tb2 = st.tabs(["🔷 Natureza (Direto/Indireto)", "📊 Comportamento (Fixo/Variável)"])
        
        with tb1:
            st.subheader("Diretos vs. Indiretos")
            col1, _, col2 = st.columns([1.5, 0.5, 1.5])
            
            with col1:
                st.markdown("""
                **Custos Diretos:**
                - Identificáveis diretamente no produto
                - Exemplos:
                  - Matéria-prima específica
                  - Embalagem do produto
                  - Mão de obra dedicada
                """)
                
            with col2:
                st.markdown("""
                **Custos Indiretos:**
                - Não podem ser atribuídos diretamente
                - Exemplos:
                  - Energia da fábrica
                  - Aluguel do prédio
                  - Limpeza geral
                """)
             
                
            # Dados personalizados por produto
            dados_produtos = {
                "Smartphone": {
                    "Direto": {
                        "Tela LCD": 120,
                        "Processador": 85,
                        "Câmera": 60,
                        "Bateria": 45
                    },
                    "Indireto": {
                        "Energia": 30,
                        "Depreciação": 15,
                        "Logística": 25,
                        "Embalagem": 10
                    }
                },
                "Notebook": {
                    "Direto": {
                        "Tela LED": 200,
                        "CPU": 150,
                        "GPU": 120,
                        "Memória RAM": 80
                    },
                    "Indireto": {
                        "Manutenção": 40,
                        "Transporte": 35,
                        "Impostos": 50,
                        "Seguro": 20
                    }
                },
                "Tablet": {
                    "Direto": {
                        "Tela Touch": 90,
                        "Chipset": 70,
                        "Alto-falante": 30,
                        "Conectividade": 25
                    },
                    "Indireto": {
                        "Pesquisa": 20,
                        "Marketing": 35,
                        "Armazenamento": 15,
                        "Suporte": 10
                    }
                }
            }
            
            # Interface no Streamlit
            st.title("Vejamos um exemplo prático")
            
            colx1, colx2 = st.columns([1, 3])
            
            with colx1:
                produto_selecionadox = st.selectbox(
                    "Selecione um produto para análise:",
                    list(dados_produtos.keys()),
                    key="produto_selectx"
                )
            
            with colx2:
                # Prepara os dados para o DataFrame
                dados_formatados = []
                for tipo, itens in dados_produtos[produto_selecionadox].items():
                    for item, valor in itens.items():
                        dados_formatados.append({
                            "Tipo": tipo,
                            "Item": item,
                            "Valor": valor,
                            "Produto": produto_selecionadox
                        })
                
                df = pd.DataFrame(dados_formatados)
                
                # Cria o gráfico Sunburst
                fig = px.sunburst(
                    df,
                    path=['Tipo', 'Item'],
                    values='Valor',
                    color='Tipo',
                    color_discrete_map={'Direto': '#4CAF50', 'Indireto': '#FF9800'},
                    title=f"Composição de Custos - {produto_selecionadox}",
                    branchvalues='total'
                )
                
                # Ajustes de layout
                fig.update_layout(margin=dict(t=50, l=0, r=0, b=0))
                fig.update_traces(textinfo="label+percent parent", 
                                  hovertemplate='<b>Custo %{parent}</b><br><b>%{label}</b><br>Valor: R$ %{value:.2f}<extra></extra>')
                
                st.plotly_chart(fig, use_container_width=True)
                st.caption("🔎 Clique no gráfico para explorar a composição detalhada")
                
        with tb2:
            st.subheader("Fixos vs. Variáveis")
            
            # Simulador interativo
            st.markdown("#### 📈 Simulador de Comportamento de Custos")
            
            col_fv1, col_fv2 = st.columns(2)
            with col_fv1:
                custo_fixo = st.slider("Custo Fixo Mensal (R$)", 1000, 50000, 15000)
                custo_variavel_unit = st.slider("Custo Variável Unitário (R$)", 5, 200, 50)
            
            with col_fv2:
                producao_min = st.slider("Produção Mínima (un)", 0, 500, 0)
                producao_max = st.slider("Produção Máxima (un)", 500, 5000, 2000)
            
            # Gerar dados para o gráfico
            qtd_producao = list(range(producao_min, producao_max+1, 50))
            custo_total = [custo_fixo + custo_variavel_unit*q for q in qtd_producao]
            
            df = pd.DataFrame({
                "Quantidade": qtd_producao,
                "Custo Total": custo_total,
                "Custo Fixo": custo_fixo,
                "Custo Variável": [custo_variavel_unit*q for q in qtd_producao]
            })
            
            fig = px.line(
                df,
                x="Quantidade",
                y=["Custo Total", "Custo Fixo", "Custo Variável"],
                labels={"value": "Custo (R$)", "variable": "Tipo de Custo"},
                title="Comportamento dos Custos em Relação ao Volume de Produção"
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Exemplos práticos
            st.markdown("""
            **Exemplos Reais:**
            - 🏭 **Custo Fixo Típico:** Aluguel da fábrica, salários administrativos
            - 🚚 **Custo Variável Típico:** Matéria-prima, frete por unidade vendida
            - 💡 **Custo Misto:** Energia (parte fixa + parte variável pelo uso)
            """)
     
    with tab3:  # Comportamento
        st.title("⚖️ Diferença entre Custos e Despesas")
        st.subheader("🔍 Como os custos e as despesas impactam o resultado da empresa?")
        
        st.markdown("""
        > Entender a diferença entre **custos** e **despesas** é essencial para uma boa gestão financeira. Cada um tem um papel específico na formação do resultado da empresa.
        
        """)
        
        st.divider()
        
        st.subheader("📊 **Relação dos Processos com Custos e Despesas**")
        
        # Criando o diagrama
        grafico = graphviz.Digraph()
        
        grafico.attr('node', shape='box', style='rounded, filled', fillcolor='#f0f9f9')
        
        # Processos
        grafico.node('Prod', '🔧 Processo Produtivo')
        grafico.node('RH', '👥 Recursos Humanos')
        grafico.node('Mkt', '📢 Marketing')
        grafico.node('Fin', '💰 Finanças')
        grafico.node('Adm', '📑 Administrativo')
        grafico.node('Outros', '➕ Outros')
        
        # Receita e resultado
        grafico.node('Rec', '💵 Receita\n(-) Custo das Mercadorias Vendidas\n= Lucro Bruto\n(-) Despesas Operacionais\n= Lucro Operacional', shape='rectangle', fillcolor='#d0eafc')
        
        # Conexões
        grafico.edge('Prod', 'Rec', label='➡️ Custo')
        grafico.edge('RH', 'Rec', label='➡️ Despesa')
        grafico.edge('Mkt', 'Rec', label='➡️ Despesa')
        grafico.edge('Fin', 'Rec', label='➡️ Despesa')
        grafico.edge('Adm', 'Rec', label='➡️ Despesa')
        grafico.edge('Outros', 'Rec', label='➡️ Despesa')
        
        st.graphviz_chart(grafico)
        
        st.divider()
        
        st.subheader("💡 **Conceituando:**")
        
        st.markdown("""
        ### ✔️ **Custos**
        - São todos os gastos diretamente relacionados com o processo produtivo ou com a entrega do serviço.
        - Quando mais a produção ou venda cresce, mais os custos tendem a aumentar proporcionalmente.
        - ➕ **Exemplos:** matéria-prima, salários da produção, depreciação de máquinas, compra de mercadorias para revenda.
        
        ### ✔️ **Despesas**
        - São gastos necessários para manter a estrutura administrativa, comercial e de apoio, mas **não estão diretamente ligados à produção**.
        - ➕ **Exemplos:** salários da administração, despesas de marketing, aluguel da sede, energia da área administrativa, honorários da contabilidade.
        """)
    
        st.divider()
        
        st.subheader("🧠 **Impacto na Demonstração do Resultado:**")
        
        st.markdown("""
        - 🏭 **Custos** afetam o **Lucro Bruto**:
          > Receita - **Custo das Mercadorias Vendidas** = **Lucro Bruto**
        
        - 🏢 **Despesas** afetam o **Lucro Operacional**:
          > Lucro Bruto - **Despesas Operacionais** = **Lucro Operacional**
        """)
        
        st.divider()
        
        st.subheader("🚀 **Desafio Interativo!**")
        
        pergunta = st.radio(
            "Imagine que uma empresa contratou uma agência de marketing para fazer campanhas nas redes sociais. Esse gasto é:",
            ("Custo", "Despesa"), index=None
        )
        
        if pergunta:
            if pergunta == "Despesa":
                st.success("✅ Correto! Marketing é uma despesa, pois não está diretamente ligado à produção.")
            else:
                st.error("❌ Não é isso. Marketing não é custo, pois não faz parte diretamente do processo produtivo.")
        
        st.markdown("---")
        
        st.subheader("🎯 **Mais Desafios?**")
        
        if st.button("Quero mais perguntas!"):
            st.info("Em breve teremos quizzes completos aqui na plataforma!")
        
        st.info("""
        Se você entende essa diferença, já está à frente de muitos gestores no mercado.
        """)
        
        st.title("⚖️ Custos x Despesas e seus impactos na DRE")
        
        st.subheader("🔍 Como custos e despesas se refletem no resultado da empresa?")
        
        st.markdown("""
        > Antes de tudo, precisamos entender que **custos** e **despesas** não são apenas conceitos contábeis — eles impactam diretamente os resultados financeiros da empresa, especialmente na **Demonstração do Resultado (DRE)**.
        """)
        
        st.divider()
        
        st.subheader("📊 **Relação dos Processos com Custos, Despesas e a DRE**")
        
        # Criando o diagrama
        grafico = graphviz.Digraph()
        
        grafico.attr('node', shape='box', style='rounded, filled', fillcolor='#f0f9f9')
        
        # Processos
        grafico.node('Prod', '🔧 Processo Produtivo\n(Custos)')
        grafico.node('RH', '👥 Recursos Humanos\n(Despesas)')
        grafico.node('Mkt', '📢 Marketing\n(Despesas)')
        grafico.node('Fin', '💰 Finanças\n(Despesas)')
        grafico.node('Adm', '📑 Administrativo\n(Despesas)')
        grafico.node('Outros', '➕ Outros\n(Despesas)')
        
        # Receita e DRE
        grafico.node('Rec', '''💵 Receita
        (-) Custo das Mercadorias Vendidas
        = Lucro Bruto
        (-) Despesas Operacionais
        = Lucro Operacional''', shape='rectangle', fillcolor='#d0eafc')
        
        # Conexões
        grafico.edge('Prod', 'Rec', label='➡️ Custo (CMV)')
        grafico.edge('RH', 'Rec', label='➡️ Despesa')
        grafico.edge('Mkt', 'Rec', label='➡️ Despesa')
        grafico.edge('Fin', 'Rec', label='➡️ Despesa')
        grafico.edge('Adm', 'Rec', label='➡️ Despesa')
        grafico.edge('Outros', 'Rec', label='➡️ Despesa')
        
        st.graphviz_chart(grafico)
        
        st.divider()
        
        st.subheader("💡 **Conceituando:**")
        
        st.markdown("""
        ### ✔️ **Custos**
        - 🔧 São os gastos **diretamente ligados** à produção de bens ou serviços, ou à compra de mercadorias para revenda.
        - ➕ **Exemplos:** matéria-prima, salários da produção, energia da fábrica, depreciação de máquinas, custo de mercadorias para revenda.
        - 🔍 **Na DRE:** aparecem no grupo **"Custo das Mercadorias Vendidas (CMV)"**, **reduzindo a Receita para gerar o Lucro Bruto.**
        
        ---
        
        ### ✔️ **Despesas**
        - 🏢 São os gastos necessários para **manter a estrutura administrativa, comercial e de suporte**, mas **não estão diretamente ligados à produção.**
        - ➕ **Exemplos:** salários da administração, marketing, despesas financeiras, aluguel da sede, serviços contábeis, despesas com TI.
        - 🔍 **Na DRE:** aparecem no grupo **"Despesas Operacionais"**, sendo deduzidas do **Lucro Bruto** para se chegar ao **Lucro Operacional.**
        """)
        
        st.divider()
        
        st.subheader("📈 **Visão simplificada da DRE:**")
        st.markdown("""
        A **Demonstração do Resultado do Exercício (DRE)** mostra o caminho do dinheiro na empresa:  
        Das **Receitas**, subtraímos os **Custos** e as **Despesas**, chegando ao **Lucro ou Prejuízo**.
        
        Vamos visualizar como isso funciona:
        """)
        
        # 🔷 Layout visual da DRE
        st.markdown("---")
        st.markdown("### 🔷 **Estrutura da DRE:**")
        
        # Receita
        st.markdown("""
        <div style="background-color:#81C784; padding:15px; border-radius:10px;">
            <h4 style="color:#1B5E20;">🚀 Receita Bruta</h4>
            <p style="color:#212121;">Tudo que a empresa recebe pelas vendas de seus produtos ou serviços.</p>
        </div>
        """, unsafe_allow_html=True)
        
        # (-) Custos
        st.markdown("""
        <div style="background-color:#FFB74D; padding:15px; border-radius:10px;">
            <h4 style="color:#E65100;">⚙️ (-) Custos dos Produtos ou Serviços</h4>
            <p style="color:#212121;">São os gastos diretamente relacionados à produção ou entrega do serviço.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <h3 style="text-align:center;">= Lucro Bruto</h3>
        """, unsafe_allow_html=True)
        
        # (-) Despesas
        st.markdown("""
        <div style="background-color:#64B5F6; padding:15px; border-radius:10px;">
            <h4 style="color:#0D47A1;">🧾 (-) Despesas Operacionais</h4>
            <p style="color:#212121;">Gastos administrativos, comerciais, marketing, vendas, etc.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <h3 style="text-align:center;">= Resultado Operacional</h3>
        """, unsafe_allow_html=True)
        
        # Resultado
        st.markdown("""
        <div style="background-color:#FFD54F; padding:15px; border-radius:10px;">
            <h4 style="color:#F57F17;">💰 Lucro ou Prejuízo</h4>
            <p style="color:#212121;">Resultado final após considerar receitas, custos e despesas.</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # 🔥 Desafio prático — Montar a DRE
        
        st.markdown("## 🧠 **Desafio: Monte sua própria DRE!**")
        
        with st.expander("🚀 Clique aqui para testar sua compreensão"):
            st.markdown("Associe corretamente cada item à sua posição na DRE:")
        
            itens_dre = {
                "💰 Venda de produtos ou serviços": "Receita",
                "🛠️ Compra de matéria-prima": "Custo",
                "🔌 Energia elétrica da fábrica": "Custo",
                "🏢 Aluguel do escritório": "Despesa",
                "🧠 Salário do administrativo": "Despesa",
                "🚛 Frete pago para entregar mercadorias": "Custo",
                "🛒 Comissão de vendedores": "Despesa",
            }
        
            acertos = 0
            for item, resposta_correta in itens_dre.items():
                resposta = st.radio(
                    f"{item}",
                    ["Receita", "Custo", "Despesa"],
                    index=None,
                    key=item
                )
                if resposta:
                    if resposta == resposta_correta:
                        st.success(f"✅ Correto!")
                        acertos += 1
                    else:
                        st.error(f"❌ Incorreto. A resposta certa é: **{resposta_correta}**")
        
            if acertos == len(itens_dre):
                st.balloons()
                st.success("🎉 Excelente! Você classificou tudo corretamente!")
            elif acertos > 0:
                st.info(f"👍 Você acertou {acertos} de {len(itens_dre)}.")
            else:
                st.warning("🚀 Vamos começar! Classifique os itens acima.")
        
        # 🔗 Conclusão
        st.markdown("""
        > 💡 Perceba como a estrutura da DRE ajuda a entender **onde estão os maiores gastos e como se forma o lucro da empresa.**  
        > Isso vale para empresas privadas, públicas, ONGs e qualquer organização!
        """)    
        st.markdown("""
        """)
        
        st.divider()
        
        st.subheader("🚀 **Desafio Interativo!**")
        
        pergunta = st.radio(
            "📢 A empresa paga aluguel da sua sede administrativa. Esse gasto é considerado:",
            ("Custo", "Despesa"), index=None
        )
        
        if pergunta:
            if pergunta == "Despesa":
                st.success("✅ Correto! É uma despesa, pois não está diretamente ligado à produção, mas sim ao suporte da operação.")
            else:
                st.error("❌ Incorreto. O aluguel da sede administrativa não faz parte do custo de produção.")
        
        st.markdown("---")
        
        st.subheader("🎯 **Mais desafios ou simulações?**")
        
        if st.button("Quero simular uma DRE!"):
            st.info("🔧 Em breve vamos incluir uma planilha simuladora da DRE, mostrando como custos e despesas impactam o resultado.")
    
        # Quiz interativo
        with st.expander("🧩 Teste Seu Conhecimento"):
            resposta = st.radio(
                "O salário do supervisor de produção é classificado como:",
                ["Custo Direto", "Custo Indireto", "Despesa"],
                index=None
            )
            if resposta:
                if resposta == "Custo Indireto":
                    st.success("✅ Correto! É um custo indireto pois beneficia toda a produção.")
                else:
                    st.error("❌ Revise a classificação de custos indiretos")
                
        
        st.header("📊 Análise [Simples] de Impacto de Custos")
        st.markdown("""
            ```math
            Custo\ Total = Custo\ Fixo + (Custo\ Variável\ Unitário × Quantidade)
            ```

            
            ```math
            Ponto\ de\ Equilíbrio = (Custo\ Total + Despesas) / (PV - CVU)
            ```
        """)

        # Comportamento dos Custos
        c1, c2 = st.columns([1, 2])
        with c1:
        # Controles interativos
            st.markdown("""
            """)
        
        with c2:
            st.subheader("Parâmetros de Entrada")
            cf = st.slider("Custo Fixo Total (R$):", 1000, 50000, 10000, 500, 
                          help="Custos que não variam com o volume de produção")
            cv = st.slider("Custo Variável Unitário (R$):", 1, 100, 15, 1,
                          help="Custo adicional por unidade produzida")
            q = st.slider("Quantidade Produzida:", 0, 1000, 200, 10,
                         help="Volume total de unidades produzidas")
            d = st.slider("Despesas (R$):", 1000, 50000, 10000, 500, 
                         help="Total de Despesas")
            p = st.slider("Preço de venda:", 1, 100, 20, 1,
                         help="Preço unitário do produto")
        
        # Cálculos
        ct = cf + (cv * q)
        custo_medio = ct / q if q > 0 else 0
        
        # Métricas
        st.divider()
        col_met1, col_met2 = st.columns(2)
        with col_met1:
            st.metric("Custo Total Estimado", f"R$ {ct:,.2f}", 
                     help="Soma de custos fixos e variáveis totais")
        with col_met2:
            st.metric("Custo Médio por Unidade", f"R$ {custo_medio:,.2f}" if q > 0 else "N/A",
                     help="Custo total dividido pela quantidade produzida")
        
        col_met3, col_met4 = st.columns(2)
        with col_met3:
            percent_var = (cv * q) / ct * 100
            st.metric("Participação dos Custos Variáveis", f"{percent_var:.1f}%",
                     help="Quanto do custo total é variável")
        with col_met4:
            if p > cv:
                peq = (cf+d)/(p-cv)
                st.metric("Ponto de Equilíbrio", f"{int(peq)} unidades",
                     help="Quantidade necessária para cobrir todos os custos")
            elif p == cv:
                st.markdown("""
                Ponto de Equilíbrio = ERRO!<br>(Preço de Venda = Custo Unitário)
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                CUIDADO! (Preço de Venda abaixo do Custo Unitário)
                """)
            
        # Análise de sensibilidade
        st.divider()
        st.subheader("🔍 Análise de Sensibilidade")
        
        # Simulação de diferentes quantidades
        q_range = np.linspace(0, q*2, 50)
        ct_range = cf + (cv * q_range)
        cm_range = ct_range / np.where(q_range > 0, q_range, 1)
        
        t1, t2 = st.tabs(["Gráfico de Custos", "Tabela de Dados"])
        
        with t1:
            fig = px.line(x=q_range, y=ct_range, 
                         labels={'x': 'Quantidade Produzida', 'y': 'Custo Total (R$)'},
                         title="Relação entre Quantidade e Custo Total")
            fig.add_vline(x=q, line_dash="dash", line_color="red",
                         annotation_text=f"Quantidade Atual: {q}", 
                         annotation_position="top left")
            fig.update_layout(hovermode="x unified")
            st.plotly_chart(fig, use_container_width=True)
        
        with t2:
            df = pd.DataFrame({
                'Quantidade': q_range.astype(int),
                'Custo Total': ct_range,
                'Custo Médio': cm_range
            })
            st.dataframe(df.style.format({
                'Custo Total': 'R$ {:,.2f}',
                'Custo Médio': 'R$ {:,.2f}'
            }), use_container_width=True)
        
        # Análise de cenários
        st.divider()
        st.subheader("🌐 Análise de Cenários")
        
        scenarios = {
            "Otimista (CV -20%)": cv * 0.8,
            "Atual": cv,
            "Pessimista (CV +20%)": cv * 1.2
        }
        
        scenario_data = []
        for name, cv_scenario in scenarios.items():
            ct_scenario = cf + (cv_scenario * q)
            scenario_data.append({
                "Cenário": name,
                "Custo Variável Unitário": cv_scenario,
                "Custo Total": ct_scenario,
                "Diferença": ct_scenario - ct
            })
        
        df_scenarios = pd.DataFrame(scenario_data)
        col_an1, col_an2 = st.columns([1, 2])
        
        with col_an1:
            st.markdown("**Impacto de Variações no Custo Variável**")
            st.dataframe(df_scenarios.style.format({
                "Custo Variável Unitário": "R$ {:.2f}",
                "Custo Total": "R$ {:,.2f}",
                "Diferença": "R$ {:,.2f}"
            }), hide_index=True, use_container_width=True)
        
        with col_an2:
            fig2 = px.bar(df_scenarios, x='Cenário', y='Custo Total',
                         color='Cenário',
                         title="Comparação de Cenários",
                         text=[f"R$ {x:,.2f}" for x in df_scenarios['Custo Total']])
            fig2.update_layout(showlegend=False)
            st.plotly_chart(fig2, use_container_width=True)
        
        # Explicação dos conceitos
        with st.expander("📚 Explicação dos Conceitos"):
            st.markdown("""
            **Análise de Impacto de Custos**:
            - **Custo Fixo**: Despesas que não mudam com o volume de produção (aluguel, salários)
            - **Custo Variável**: Custos diretamente ligados à produção (matéria-prima, embalagem)
            - **Ponto de Equilíbrio**: Quantidade necessária para cobrir todos os custos (fixos + variáveis)
            
            **Análise de Sensibilidade** mostra como mudanças nos parâmetros afetam os resultados.
            """)

        # 🔜 Botão para próxima página
        st.markdown(" ")
        if st.button("👉 Avançar para o próximo tópico: Conhecer o Método de Custeio por Absorção"):
            st.switch_page("pages/3_📊_Custeio_por_Absorcao.py")

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
