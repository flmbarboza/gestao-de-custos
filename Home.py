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

    # === IDENTIFICAÇÃO ANÔNIMA (com toque de gamificação) ===
    user_id = get_anon_user_id()
    
    st.success(f"""🔐 Dados anônimos. Usamos isso para tornar a experiência melhor — nada pessoal, tudo pedagógico.
                Assim começa sua missão! Toda sua jornada contribui para melhorar esse site. 
                Vamos usar um código de identificação para você `{user_id[:8]}`. Caso queira saber mais sobre isso, contate o idealizador.""")
    
    # === QUIZ RÁPIDO (para engajar desde o início) ===# === QUIZ RÁPIDO (para engajar desde o início) ===
    with st.expander("🎯 Teste rápido: Você entende de custos?", expanded=True):
        st.markdown("Se uma empresa vende mais, mas lucra menos, o problema provavelmente é:")
    
        # Inicializa estado do quiz (apenas uma vez)
        if 'quiz_feito' not in st.session_state:
            st.session_state.quiz_feito = False
            st.session_state.quiz_acertou = False
            st.session_state.resposta_selecionada = None
    
        # --- helper seguro para logging (não quebra a UI se log falhar) ---
        def safe_log_interacao(nome=None, pagina=None, acao=None):
            try:
                # tenta chamar sua função de log (assume assinatura nome, pagina, acao)
                log_interacao_google(nome=nome, pagina=pagina, acao=acao)
            except Exception:
                # se algo der errado no log, ignora silenciosamente para não quebrar a UI
                pass
    
        # Garante que exista um user_id e nome da página
        user_id = st.session_state.get('user_id') or get_anon_user_id()
        page_name = st.session_state.get('pagina') or "Página de Abertura"
    
        # Opções com placeholder (evita index=None)
        options = [
            "-- Selecione --",
            "A) Falta de marketing",
            "B) Preço baixo demais",
            "C) Custo mal calculado ou mal alocado",
            "D) Crise econômica"
        ]
    
        # Formulário do quiz
        with st.form(key="quiz_form"):
            resposta = st.selectbox(
                label="Escolha uma opção:",
                options=options,
                index=0,
                key="quiz_select"
            )
            submit_button = st.form_submit_button("✅ Verificar resposta")
    
        # Processamento após submit (fora do with)
        if submit_button:
            st.session_state.quiz_feito = True
            st.session_state.resposta_selecionada = resposta
    
            if resposta == "-- Selecione --":
                st.warning("⚠️ Por favor, selecione uma opção antes de verificar!")
                st.session_state.quiz_acertou = False
                safe_log_interacao(nome=user_id, pagina=page_name, acao="quiz_sem_resposta")
            elif resposta == "C) Custo mal calculado ou mal alocado":
                st.success("🔥 Acertou! Esse é o *núcleo* da Gestão de Custos.")
                st.balloons()
                st.session_state.quiz_acertou = True
                safe_log_interacao(nome=user_id, pagina=page_name, acao="quiz_acertou")
            else:
                st.warning("💡 Quase! O erro mais comum é achar que é marketing ou preço. Mas sem custos bem mapeados, qualquer decisão é no escuro.")
                st.session_state.quiz_acertou = False
                safe_log_interacao(nome=user_id, pagina=page_name, acao="quiz_errou")
    
            st.info("📌 Aprender a enxergar isso é o que separa um técnico de um estrategista.")
    
        # Reexibe feedback caso já tenha respondido (evita perda após rerun)
        elif st.session_state.quiz_feito:
            resp = st.session_state.resposta_selecionada
            if resp is None or resp == "-- Selecione --":
                st.warning("⚠️ Você deixou o quiz sem responder.")
            elif st.session_state.quiz_acertou:
                st.success("🔥 Acertou! Esse é o *núcleo* da Gestão de Custos.")
                st.info("📌 Aprender a enxergar isso é o que separa um técnico de um estrategista.")
            else:
                st.warning("💡 Quase! O erro mais comum é achar que é marketing ou preço. Mas sem custos bem mapeados, qualquer decisão é no escuro.")
                st.info("📌 Aprender a enxergar isso é o que separa um técnico de um estrategista.")
                
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
