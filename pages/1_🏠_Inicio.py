import streamlit as st
from utils import leitor_de_texto

def main():
    st.title("🏦 Gestão de Custos - FAGEN/UFU")
    
    # Texto de boas-vindas
    texto_boas_vindas = """
    Bem-vindo à plataforma interativa da disciplina Gestão de Custos. Aqui você aprenderá:
    - Os fundamentos da contabilidade de custos
    - Métodos de custeio (absorção e variável)
    - Técnicas de precificação
    - Análise de margem de contribuição
    - E muito mais!
    """
    st.markdown(texto_boas_vindas)
    
    # Seção de objetivos
    with st.expander("🎯 Objetivos da Disciplina", expanded=True):
        st.markdown("""
        - Apresentar conceitos de registro, apuração e controle de custos
        - Fornecer visão ampla da contabilidade financeira e gerencial
        - Analisar impactos tributários em custos e preços
        - Desenvolver habilidades para tomada de decisão com restrições
        """)
    
    # Ementa interativa
    st.subheader("📚 Programa da Disciplina")
    cols = st.columns(3)
    unidades = [
        ("1️⃣ Introdução à Contabilidade de Custos", "Terminologia, Classificação e Comportamento de Custos"),
        ("2️⃣ Custeio por Absorção", "CPP, CPA, CPV, Rateio de CIF, DRE"),
        ("3️⃣ Custeio Variável", "Margem de Contribuição, Ponto de Equilíbrio"),
        ("4️⃣ Precificação", "Método Mark-up, Impacto Tributário"),
        ("5️⃣ Margem de Contribuição", "Limitações na Capacidade Produtiva")
    ]
    
    for i, (unidade, desc) in enumerate(unidades):
        cols[i%3].button(
            f"{unidade}",
            help=desc,
            use_container_width=True
        )
    
    # Botão de áudio
#    if st.button("🎧 Ouvir Apresentação"):
 #       texto_audio = texto_boas_vindas + "\nObjetivos: " + " ".join([
  #          "Apresentar conceitos, ",
   #         "Fornecer visão ampla, ",
    #        "Analisar impact

if __name__ == "__main__":
    main()
