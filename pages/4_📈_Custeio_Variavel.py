import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
    st.title("📈 Custeio Variável (Gerencial) – Aprendizado Interativo")

    st.markdown("""
    Bem-vindo à análise interativa do **Custeio Variável**!  
    Aqui você vai entender como esse método auxilia na **tomada de decisões gerenciais**, com simulações, exercícios e comparações práticas.
    """)

    # ===========================
    # Expander 1: Método de Custeio Gerencial
    # ===========================
    with st.expander("🔍 1. Método de Custeio Gerencial", expanded=True):
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
    with st.expander("📊 2. Margem de Contribuição"):
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
    with st.expander("📑 3. Elaboração de DRE com Custeio Gerencial"):
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
                f"- R$ {cv_total:,.2f}",
                f"R$ {mc:,.2f}",
                f"- R$ {cf_total:,.2f}",
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
    with st.expander("📉 4. Análise Custo-Volume-Lucro e Ponto de Equilíbrio"):
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
    with st.expander("🛡️ 5. Margem de Segurança e Alavancagem Operacional"):
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
    with st.expander("✅ 6. Tomada de Decisão com Custeio Gerencial"):
        st.markdown("""
        ### 🧩 Exemplo: Aceitar um pedido especial?
        Um cliente oferece comprar 200 unidades a R$ 45,00 cada.  
        Custo variável unitário: R$ 30,00. Custo fixo não aumenta.  
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
    with st.expander("⚠️ 7. Deficiências do Custeio por Absorção"):
        st.markdown("""
        ### ❌ Por que o custeio por absorção pode atrapalhar decisões?
        - **Efeito do estoque:** lucro sobe com produção (mesmo sem venda)
        - **Máscara de rentabilidade:** produtos com alto custo fixo podem parecer menos lucrativos
        - **Decisões erradas:** pode levar à manutenção de produtos não viáveis

        📌 **Exemplo:**
        - Produção: 10.000 unidades, Vendas: 8.000 unidades
        - Custo fixo: R$ 100.000 → R$ 10/unidade alocado
        - Lucro contábil: positivo (porque R$ 20.000 de custo fixo estão no estoque)
        - Mas caixa não entrou!
        """)

        st.info("💡 O custeio variável mostra o fluxo real de contribuição, melhor para decisões de curto prazo.")

    # ===========================
    # Final: Próxima Etapa
    # ===========================
    st.divider()
    st.markdown("✅ Parabéns! Você completou a análise interativa de Custeio Variável.")

    if st.button("👉 Avançar para o próximo tópico: Precificação a partir do custo"):
        st.switch_page("pages/5_💰_Precificacao.py")

if __name__ == "__main__":
    main()
