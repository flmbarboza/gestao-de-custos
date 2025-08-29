import streamlit as st
import pandas as pd

def main():
    st.title("📝 Simulador de Prova - Custeio por Absorção")
    st.markdown("""
    Teste seus conhecimentos sobre custeio por absorção básico e avançado.
    *Responda todas as questões e verifique seu resultado no final.*
    """)

    nome_usuario = st.session_state.get("user_id") or get_anon_user_id()

    # === QUIZ RÁPIDO (para engajar desde o início) ===
    st.expander("🎯 Teste rápido: Você entende de custos?", expanded=True):
        
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
         
if __name__ == "__main__":
    main()
