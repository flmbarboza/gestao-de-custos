import streamlit as st
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google, safe_log_interacao

def main():
    # Configuração da página
    st.set_page_config(page_title="Gestão de Custos - FAGEN/UFU", layout="centered")

    # Recupera o nome do usuário
    nome_usuario = get_anon_user_id()
    pagina_atual = "Início"

    # Registra o acesso
    if 'page1_acessada' not in st.session_state:
        log_acesso_google(nome_usuario, pagina_atual, f"acessou_{pagina_atual}")
        st.session_state.page1_acessada = True

    # Título principal com ícone
    st.title("🏦 Gestão de Custos – FAGEN/UFU")
    st.markdown("<h3 style='color: #2C3E50;'>Onde números viram decisões estratégicas</h3>", unsafe_allow_html=True)

    # === NOVO CONTEXTO DE ENGAJAMENTO ===
    st.markdown("""
    <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px; border-left: 5px solid #27ae60;">
        <p style="font-size: 1.1em; color: #2C3E50;">
            Você já parou para pensar que <strong>9 em cada 10 empresas que falham têm problemas de gestão de custos</strong>? 
            E que <strong>tomar decisões sem entender os custos é como dirigir no escuro</strong>?
        </p>
        <p style="font-size: 1.1em;">
            Em um mundo de margens apertadas, crises econômicas e transformação digital, dominar <strong>Gestão de Custos</strong> 
            não é apenas saber lançar números — é <strong>salvar empresas, criar estratégias e gerar valor real</strong>.
        </p>
        <p style="font-style: italic; color: #16a085;">
            Esta disciplina é sua chave para se tornar um(a) administrador(a) <strong>crítico, estratégico e capaz de impactar resultados</strong>.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # === CONTEXTO PEDAGÓGICO E INTERDISCIPLINARIDADE ===
    with st.expander("🔍 Por que Gestão de Custos é essencial no seu curso? (Conexão com o PPC)", expanded=False):
        st.markdown("""
        O Projeto Pedagógico do Curso de Administração da FAGEN/UFU destaca que você deve formar-se como um(a) profissional:
        
        - 🔗 **Interdisciplinar**: conectando conhecimentos de **Contabilidade, Finanças, Marketing e Operações**.
        - 🎯 **Generalista com foco em decisão**: capaz de atuar em qualquer área da organização.
        - 💡 **Crítico e analítico**: com habilidades para interpretar dados e propor soluções reais.

        E a **Gestão de Custos** é o **ponto de encontro** dessas competências. Ela dialoga diretamente com:
        
        - **Contabilidade I e II** → base para apuração de custos.
        - **Finanças Corporativas** → análise de rentabilidade e viabilidade.
        - **Marketing** → precificação com base em custos e demanda.
        - **Operações** → controle de produção e eficiência.
        - **Extensão** → aplicação em projetos reais, como planos de negócios e consultorias.

        > 📌 *Como diz o PPC: “O curso busca superar uma formação fragmentada, enfatizando uma formação integral.”*  
        > **Gestão de Custos é isso**: integrar teoria e prática para resolver problemas reais.
        """)

        if st.button("✅ Clique aqui se essa informação foi útil", key="btn_conexao"):
            safe_log_interacao(nome_usuario, pagina_atual, "expandiu_conexao")
            st.toast("Boa! Você está vendo o todo! 🌐", icon="🧠")

    # === OBJETIVOS DA DISCIPLINA ===
    with st.expander("🎯 O que você vai dominar nesta disciplina?", expanded=True):
        st.markdown("""
        Ao final deste curso, você será capaz de:
        
        - 🔢 Apurar custos com precisão usando **custeio por absorção e variável**.
        - 💰 Definir preços com base em custos, tributos e margens estratégicas.
        - 📊 Calcular o **ponto de equilíbrio** e analisar a **margem de contribuição**.
        - 🧠 Tomar decisões sob escassez: **o que produzir quando não dá para fazer tudo?**
        - 📈 Interpretar demonstrações de resultados com foco gerencial, não apenas contábil.
        - 🛠️ Aplicar esses conceitos em **projetos reais**, como planos de negócios, consultorias ou empresas juniores.

        > 💡 *Este não é um curso de “fazer conta”. É um curso de **pensar como gestor**.*
        """)

        if st.button("✅ Clique aqui se essa informação foi útil", key="btn_objetivos"):
            log_interacao_google(nome_usuario, pagina_atual, "expandiu_objetivos")
            st.toast("Você está no caminho certo! 🎯", icon="💡")

    # === PROGRAMA INTERATIVO ===
    st.subheader("📚 Jornada de Aprendizagem")
    st.markdown("Clique nas unidades para saber mais e começar sua trilha:")

    cols = st.columns(3)
    unidades = [
        ("1️⃣ Fundamentos de Custos", "Comportamento de custos, classificação e impacto nas decisões", "2_📚_Introducao.py"),
        ("2️⃣ Custeio por Absorção", "CPP, CPA, CPV, rateio de CIF e DRE", "3_📊_Custeio_por_Absorcao_I.py"),
        ("3️⃣ Custeio Variável", "Margem de Contribuição, DRE Gerencial, Análise Custo-Volume-Lucro e +", "4_📈_Custeio_Variavel.py"),
        ("4️⃣ Precificação Estratégica", "Mark-up, tributos e decisão de preço", "5_💰_Precificacao.py"),
        ("5️⃣ Decisão com Restrições", "O que produzir? Como alocar recursos escassos?", "6_⚖️_Margem_Contribuicao.py")
    ]
    
    for i, (unidade, desc, pagina_py) in enumerate(unidades):
        col = cols[i % 3]
        botao_key = f"botao_unidade_{i}"
    
        if col.button(unidade, help=desc, width=True, key=botao_key):
            # Registra a interação
            safe_log_interacao(nome_usuario, pagina_atual, f"clicou_unidade_{i+1}")
            st.toast(f"🚀 Ótimo! {unidade} é essencial para sua carreira!", icon="✅")
            
            # Salva a unidade atual no estado da sessão (opcional, para usar depois)
            st.session_state['ultima_unidade_acessada'] = i + 1
            
            # Navega para a página da unidade
            st.switch_page(f"pages/{pagina_py}")

    # === CONEXÃO COM A REALIDADE PROFISSIONAL ===
    st.markdown("<br>", unsafe_allow_html=True)
    with st.expander("💼 E na prática? O que um(a) administrador(a) faz com isso?", expanded=False):
        st.markdown("""
        Imagine que você está em uma empresa e o lucro caiu — mas as vendas aumentaram.  
        **Qual é o problema?**  
        Talvez o custo de produção tenha subido, ou o rateio de custos indiretos esteja distorcendo a realidade.

        Com Gestão de Custos, você:
        
        - 🔎 Identifica **produtos que parecem lucrativos, mas na verdade geram prejuízo**.
        - 📉 Propõe **ajustes de mix de produção** com base em margem de contribuição.
        - 💬 Apresenta relatórios claros para a diretoria: “Esse produto tem alta venda, mas baixa margem. Devemos repensar.”
        - 🚀 Cria um **plano de negócios sustentável**, com preços realistas e custos controlados.

        > 👨‍💼 *Egressos do curso relatam que conhecimentos em custos foram decisivos em processos seletivos, consultorias e até na criação de startups.*
        """)

        if st.button("✅ Clique aqui se essa informação foi útil", key="btn_pratica"):
            log_interacao_google(nome_usuario, pagina_atual, "expandiu_pratica")
            st.toast("Você está pensando como um(a) profissional! 💼", icon="🚀")

    # === CHAMADA PARA AÇÃO FINAL ===
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align: center; padding: 20px; background-color: #e8f4f8; border-radius: 10px;">
        <h4>Pronto para transformar custos em vantagem competitiva?</h4>
        <p>Os números não mentem — mas só quem sabe interpretá-los pode mudar o jogo.</p>
        <p style="font-weight: bold;">Vamos juntos?</p>
    </div>
    """, unsafe_allow_html=True)

    # === ÁUDIO (OPCIONAL - EXEMPLO FUTURO) ===
    # if st.button("🎧 Ouvir: Por que estudar Gestão de Custos?"):
    #     log_interacao_google(nome_usuario, pagina_atual, "ouviu_audio_introducao")
    #     texto_audio = (
    #         "Bem-vindo à Gestão de Custos. "
    #         "Você vai aprender a transformar números em decisões estratégicas. "
    #         "Dominar custos é essencial para qualquer administrador que quer impactar resultados. "
    #         "Vamos juntos nessa jornada?"
    #     )
    #     leitor_de_texto(texto_audio)
    #     st.success("Áudio reproduzido! 🎧")

if __name__ == "__main__":
    main()
