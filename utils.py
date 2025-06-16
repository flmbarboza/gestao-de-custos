import gtts
from io import BytesIO
import streamlit as st
import base64

def leitor_de_texto(texto, lang='pt-br'):
    """
    Converte texto em áudio e reproduz no navegador
    Parâmetros:
    - texto (str): Texto a ser convertido
    - lang (str): Idioma (padrão 'pt-br' para português brasileiro)
    """
    try:
        # Cria o objeto de conversão texto-para-voz
        tts = gtts.gTTS(texto, lang=lang)
        
        # Salva o áudio em um buffer de memória
        audio_bytes = BytesIO()
        tts.write_to_fp(audio_bytes)
        audio_bytes.seek(0)
        
        # Converte para base64 para embed no HTML
        audio_base64 = base64.b64encode(audio_bytes.read()).decode()
        audio_html = f"""
        <audio autoplay controls>
        <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        Seu navegador não suporta o elemento de áudio.
        </audio>
        """
        
        # Exibe o player de áudio
        st.components.v1.html(audio_html, height=50)
        
    except Exception as e:
        st.error(f"Erro ao gerar áudio: {str(e)}")


def formatar_moeda(valor):
    """Formata valores como moeda brasileira"""
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
