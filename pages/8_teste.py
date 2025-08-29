import streamlit as st
import pandas as pd

def main():
    st.title("📝 Simulador de Prova - Custeio por Absorção")
    st.markdown("""
    Teste seus conhecimentos sobre custeio por absorção básico e avançado.
    *Responda todas as questões e verifique seu resultado no final.*
    """)
    
    # === QUIZ RÁPIDO (para engajar desde o início) ===
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

    st.title("📝 Simulador de Prova - Custeio por Absorção")
      st.markdown("""
      Teste seus conhecimentos sobre custeio por absorção básico e avançado.
      *Responda todas as questões e verifique seu resultado no final.*
      """)
      
      # Sistema de pontuação
      if 'score' not in st.session_state:
          st.session_state.score = 0
          st.session_state.answers = {}
      
      # Questões
      questions = [
          {
              "type": "multiple_choice",
              "question": "1. Qual a fórmula correta do Custo de Produção do Período (CPP)?",
              "options": [
                  "A",
                  "B",
                  "C",
                  "D"
              ],
              "answer": 0,
              "explanation": "O CPP é a soma de Matéria-Prima (MP), Mão de Obra Direta (MOD) e Custos Indiretos de Fabricação (CIF)."
          },
          {
          "type": "multiple_choice",
          "question": "Uma indústria possui dois departamentos auxiliares: Manutenção e Refeitório. Os custos mensais são R\$ 10.000 para Manutenção e R\$ 5.000 para Refeitório. Se os departamentos produtivos utilizam 70% da Manutenção e 60% do Refeitório, quanto será alocado ao setor produtivo no total?",
          "options": [
              "R\$ 10.000",
              "R\$ 10.500",
              "R\$ 11.000",
              "R\$ 11.500",
              "R\$ 12.000",
          ],
          "answer": 0,
          "explanation": "Manutenção: 70% x 10.000 = 7.000. Refeitório: 60% x 5.000 = 3.000. Total alocado ao setor produtivo: 7.000 + 3.000 = R\$ 10.000."
          }
      ]
      
      # Formulário de questões
      with st.form("test_form"):
          st.subheader("Questões")
          
          for i, q in enumerate(questions):
              st.markdown(f"**{q['question']}**")
              
              if q['type'] == 'multiple_choice':
                  user_answer = st.radio(
                      f"Opções Q{i+1}",
                      q['options'],
                      index=None,
                      key=f"q{i}"
                  )
                  st.session_state.answers[i] = q['options'].index(user_answer) if user_answer else None
                  
              elif q['type'] == 'true_false':
                  user_answer = st.radio(
                      f"Verdadeiro/Falso Q{i+1}",
                      ["Verdadeiro", "Falso"],
                      index=None,
                      key=f"q{i}"
                  )
                  st.session_state.answers[i] = (user_answer == "Verdadeiro") if user_answer else None
                  
              elif q['type'] in ['calculation', 'case_analysis']:
                  user_answer = st.number_input(
                      f"Resposta Q{i+1} (R\$)",
                      value=None,
                      step=1000,
                      key=f"q{i}"
                  )
                  st.session_state.answers[i] = user_answer if user_answer is not None else None
          
          submitted = st.form_submit_button("📥 Submeter Respostas")
      
      # Correção
      if submitted:
          st.session_state.score = 0
          st.divider()
          st.subheader("🔍 Resultado")
          
          for i, q in enumerate(questions):
              st.markdown(f"**Q{i+1}:** {q['question']}")
              
              if st.session_state.answers.get(i) is None:
                  st.error("Não respondida")
                  continue
              
              if q['type'] in ['multiple_choice', 'true_false']:
                  if st.session_state.answers[i] == q['answer']:
                      st.success(f"✅ Correta! {q['explanation']}")
                      st.session_state.score += 1
                  else:
                      correct = q['options'][q['answer']] if q['type'] == 'multiple_choice' else "Verdadeiro" if q['answer'] else "Falso"
                      st.error(f"❌ Incorreta. Resposta correta: {correct}. {q['explanation']}")
              
              elif q['type'] in ['calculation', 'case_analysis']:
                  tolerance = q.get('tolerance', 0.01 * q['answer'])
                  if abs(st.session_state.answers[i] - q['answer']) <= tolerance:
                      st.success(f"✅ Correta! {q['explanation']}")
                      st.session_state.score += 1
                  else:
                      st.error(f"❌ Incorreta. Resposta correta: R\$ {q['answer']:,.2f}. {q['explanation']}")
          
          # Resultado final
          st.divider()
          score_percent = (st.session_state.score / len(questions)) * 100
          st.metric("Pontuação Final", 
                   f"{st.session_state.score}/{len(questions)} ({score_percent:.0f}%)")
          
          if score_percent >= 70:
              st.success("🎉 Parabéns! Você domina o custeio por absorção!")
          elif score_percent >= 40:
              st.warning("📚 Bom esforço! Reveja os conceitos e tente novamente!")
          else:
              st.error("✏️ Estude mais os fundamentos antes de tentar novamente.")
          
         
if __name__ == "__main__":
    main()
