import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google, safe_log_interacao

def main():
    st.title("📈 Custeio Variável (Gerencial) – Aprendizado Interativo")
    # Recupera o nome do usuário
    nome_usuario = get_anon_user_id()
    pagina_atual = "Custeio Variavel"
    
    # Registra o acesso
    if 'page4_acessada' not in st.session_state:
        log_acesso_google(nome_usuario, pagina_atual, f"acessou_{pagina_atual}")
        st.session_state.page4_acessada = True

    st.markdown("""
    Bem-vindo à análise interativa do **Custeio Variável**!  
    Aqui você vai entender como esse método auxilia na **tomada de decisões gerenciais**, com simulações, exercícios e comparações práticas.
    """)

    # ===========================
    # Expander 1: Método de Custeio Gerencial
    # ===========================
    with st.expander("🔍 1. Método de Custeio Gerencial", expanded=False):
        st.markdown("""
        ### 💡 O que é Custeio Variável?
        Também chamado de **custeio direto** ou **custeio marginal**, ele separa custos fixos e variáveis, tratando os **custos fixos como despesa do período** (não são alocados aos produtos).

        ✅ **Vantagens:**
        - Facilita análise de margem de contribuição
        - Melhor para decisões de curto prazo
        - Evita distorções no lucro com variações de estoque

        ❌ **Custeio por Absorção:**
        - Aloca custos fixos aos produtos
        - Pode inflar o lucro se estoques aumentarem
        """)

        st.subheader("📌 Atividade: Identifique o Método Correto")
        resposta1 = st.radio(
            "Em qual método o lucro pode aumentar mesmo sem venda, apenas com aumento de produção e estoque?",
            options=["Custeio Variável", "Custeio por Absorção"],
            key="q1"
        )
        if st.button("✅ Verificar Resposta", key="b1"):
            if resposta1 == "Custeio por Absorção":
                st.success("Correto! O custeio por absorção aloca custos fixos aos produtos, então aumentar estoque 'empurra' custos para o futuro, inflando o lucro.")
            else:
                st.error("Incorreto. Reveja: no custeio variável, custos fixos são despesas imediatas, então não há esse efeito.")

    # ===========================
    # Expander 2: Margem de Contribuição
    # ===========================
    with st.expander("📊 2. Margem de Contribuição", expanded=False):
        st.markdown("""
        ### 📈 O que é Margem de Contribuição (MC)?
        - **MC = Preço de Venda - Custo Variável Unitário**
        - Representa o quanto cada unidade vendida contribui para cobrir custos fixos e gerar lucro.

        **MC Total = MC unitária × quantidade**
        """)

        st.subheader("🧮 Calcule a Margem de Contribuição")
        preco_venda = st.number_input("Preço de Venda Unitário (R$)", min_value=0.0, value=100.0, step=1.0, key="mc_pv")
        custo_var = st.number_input("Custo Variável Unitário (R$)", min_value=0.0, value=60.0, step=1.0, key="mc_cv")
        qtd_vendida = st.number_input("Quantidade Vendida", min_value=0, value=500, step=10, key="mc_qtd")

        if preco_venda > 0:
            mc_unit = preco_venda - custo_var
            mc_total = mc_unit * qtd_vendida
            st.metric("Margem de Contribuição Unitária", f"R$ {mc_unit:.2f}")
            st.metric("Margem de Contribuição Total", f"R$ {mc_total:.2f}")

            st.progress(mc_unit / preco_venda if preco_venda > 0 else 0)
            st.caption(f"{(mc_unit / preco_venda * 100):.1f}% do preço vai para cobrir CF e lucro.")

    # ===========================
    # Expander 3: Elaboração de DRE com Custeio Gerencial
    # ===========================
    with st.expander("📑 3. Elaboração de DRE com Custeio Gerencial", expanded=False):
        st.markdown("""
        ### 🧾 Demonstração de Resultados com Custeio Variável
        Compare com o custeio por absorção:
        """)

        receita = st.number_input("Receita Total (R$)", 50000, 200000, 100000, key="dre_receita")
        cv_total = st.number_input("Custos Variáveis Totais (R$)", 10000, 80000, 50000, key="dre_cv")
        cf_total = st.number_input("Custos Fixos Totais (R$)", 10000, 60000, 30000, key="dre_cf")

        mc = receita - cv_total
        lucro = mc - cf_total

        dre_df = pd.DataFrame({
            "Descrição": [
                "Receita",
                "(-) Custos Variáveis",
                "Margem de Contribuição",
                "(-) Custos Fixos",
                "Lucro Operacional"
            ],
            "Valor (R$)": [
                f"R$ {receita:,.2f}",
                f"-- R$ {cv_total:,.2f}",
                f"R$ {mc:,.2f}",
                f"-- R$ {cf_total:,.2f}",
                f"R$ {lucro:,.2f}"
            ]
        })

        st.table(dre_df)

        if lucro > 0:
            st.success("✅ Empresa lucrativa!")
        elif lucro == 0:
            st.info("🟡 Ponto de equilíbrio atingido.")
        else:
            st.warning("⚠️ Prejuízo operacional.")

    # ===========================
    # Expander 4: Análise CVL e Ponto de Equilíbrio
    # ===========================
    with st.expander("📉 4. Análise Custo-Volume-Lucro e Ponto de Equilíbrio", expanded=False):
        st.markdown("### 🎯 Ponto de Equilíbrio (Break-Even Point)")

        preco_pe = st.number_input("Preço Unitário (R$)", 10.0, 200.0, 50.0, key="pe_pv")
        cvu_pe = st.number_input("Custo Variável Unitário (R$)", 1.0, 150.0, 30.0, key="pe_cvu")
        cf_pe = st.number_input("Custos Fixos Totais (R$)", 1000, 50000, 20000, key="pe_cf")

        if preco_pe > cvu_pe:
            mc_pe = preco_pe - cvu_pe
            pe_qtde = cf_pe / mc_pe
            pe_receita = pe_qtde * preco_pe

            st.metric("Ponto de Equilíbrio (quantidade)", f"{pe_qtde:.0f} unidades")
            st.metric("Ponto de Equilíbrio (em receita)", f"R$ {pe_receita:,.2f}")

            # Gráfico de CVL
            q_range = np.linspace(0, pe_qtde * 2, 200)
            rt = preco_pe * q_range
            ct = cf_pe + cvu_pe * q_range
            lucro_linha = rt - ct

            fig, ax = plt.subplots(figsize=(8, 5))
            ax.plot(q_range, rt, label="Receita Total", color="green")
            ax.plot(q_range, ct, label="Custo Total", color="red")
            ax.plot(q_range, lucro_linha, label="Lucro", color="blue", linestyle="--")
            ax.axvline(x=pe_qtde, color="purple", linestyle=":", label="Ponto de Equilíbrio")
            ax.axhline(y=0, color="black", linewidth=0.8)
            ax.set_xlabel("Quantidade")
            ax.set_ylabel("R$")
            ax.legend()
            ax.grid(alpha=0.3)
            st.pyplot(fig)
        else:
            st.error("⚠️ O custo variável não pode ser maior ou igual ao preço de venda.")

    # ===========================
    # Expander 5: Margem de Segurança e Alavancagem
    # ===========================
    with st.expander("🛡️ 5. Margem de Segurança e Alavancagem Operacional", expanded=False):
        qtde_vendida = st.number_input("Quantidade Vendida Atual", min_value=1, value=1000, key="ms_qtde")
        pe_calc = cf_pe / (preco_pe - cvu_pe) if (preco_pe - cvu_pe) > 0 else 0

        if qtde_vendida > pe_calc:
            ms_percent = ((qtde_vendida - pe_calc) / qtde_vendida) * 100
            st.metric("Margem de Segurança", f"{ms_percent:.1f}%")
            st.progress(ms_percent / 100)
            st.info(f"A empresa pode reduzir as vendas em {ms_percent:.1f}% antes de entrar no prejuízo.")
        else:
            st.warning("⚠️ As vendas estão abaixo do ponto de equilíbrio.")

        # Alavancagem Operacional
        if mc > 0:
            alavancagem = mc / (mc - cf_total) if (mc - cf_total) != 0 else float('inf')
            if alavancagem > 0:
                st.metric("Alavancagem Operacional", f"{alavancagem:.2f}x")
                st.markdown(f"""
                - **Significado:** Um aumento de 1% nas vendas gera um aumento de **{alavancagem:.2f}% no lucro**.
                - Alta alavancagem = maior risco, mas maior retorno potencial.
                """)

    # ===========================
    # Expander 6: Tomada de Decisão
    # ===========================
    with st.expander("✅ 6. Tomada de Decisão com Custeio Gerencial", expanded=False):
        st.markdown(r"""
        ### 🧩 Exemplo: Aceitar um pedido especial?
        Um cliente oferece comprar 200 unidades a R\$ 45,00 cada.  
        Custo variável unitário: R\$ 30,00. Custo fixo não aumenta.  
        Capacidade ociosa disponível.
        """)

        decisao = st.radio(
            "Você aceitaria o pedido?",
            options=["Sim", "Não", "Depende"],
            key="decisao_pedido"
        )

        if st.button("💡 Mostrar Análise", key="analise_decisao"):
            receita_adicional = 200 * 45
            custo_adicional = 200 * 30
            mc_adicional = receita_adicional - custo_adicional

            st.write(f"- Receita adicional: R$ {receita_adicional:,.2f}")
            st.write(f"- Custo variável adicional: R$ {custo_adicional:,.2f}")
            st.write(f"- **Margem de Contribuição adicional: R$ {mc_adicional:,.2f}**")

            if decisao == "Sim":
                st.success("Correto! Como há capacidade ociosa e o preço > CVU, o pedido aumenta o lucro.")
            else:
                st.info("Reavalie: mesmo com preço baixo, se cobre o custo variável e não há custo fixo adicional, vale a pena.")

    # ===========================
    # Expander 7: Deficiências do Custeio por Absorção
    # ===========================
    with st.expander("⚠️ 7. Deficiências do Custeio por Absorção", expanded=False):
        st.markdown(r"""
        ### ❌ Por que o custeio por absorção pode atrapalhar decisões?
        - **Efeito do estoque:** lucro sobe com produção (mesmo sem venda)
        - **Máscara de rentabilidade:** produtos com alto custo fixo podem parecer menos lucrativos
        - **Decisões erradas:** pode levar à manutenção de produtos não viáveis

        📌 **Exemplo:**
        - Produção: 10.000 unidades, Vendas: 8.000 unidades
        - Custo fixo: R\$ 100.000 → R$ 10/unidade alocado
        - Lucro contábil: positivo (porque R\$ 20.000 de custo fixo estão no estoque)
        - Mas caixa não entrou!
        """)

        st.info("💡 O custeio variável mostra o fluxo real de contribuição, melhor para decisões de curto prazo.")

    # ===========================
    # Expander 8: Testes Interativos
    # ===========================
    with st.expander("📝 Teste seus Conhecimentos - Nível Intermediário", expanded=False):
        st.markdown("### 🧠 Avalie seu entendimento sobre custeio variável e análise gerencial:")
    
        questions = [
            {
                "question": "No custeio variável, como são tratados os custos fixos de fabricação?",
                "options": [
                    "Alocados aos produtos com base em horas máquina",
                    "Distribuídos entre os produtos vendidos",
                    "Tratados como despesa do período",
                    "Incluídos no custo dos estoques",
                    "Rateados entre departamentos"
                ],
                "correct": 2,
                "explanation": "No custeio variável, os custos fixos de fabricação **não são alocados aos produtos**, são tratados como despesas do período."
            },
            {
                "question": "O que representa a Margem de Contribuição (MC)?",
                "options": [
                    "Lucro líquido por unidade",
                    "Receita menos custos fixos",
                    "Receita menos custos variáveis",
                    "Custo variável total",
                    "Despesas operacionais"
                ],
                "correct": 2,
                "explanation": "MC = Receita - Custos Variáveis. Representa o valor disponível para cobrir custos fixos e gerar lucro."
            },
            {
                "question": "Qual é a principal vantagem do custeio variável em relação ao custeio por absorção?",
                "options": [
                    "Maior conformidade com a legislação fiscal",
                    "Melhor adequação às normas contábeis",
                    "Facilita decisões de curto prazo e análise CVL",
                    "Aumenta o lucro contábil",
                    "Reduz o imposto de renda"
                ],
                "correct": 2,
                "explanation": "O custeio variável é mais útil para **decisões gerenciais**, pois separa custos fixos e variáveis, facilitando análises de contribuição e ponto de equilíbrio."
            },
            {
                "question": "Em uma DRE com custeio variável, qual item aparece antes dos custos fixos?",
                "options": [
                    "Lucro operacional",
                    "Receita bruta",
                    "Custos fixos administrativos",
                    "Margem de Contribuição",
                    "Custo dos produtos vendidos"
                ],
                "correct": 3,
                "explanation": "A estrutura é: Receita → (-) Custos Variáveis → **Margem de Contribuição** → (-) Custos Fixos → Lucro."
            },
            {
                "question": "O que acontece com o lucro no custeio por absorção quando a produção excede as vendas?",
                "options": [
                    "Diminui, pois há mais custos",
                    "Permanece constante",
                    "Aumenta, pois parte dos custos fixos vai para o estoque",
                    "Torna-se negativo",
                    "Depende do custo variável"
                ],
                "correct": 2,
                "explanation": "No custeio por absorção, custos fixos são alocados aos produtos. Se houver estoque, parte dos custos fixos é **adiada para o futuro**, aumentando o lucro contábil do período."
            },
            {
                "question": "Como é calculado o ponto de equilíbrio em unidades?",
                "options": [
                    "Custos Fixos / Preço de Venda",
                    "Custos Variáveis / Margem de Contribuição Unitária",
                    "Custos Fixos / Margem de Contribuição Unitária",
                    "Receita / Custos Totais",
                    "Lucro / Custo Variável Unitário"
                ],
                "correct": 2,
                "explanation": "Ponto de equilíbrio (unidades) = CF / (PV - CVU) = CF / MC unitária."
            },
            {
                "question": "Se o preço de venda é R\\$ 80, o custo variável é R\\$ 50 e os custos fixos são R\\$ 30.000, qual é o ponto de equilíbrio?",
                "options": [
                    "600 unidades",
                    "750 unidades",
                    "1.000 unidades",
                    "1.200 unidades",
                    "1.500 unidades"
                ],
                "correct": 2,  # 30000 / (80-50) = 1000
                "explanation": "MC unitária = R\\$ 30. PE = 30.000 / 30 = **1.000 unidades**."
            },
            {
                "question": "Qual é a fórmula da margem de segurança?",
                "options": [
                    "(Vendas reais - Vendas planejadas) / Vendas reais",
                    "(Vendas atuais - Ponto de equilíbrio) / Vendas atuais",
                    "Vendas atuais / Ponto de equilíbrio",
                    "Ponto de equilíbrio / Vendas atuais",
                    "Lucro / Custos Fixos"
                ],
                "correct": 1,
                "explanation": "Margem de segurança = (Vendas atuais - Vendas no PE) / Vendas atuais. Mostra quanto as vendas podem cair sem prejuízo."
            },
            {
                "question": "Um produto tem MC de R\\$ 40.000 e lucro de R\\$ 10.000. Qual é a alavancagem operacional?",
                "options": [
                    "2x",
                    "3x",
                    "4x",
                    "5x",
                    "6x"
                ],
                "correct": 2,  # 40.000 / 10.000 = 4
                "explanation": "Alavancagem = MC / Lucro = 40.000 / 10.000 = **4x**. Um aumento de 1% nas vendas gera 4% de aumento no lucro."
            },
            {
                "question": "Por que o custeio por absorção pode levar a decisões erradas?",
                "options": [
                    "Porque não considera custos variáveis",
                    "Porque subestima o custo dos produtos",
                    "Porque pode incentivar superprodução para inflar o lucro",
                    "Porque é mais caro de implementar",
                    "Porque não é aceito pela Receita Federal"
                ],
                "correct": 2,
                "explanation": "Ao alocar custos fixos aos produtos, o custeio por absorção pode **inflar o lucro com aumento de estoque**, levando a decisões de produção inadequadas."
            }
        ]
    
        if 'quiz_answers_part1' not in st.session_state:
            st.session_state.quiz_answers_part1 = [None] * len(questions)
    
        user_score = 0
        for i, q in enumerate(questions):
            st.markdown(f"**{i+1}. {q['question']}**")
            user_answer = st.radio(
                q["question"],
                options=q["options"],
                key=f"quiz1_q{i}",
                index=st.session_state.quiz_answers_part1[i] if st.session_state.quiz_answers_part1[i] is not None else None
            )
            st.session_state.quiz_answers_part1[i] = q["options"].index(user_answer) if user_answer else None
    
            if user_answer:
                if q["options"].index(user_answer) == q["correct"]:
                    st.success("✅ Correto!")
                    user_score += 1
                else:
                    st.error(f"❌ Incorreto. A resposta correta é: **{q['options'][q['correct']]}**.")
                    with st.expander("📘 Explicação"):
                        st.markdown(q["explanation"])
    
        if all(ans is not None for ans in st.session_state.quiz_answers_part1):
            st.markdown("---")
            st.markdown(f"### 🎯 Pontuação: **{user_score}/{len(questions)}**")
            if user_score >= 9:
                st.balloons()
                st.success("🎉 Excelente! Você domina os conceitos de custeio gerencial!")
            elif user_score >= 6:
                st.success("👍 Bom desempenho!")
            else:
                st.warning("📚 Revise os tópicos. Os expanders anteriores podem ajudar.")
    
    # ===========================
    # Expander 9: Testes Interativos – Parte 2 (avançado)
    # ===========================
    with st.expander("🧠 Testes Avançados (Aplicação e Decisão)", expanded=False):
        st.markdown("### 🔍 Aprofunde seu conhecimento com questões de aplicação prática:")
    
        questions = [
            {
                "question": "Uma empresa tem MC de R\$ 100.000 e custos fixos de R\\$ 70.000. Qual é o lucro operacional?",
                "options": [
                    "R\\$ 170.000",
                    "R\\$ 100.000",
                    "R\\$ 70.000",
                    "R\\$ 30.000",
                    "R\\$ 0"
                ],
                "correct": 3,  # 100k - 70k = 30k
                "explanation": "Lucro = MC - CF = 100.000 - 70.000 = R\\$ 30.000."
            },
            {
                "question": "Se a margem de segurança é 25% e as vendas atuais são 8.000 unidades, qual é o ponto de equilíbrio?",
                "options": [
                    "2.000 unidades",
                    "4.000 unidades",
                    "6.000 unidades",
                    "7.000 unidades",
                    "8.000 unidades"
                ],
                "correct": 2,  # 8000 - (0.25*8000) = 6000
                "explanation": "MS = 25% → PE = 75% das vendas → 0.75 × 8.000 = **6.000 unidades**."
            },
            {
                "question": "Um produto tem alavancagem operacional de 5x. Se as vendas aumentarem 10%, quanto aumentará o lucro?",
                "options": [
                    "10%",
                    "20%",
                    "30%",
                    "40%",
                    "50%"
                ],
                "correct": 4,  # 5 × 10% = 50%
                "explanation": "Alavancagem de 5x significa que o lucro varia 5 vezes mais que as vendas: 5 × 10% = **50%**."
            },
            {
                "question": "Em qual situação o custeio variável é mais apropriado?",
                "options": [
                    "Para apuração de imposto de renda",
                    "Para demonstrações financeiras externas",
                    "Para análise de mix de produtos e decisões de curto prazo",
                    "Para controle de estoque em armazém",
                    "Para auditoria fiscal"
                ],
                "correct": 2,
                "explanation": "O custeio variável é ideal para **decisões internas**, como análise de mix, preço mínimo, aceitação de pedidos especiais, etc."
            },
            {
                "question": "Um pedido especial oferece vender 1.000 unidades a R\\$ 25. O custo variável é R\\$ 20. Custos fixos não aumentam. Você aceita?",
                "options": [
                    "Não, porque é abaixo do preço normal",
                    "Não, porque reduz a margem",
                    "Sim, se houver capacidade ociosa",
                    "Sim, mesmo com capacidade cheia",
                    "Depende do custo fixo"
                ],
                "correct": 2,
                "explanation": "Se há capacidade ociosa, qualquer preço acima do CVU (R\\$ 20) gera **MC adicional**. R\\$ 25 > R\$ 20 → **aceitar**."
            },
            {
                "question": "Qual é a principal desvantagem do custeio por absorção na análise de lucratividade por produto?",
                "options": [
                    "É mais complexo de calcular",
                    "Subestima os custos variáveis",
                    "Pode alocar custos fixos de forma arbitrária, distorcendo a rentabilidade",
                    "Não considera despesas administrativas",
                    "Exige software especializado"
                ],
                "correct": 2,
                "explanation": "A alocação de custos fixos pode fazer produtos com baixa demanda parecerem menos lucrativos do que realmente são."
            },
            {
                "question": "A MC unitária é R\\$ 15. O CF total é R\\$ 60.000. Qual é o PE em unidades?",
                "options": [
                    "3.000",
                    "4.000",
                    "5.000",
                    "6.000",
                    "7.000"
                ],
                "correct": 1,  # 60.000 / 15 = 4.000
                "explanation": "PE = CF / MC unitária = 60.000 / 15 = **4.000 unidades**."
            },
            {
                "question": "Se o PE é 1.200 unidades e as vendas são 1.500, qual é a margem de segurança?",
                "options": [
                    "10%",
                    "15%",
                    "20%",
                    "25%",
                    "30%"
                ],
                "correct": 3,  # (1500-1200)/1500 = 300/1500 = 20%
                "explanation": "(1.500 - 1.200) / 1.500 = 300 / 1.500 = **20%**."
            },
            {
                "question": "O que acontece com a MC se o custo variável unitário aumentar?",
                "options": [
                    "Aumenta",
                    "Permanece constante",
                    "Diminui",
                    "Torna-se negativa",
                    "Depende do preço"
                ],
                "correct": 2,
                "explanation": "MC = PV - CVU. Se CVU aumenta, MC **diminui**, reduzindo a capacidade de cobrir custos fixos."
            },
            {
                "question": "Por que a análise CVL é importante para o gestor?",
                "options": [
                    "Para calcular o imposto de renda",
                    "Para determinar o estoque de segurança",
                    "Para entender o impacto de mudanças no volume sobre o lucro",
                    "Para avaliar o desempenho do RH",
                    "Para prever a inflação"
                ],
                "correct": 2,
                "explanation": "A análise CVL mostra como variações no volume de vendas afetam custos e lucros, essencial para planejamento."
            }
        ]
    
        if 'quiz_answers_part2' not in st.session_state:
            st.session_state.quiz_answers_part2 = [None] * len(questions)
    
        user_score = 0
        for i, q in enumerate(questions):
            st.markdown(f"**{i+1}. {q['question']}**")
            user_answer = st.radio(
                q["question"],
                options=q["options"],
                key=f"quiz2_q{i}",
                index=st.session_state.quiz_answers_part2[i] if st.session_state.quiz_answers_part2[i] is not None else None
            )
            st.session_state.quiz_answers_part2[i] = q["options"].index(user_answer) if user_answer else None
    
            if user_answer:
                if q["options"].index(user_answer) == q["correct"]:
                    st.success("✅ Correto!")
                    user_score += 1
                else:
                    st.error(f"❌ Incorreto. A resposta correta é: **{q['options'][q['correct']]}**.")
                    with st.expander("📘 Explicação"):
                        st.markdown(q["explanation"])
    
        if all(ans is not None for ans in st.session_state.quiz_answers_part2):
            st.markdown("---")
            st.markdown(f"### 🎯 Pontuação: **{user_score}/{len(questions)}**")
            if user_score >= 9:
                st.balloons()
                st.success("🎉 Parabéns! Excelente domínio da análise gerencial!")
            elif user_score >= 6:
                st.success("👍 Bom trabalho!")
            else:
                st.warning("📚 Revise os conceitos com os materiais anteriores.")
                
    # ===========================
    # Final: Próxima Etapa
    # ===========================
    st.divider()
    st.markdown("✅ Parabéns! Você completou a análise interativa de Custeio Variável.")

    if st.button("👉 Avançar para o próximo tópico: Precificação a partir do custo"):
        st.switch_page("pages/5_💰_Precificacao.py")

if __name__ == "__main__":
    main()
