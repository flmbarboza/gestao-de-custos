import streamlit as st
from datetime import datetime
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google

# Configuração da página
st.set_page_config(
    page_title="Gestão de Custos Academy",
    page_icon="🏦",
    layout="centered"
)

# === REGISTRA O ACESSO (APENAS UMA VEZ POR SESSÃO) ===
nome_usuario = get_anon_user_id()
pagina = "Página de Abertura"

if 'home_acessada' not in st.session_state:
    log_acesso_google(nome_usuario, pagina, acao="acessou_home")
    st.session_state.home_acessada = True

# Evita reexecução
if 'redirecionado' not in st.session_state:
    st.session_state.redirecionado = False

if not st.session_state.redirecionado:
    st.session_state.redirecionado = True

    # === TÍTULO E BOAS-VINDAS DINÂMICAS ===
    st.markdown("<h1 style='text-align: center;'>🏦 Gestão de Custos <span style='color:#27ae60'>Academy</span></h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #2C3E50;'>Onde números viram poder de decisão</h3>", unsafe_allow_html=True)

    st.markdown("""
    <div style='text-align: center; font-size: 1.1em; color: #34495E; margin-bottom: 20px;'>
        Você já parou pra pensar que <strong>o maior erro de gestão</strong> não é perder dinheiro...<br>
        <strong>É achar que está economizando quando, na verdade, está destruindo valor?</strong>
    </div>
    """, unsafe_allow_html=True)

    st.image("pages/figs/welcome.png")

    st.success(f"""🔐 Dados anônimos. Usamos isso para tornar a experiência melhor — nada pessoal, tudo pedagógico.
                Assim começa sua missão! Toda sua jornada contribui para melhorar esse site. 
                Vamos usar um código de identificação para você `{nome_usuario[:8]}`. Caso queira saber mais sobre isso, contate o idealizador.""")
    
    # === QUIZ RÁPIDO (para engajar desde o início) ===
    with st.form("test_form"):
        st.info("🎯 Teste rápido: Você entende de custos?")
    
        # --- questão (estrutura solicitada) ---
        question = [
            {
                "type": "multiple_choice",
                "question": "Se uma empresa vende mais, mas lucra menos, o problema provavelmente é:",
                "options": [
                    "A) Falta de marketing",
                    "B) Preço baixo demais",
                    "C) Custo mal calculado ou mal alocado",
                    "D) Crise econômica"
                ],
                "answer": 2,  # índice correto
                "explanation": "O núcleo da Gestão de Custos está em entender e alocar corretamente os custos."
            }
        ]
    
        # pega a primeira (única) questão para o quiz rápido
        q = question[0]
    
        # --- estado minimalista e seguro ---
        if "quiz_done" not in st.session_state:
            st.session_state.quiz_done = False
            st.session_state.quiz_choice = None
    
        page_name = st.session_state.get("pagina", "Página de Abertura")
    
        # wrapper seguro para logging (garante que falha no logger não quebre a UI)
        def safe_log_interacao(nome, pagina, acao):
            try:
                log_interacao_google(nome=nome, pagina=pagina, acao=acao)
            except Exception:
                # falha silenciosa no log para não interromper o app
                pass
    
        st.markdown(f"**{q['question']}**")
    
        # --- formulário simples ---
        with st.form("quiz_form"):
            choices = ["-- Selecione --"] + q["options"]
            escolha = st.selectbox("Escolha uma opção:", choices, index=0, key="quiz_select_0")
            enviar = st.form_submit_button("✅ Verificar resposta")
    
        # --- processamento do submit ---
        if enviar:
            if escolha == "-- Selecione --":
                st.warning("⚠️ Por favor, selecione uma opção antes de verificar!")
                safe_log_interacao(nome_usuario, page_name, "quiz_sem_resposta")
            else:
                idx = q["options"].index(escolha)  # mapeia para índice dentro de q['options']
                st.session_state.quiz_choice = idx
                st.session_state.quiz_done = True
    
                if idx == q["answer"]:
                    st.success("🔥 Acertou! " + q.get("explanation", ""))
                    st.balloons()
                    safe_log_interacao(nome_usuario, page_name, "quiz_acertou")
                else:
                    st.warning(f"💡 Quase! Resposta correta: {q['options'][q['answer']]}.")
                    st.info(q.get("explanation", ""))
                    safe_log_interacao(nome_usuario, page_name, "quiz_errou")
    
        # --- se já respondeu em sessão anterior, reapresenta feedback ---
        elif st.session_state.quiz_done:
            idx = st.session_state.quiz_choice
            if idx == q["answer"]:
                st.success("🔥 Acertou! " + q.get("explanation", ""))
            else:
                st.warning(f"💡 Resposta correta: {q['options'][q['answer']]}.")
                st.info(q.get("explanation", ""))

    # === INSIGHTS PROVOCATIVOS (com expanders interativos) ===
    st.markdown("### 🔥 O que os melhores gestores sabem (e os outros não percebem)")

    with st.expander("📉 Produtividade > Corte de gastos", expanded=False):
        st.markdown("""
        Cortar custos é fácil. **Receber mais com menos é arte.**  
        Empresas de alta performance focam em **produtividade real**, não em demissões.  
        → [McKinsey: The Productivity Imperative](https://www.mckinsey.com/featured-insights/productivity/driving-productivity-imperative)
        """)
        if st.button("✅ Entendi: produtividade é estratégia", key="produtividade"):
            log_interacao_google(nome_usuario, pagina, "expandiu_produtividade")

    with st.expander("🤖 IA e Automação: o novo 'corte de custos'", expanded=False):
        st.markdown("""
        Automatizar processos de custos com IA pode reduzir tempo em 70%.  
        Mas o grande ganho? **Libera tempo para análise estratégica.**  
        → [McKinsey: State of AI 2023](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai-in-2023)
        """)
        if st.button("✅ Entendi: IA é aliada, não substituta", key="ia"):
            log_interacao_google(nome_usuario, pagina, "expandiu_ia")

    with st.expander("🛒 Cost-to-Serve: o segredo dos lucros ocultos", expanded=False):
        st.markdown("""
        Muitas empresas crescem... e perdem dinheiro.  
        Por quê? **Clientes 'grandes' podem ser os mais caros.**  
        Mapear o custo por cliente é essencial.  
        → [Gartner: Cost Optimization](https://www.gartner.com/en/insights/cost-optimization)
        """)
        if st.button("✅ Entendi: nem todo cliente é lucrativo", key="cost_to_serve"):
            log_interacao_google(nome_usuario, pagina, "expandiu_cost_to_serve")

    with st.expander("🌍 Benchmarks: o que as top financeiras fazem", expanded=False):
        st.markdown("""
        Funções financeiras de elite gastam apenas **0,66% da receita** com operações.  
        O resto vai para inovação, análise e estratégia.  
        → [The Hackett Group](https://www.thehackettgroup.com/)
        """)
        if st.button("✅ Entendi: eficiência gera espaço para inovação", key="benchmark"):
            log_interacao_google(nome_usuario, pagina, "expandiu_benchmark")

    # === CHAMADA PARA USAR IA (interação real e moderna) ===
    with st.expander(" 💬 Quer conversar com quem entende de custos? (sem cobrar hora)", expanded=False):
        if st.button("🤖 Pergunte à IA sobre Gestão de Custos"):
            st.info("""
            🔍 Abra seu chat favorito (Copilot, Gemini, ChatGPT) e pergunte:
            
            > _"Como calcular o custo real de um produto que tem produção terceirizada e logística variável?"_
            
            > _"Quais são os 3 erros mais comuns na precificação com base em custos?"_
            
            ✅ Use a IA como **tutora**, mas **você é o estrategista**.
            """)
            log_interacao_google(nome_usuario, pagina, "dica_ia_usada")

    # === VÍDEOS RECOMENDADOS (com mini-descrições) ===
    st.markdown("### 🎥 Aprenda rápido com vídeos práticos")
    videos = {
        "Introdução à Gestão de Custos (PT-BR)": "https://youtu.be/Dykj7QoifPM?si=7xVwzljWUi560Acq",
        "Cost-to-Serve em ação (EN)": "https://youtu.be/FZsikxMiDak?si=0beG90FrQQWHzk9D"
    }
    for nome, link in videos.items():
        if st.button(f"▶️ Assistir: {nome}", key=f"btn_{nome}"):
            st.video(link)
            log_interacao_google(nome_usuario, pagina, f"assistiu_video_{nome}")

    # === ESCOLHA DO CAMINHO (interatividade com propósito) ===
    st.markdown("---")
    st.markdown("### 🧭 Por onde você quer começar?")
    caminho = st.radio(
        "Escolha seu estilo de aprendizagem:",
        [
            "🚀 Rápido e prático – quero resolver problemas reais",
            "🧠 Profundo e estratégico – quero entender o sistema todo",
            "📊 Analítico e técnico – quero dominar os cálculos"
        ]
    )

    if st.button("➡️ Iniciar minha jornada", key="btn_inicio"):
        log_interacao_google(nome_usuario, pagina, f"escolheu_caminho_{caminho.split('–')[0].strip()}")
        st.session_state.caminho_escolhido = caminho
        st.switch_page("pages/1_🏠_Inicio.py")

# === FOOTER ELEGANTE E PROFISIONAL ===
st.sidebar.markdown("---")
st.sidebar.markdown("""
<div style='text-align: center; color: gray; font-size: 12px; line-height: 1.5;'>
    <strong>Gestão de Custos Academy</strong><br>
    <em>versão beta | 2025</em><br><br>
    Desenvolvido para a disciplina de<br>
    <strong>Gestão de Custos</strong><br>
    FAGEN / UFU<br><br>
    🌐 Conectando teoria, prática e futuro
</div>
""", unsafe_allow_html=True)
