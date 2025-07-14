import streamlit as st
import pandas as pd

def main():
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
                "MP + MOD + CIF",
                "CPA + EIPA - EFPA",
                "CPP + EIPP - EFPP",
                "MOD + EI - EF"
            ],
            "answer": 0,
            "explanation": "O CPP é a soma de Matéria-Prima (MP), Mão de Obra Direta (MOD) e Custos Indiretos de Fabricação (CIF)."
        },
        {
            "type": "true_false",
            "question": "2. No custeio por absorção, os custos fixos podem ser rateados usando o volume produzido como critério de rateio.",
            "answer": True,
            "explanation": "Verdadeiro. Essa é uma característica considerada mais simples do custeio por absorção, porém é aplicável."
        },
        {
            "type": "calculation",
            "question": "3. Uma empresa teve: MP R\$ 50.000, MOD R\$ 30.000, CIF R\$ 20.000. Qual o CPP?",
            "answer": 100000,
            "tolerance": 0,
            "explanation": "CPP = MP + MOD + CIF = 50.000 + 30.000 + 20.000 = R$ 100.000"
        },
        {
            "type": "multiple_choice",
            "question": "4. Qual destes NÃO é um critério comum para rateio de CIF?",
            "options": [
                "Horas-máquina",
                "Número de funcionários",
                "Área ocupada",
                "Cor preferida do gerente"
            ],
            "answer": 3,
            "explanation": "Critérios de rateio devem ser objetivos e mensuráveis, não subjetivos como preferências pessoais."
        },
        {
            "type": "case_analysis",
            "question": "5. Uma fábrica produziu 1.000 unidades com CPA de R\$ 80.000 e vendeu 800 unidades. Se o EIPA era R\$ 10.000, qual o CPV?",
            "answer": 74000,
            "tolerance": 0,
            "explanation": "CPV = (CPA / Unidades Produzidas) × Unidades Vendidas + EIPA - EFPA\n= (80.000/1.000)×800 + 10.000 - (80.000/1.000×200) = R\$ 74.000"
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
                    f"Resposta Q{i+1} (R$)",
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
                    st.error(f"❌ Incorreta. Resposta correta: R$ {q['answer']:,.2f}. {q['explanation']}")
        
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
        
        # Sugestões de estudo
        st.markdown("""
        **Recursos recomendados:**
        - Capítulos 5 e 6 do livro 'Contabilidade de Custos' do Prof. Eliseu Martins;
        - Capítulos 2 e 4 do livro 'Série Desvendando as Finanças - Administração Custos Preços Lucros' do Prof. Bruni;
        - Unidade 2 do livro 'Análise de Custo' de Aline Alves e colaboradores; e,
        - Parte I do livro 'Análise de custos: uma abordagem simples e objetiva' de Eduardo F. Lyrio e colaboradores.
        """)
    
    # Navegação
    st.divider()
    cols = st.columns(3)
    with cols[0]:
        if st.button("⬅️ Voltar ao Custeio por Absorção"):
            st.switch_page("pages/3_📊_Custeio_por_Absorcao_I.py")
    with cols[1]:
        if st.button("📊 Avançar para Custeio Variável"):
            st.switch_page("pages/4_📈_Custeio_Variavel.py")
    with cols[2]:
        subcol1, subcol2 = st.columns([3,1])  # 3:1 ratio
        with subcol2:
            if st.button("🔄 Refazer Teste"):
                st.session_state.score = 0
                st.session_state.answers = {}
                st.rerun()

if __name__ == "__main__":
    main()
