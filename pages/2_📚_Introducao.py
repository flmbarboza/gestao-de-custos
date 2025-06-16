import streamlit as st
import streamlit as st
import streamlit.components.v1 as components
import streamlit as st
import graphviz

def main():
    st.title("📚 Introdução à Contabilidade Gerencial de Custos")
    
    with st.expander("📌 Objetivos da Unidade", expanded=True):
        st.markdown("""
        - Compreender terminologia básica de custos
        - Classificar custos por natureza e comportamento
        - Analisar o comportamento de custos
        """)
    
    st.subheader("🧠 Conceitos Fundamentais")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Terminologia:**
        - Gastos
            - Custos 
            - Despesas
            - Investimentos
            - Perda
        - Desembolso
        """)
    
    with col2:
        st.markdown("""
        **Classificação de Custos:**
        - Diretos vs. Indiretos
        - Fixos vs. Variáveis
        - Custos vs. Despesas
        """)
        
    st.subheader("💡 Por que entender custos é crucial?")
    
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
            respostas[pergunta] = st.radio(pergunta, ["Verdadeiro", "Falso"], key=pergunta)
    
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
    
    # 🏗️ Cenários por setor
    st.subheader("🏢 E na prática? Como isso aparece em diferentes setores?")
    
    setor = st.selectbox(
        "Escolha o setor para explorar:",
        ["Indústria", "Comércio", "Serviços", "Administração Pública"]
    )
    
    if setor == "Indústria":
        st.markdown("""
    **Indústria:**  
    - 🏭 **Custos:** Matéria-prima, mão de obra da fábrica, energia da produção, manutenção das máquinas.  
    - 💸 **Despesas:** Marketing, vendas, administrativo, RH, aluguel do escritório.  
    - 💼 **Investimentos:** Compra de máquinas, galpões, tecnologia de produção.  
    """)
    elif setor == "Comércio":
        st.markdown("""
    **Comércio:**  
    - 🏪 **Custos:** Compra de mercadorias para revenda, transporte dos produtos, armazenamento.  
    - 💸 **Despesas:** Vendedores, propaganda, aluguel da loja, sistemas de gestão.  
    - 💼 **Investimentos:** Reformas, expansão de lojas, aquisição de equipamentos.  
    """)
    elif setor == "Serviços":
        st.markdown("""
    **Serviços:**  
    - 👩‍⚕️ **Custos:** Salário dos profissionais diretamente envolvidos na entrega (médicos, professores, consultores), materiais usados na prestação do serviço.  
    - 💸 **Despesas:** Publicidade, atendimento, suporte, administração, aluguel do escritório.  
    - 💼 **Investimentos:** Softwares, equipamentos especializados, estrutura física.  
    """)
    else:
        st.markdown("""
    **Administração Pública:**  
    - 🏛️ **Custos:** Recursos diretamente aplicados em serviços públicos (salários de médicos de hospitais públicos, professores de escolas públicas, manutenção dos espaços de atendimento).  
    - 💸 **Despesas:** Atividades administrativas, suporte, gestão, auditoria, comunicação.  
    - 💼 **Investimentos:** Obras públicas, compra de veículos, construção de hospitais, sistemas tecnológicos.  
    """)
    
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
    
    st.subheader("💡 **Refletindo sobre os Conceitos**")
    
    st.markdown("""
    ### 🏭 **No Setor Industrial:**
    - **Custo:** Matéria-prima, mão de obra da produção, depreciação de máquinas.
    - **Despesa:** Energia da área administrativa, salário do contador, marketing.
    - **Investimento:** Compra de uma nova máquina.
    - **Perda:** Roubo de estoque, incêndio sem seguro.
    
    ### 🏪 **No Comércio:**
    - **Custo:** Compra dos produtos para revenda.
    - **Despesa:** Salário dos vendedores, aluguel da loja.
    - **Investimento:** Ampliação da loja.
    - **Perda:** Produtos quebrados ou vencidos.
    
    ### 💼 **No Setor de Serviços:**
    - **Custo:** Salário dos consultores, ferramentas de software usadas no atendimento.
    - **Despesa:** Marketing, aluguel do escritório.
    - **Investimento:** Compra de computadores novos.
    - **Perda:** Cancelamento não pago de um contrato.
    
    ### 🏛️ **Na Administração Pública:**
    - **Custo:** Materiais usados na prestação de serviços públicos (ex.: material escolar em escolas públicas).
    - **Despesa:** Energia elétrica da prefeitura, salários da área administrativa.
    - **Investimento:** Construção de uma nova escola.
    - **Perda:** Danificação de veículos públicos sem cobertura.
    
    """)
    
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
    

    
    st.info("""
    Se você entende essa diferença, já está à frente de muitos gestores no mercado.
    """)
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
    # 🔜 Botão para próxima página
    st.markdown("---")
    if st.button("👉 Avançar para: Planejamento de Custos"):
        st.switch_page("pages/3_📊_Custeio_Absorcao.py")

if __name__ == "__main__":
    main()
