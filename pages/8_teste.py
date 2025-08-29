import streamlit as st
import pandas as pd
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google

def main():
    nome_usuario = st.session_state.get("user_id") or get_anon_user_id()
    pagina = "pagina_teste"
    # === QUIZ RÁPIDO (para engajar desde o início) ===
    with st.expander("🎯 Teste rápido: Você entende de custos?", expanded=False):
        
        # --- questão (estrutura solicitada) ---
        q = [{   "question": "Se uma empresa vende mais, mas lucra menos, o problema provavelmente é:",
                "options": [ "A) Falta de marketing", "B) Preço baixo demais", "C) Custo mal calculado ou mal alocado",
                    "D) Crise econômica"],
                "answer": 2,  # índice correto
                "explanation": "O núcleo da Gestão de Custos está em entender e alocar corretamente os custos."
                }]
        
        # pega a primeira (única) questão para o quiz rápido
        #q = question[0]
        
        # --- estado minimalista e seguro ---
        if "quiz_done" not in st.session_state:
            st.session_state.quiz_done = False
            st.session_state.quiz_choice = None
        
        #page_name = st.session_state.get(pagina, "Página de Abertura")
        
        # wrapper seguro para logging (garante que falha no logger não quebre a UI)
        def safe_log_interacao(nome, pagina, acao):
            try:
                log_interacao_google(nome=nome, pagina=pagina, acao=acao)
            except Exception:
                # falha silenciosa no log para não interromper o app
                pass
                
        # --- formulário simples ---
        with st.form("quiz_form"):
            choices = ["-- Selecione --"] + q[0]["options"]
            escolha = st.radio(
                "Escolha uma opção:",
                choices,
                index=None,
                key="quiz_0"
            )
            enviar = st.form_submit_button("✅ Verificar resposta")
        
        if enviar:
            if escolha == "-- Selecione --":
                st.warning("⚠️ Por favor, selecione uma opção antes de verificar!")
                safe_log_interacao(nome_usuario, pagina, "quiz_sem_resposta")
            else:
                idx = q[0]["options"].index(escolha)
                st.session_state.quiz_choice = idx
                st.session_state.quiz_done = True
        
                if idx == q["answer"]:
                    st.success("🔥 Acertou! " + q[0].get("explanation", ""))
                    st.balloons()
                    safe_log_interacao(nome_usuario, pagina, "quiz_acertou")
                else:
                    st.warning(f"💡 Quase! Resposta correta: {q[0]['options'][q[0]['answer']]}.")
                    st.info(q[0].get("explanation", ""))
                    safe_log_interacao(nome_usuario, pagina, "quiz_errou")
        
        
if __name__ == "__main__":
    main()
