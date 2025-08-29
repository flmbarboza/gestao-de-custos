import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from utils import leitor_de_texto, get_anon_user_id, log_acesso_google, log_interacao_google, safe_log_interacao

def main():
    st.title("📈 Custeio por Absorção - Avançado")
    st.markdown("""
    **Departamentalização e critérios de rateio**  
    *Distribuição científica dos custos indiretos por centros de custo e produtos*
    """)
    # Recupera o nome do usuário
    nome_usuario = get_anon_user_id()
    pagina_atual = "Custeio Abs II"
    
    # Registra o acesso
    if 'page31_acessada' not in st.session_state:
        log_acesso_google(nome_usuario, pagina_atual, f"acessou_{pagina_atual}")
        st.session_state.page31_acessada = True
    
    # Divisão em abas para diferentes métodos
    tab1, tab2, tab3 = st.tabs(["🏭 Rateio por Departamentos", "📊 Rateio por Produtos", "🧮 Cálculo Taxa CIF"])
    
    with tab1:
        st.header("Método de Departamentalização")
        st.subheader("Dados de Entrada")
        deptos = pd.DataFrame({
            'Departamento': ['Montagem', 'Acabamento', 'Administração'],
            'Custo Direto': [120000, 80000, 50000],
            'Horas-Mod': [3000, 2000, 1000],
            'Horas-Máquina': [1500, 1000, 500],
            'Área (m²)': [800, 600, 400]
        })
        edited_deptos = st.data_editor(deptos, num_rows="dynamic")
        
        criterio = st.selectbox(
            "Critério de Rateio:",
            ["Horas-Máquina", "Horas-MOD", "Área", "Custo Direto"],
            key="depto"
        )
    
        st.subheader("Resultado do Rateio")
        if st.button("Calcular Rateio", key="calc_depto"):
            total_cif = st.number_input("Total CIF a Ratear (R$):", value=150000)
            
            if criterio == "Horas-Máquina":
                base = edited_deptos['Horas-Máquina'].sum()
                edited_deptos['% Rateio'] = edited_deptos['Horas-Máquina'] / base
            elif criterio == "Horas-MOD":
                base = edited_deptos['Horas-Mod'].sum()
                edited_deptos['% Rateio'] = edited_deptos['Horas-Mod'] / base
            elif criterio == "Área":
                base = edited_deptos['Área (m²)'].sum()
                edited_deptos['% Rateio'] = edited_deptos['Área (m²)'] / base
            else:
                base = edited_deptos['Custo Direto'].sum()
                edited_deptos['% Rateio'] = edited_deptos['Custo Direto'] / base
            
            edited_deptos['CIF Rateado'] = edited_deptos['% Rateio'] * total_cif
            edited_deptos['Custo Total'] = edited_deptos['Custo Direto'] + edited_deptos['CIF Rateado']
            
            st.dataframe(edited_deptos.style.format({
                '% Rateio': '{:.1%}',
                'CIF Rateado': 'R$ {:,.2f}',
                'Custo Total': 'R$ {:,.2f}'
            }))
            
            # Gráfico de composição
            fig = px.pie(edited_deptos, values='CIF Rateado', names='Departamento',
                        title='Distribuição do CIF por Departamento')
            st.plotly_chart(fig, use_container_width=True)
    
    with tab2:
        st.header("Rateio por Linha de Produtos")
        
        produtos = pd.DataFrame({
            'Produto': ['Cadeira', 'Mesa', 'Armário'],
            'Unidades Produzidas': [500, 300, 200],
            'Horas-MOD': [2000, 1500, 1000],
            'MP Consumida': [40000, 35000, 25000]
        })
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Dados de Produção")
            edited_prod = st.data_editor(produtos, num_rows="dynamic")
            
            criterio_prod = st.selectbox(
                "Critério de Rateio:",
                ["Unidades", "Horas-MOD", "MP Consumida"],
                key="prod"
            )
            
            cif_total = st.number_input("Total CIF (R$):", value=90000, key="cif_prod")
        
        with col2:
            st.subheader("Custo Unitário por Produto")
            if st.button("Calcular Rateio", key="calc_prod"):
                if criterio_prod == "Unidades":
                    base = edited_prod['Unidades Produzidas'].sum()
                    edited_prod['% Rateio'] = edited_prod['Unidades Produzidas'] / base
                elif criterio_prod == "Horas-MOD":
                    base = edited_prod['Horas-MOD'].sum()
                    edited_prod['% Rateio'] = edited_prod['Horas-MOD'] / base
                else:
                    base = edited_prod['MP Consumida'].sum()
                    edited_prod['% Rateio'] = edited_prod['MP Consumida'] / base
                
                edited_prod['CIF Rateado'] = edited_prod['% Rateio'] * cif_total
                edited_prod['Custo Unitário'] = (edited_prod['MP Consumida'] + edited_prod['Horas-MOD'] * 25 + edited_prod['CIF Rateado']) / edited_prod['Unidades Produzidas']
                
                st.dataframe(edited_prod.style.format({
                    '% Rateio': '{:.1%}',
                    'CIF Rateado': 'R$ {:,.2f}',
                    'Custo Unitário': 'R$ {:,.2f}'
                }))
                
                # Gráfico comparativo
                fig = px.bar(edited_prod, x='Produto', y='Custo Unitário',
                            title='Custo Unitário por Produto',
                            text_auto='.2f')
                st.plotly_chart(fig, use_container_width=True)
    
    with tab3:
        st.header("Taxa de Aplicação de CIF")
        
        st.markdown("""
        **Fórmula:**  
        `Taxa CIF = (CIF Total / Base de Rateio) × 100`  
        *Onde a base pode ser horas-máquina, MOD, etc.*
        """)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Cálculo da Taxa")
            cif_total = st.number_input("CIF Total (R$):", value=180000)
            base_rateio = st.number_input("Base de Rateio (ex: horas-máquina):", value=3000)
            st.metric("Taxa de Aplicação", f"R$ {cif_total/base_rateio:,.2f} por unidade de base")
            
            st.subheader("Aplicação Prática")
            horas_produto = st.number_input("Horas consumidas pelo produto:", value=150)
            st.metric("CIF Alocado", f"R$ {(cif_total/base_rateio)*horas_produto:,.2f}")
        
        with col2:
            st.subheader("Exemplo Real")
            st.write("**Indústria Automobilística**")
            st.markdown("""
            - CIF Anual: R$ 12.000.000  
            - Horas-Máquina Anuais: 24.000  
            - Taxa: R$ 500/hora-máquina  
            - Carro X usa 8 horas: R$ 4.000 de CIF
            """)
            
            st.write("**Fábrica de Móveis**")
            st.markdown("""
            - CIF Mensal: R$ 150.000  
            - MOD Mensal: R$ 300.000  
            - Taxa: 50% da MOD  
            - Mesa com R$ 800 MOD: R$ 400 CIF
            """)
    
    # Rodapé com navegação
    st.divider()
    col1, col2 = st.columns(2)
    with col1:
        if st.button("⬅️ Voltar para Custeio por Absorção I"):
            st.switch_page("pages/3_📊_Custeio_por_Absorcao_I.py")

    with col2:
        if st.button("Avançar para Custeio Variável ➡️"):
            st.switch_page("pages/4_📈_Custeio_Variavel.py")

if __name__ == "__main__":
    main()
