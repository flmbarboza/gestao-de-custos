import gtts
from io import BytesIO
import streamlit as st
import base64
import pandas as pd
import csv
import os
from datetime import datetime
import gspread

# Função para conectar ao Google Sheets
def conectar_planilha():
    if 'gc' not in st.session_state:
        try:
            # Usa os secrets do Streamlit
            from streamlit import secrets
            gc = gspread.service_account_from_dict(secrets["gspread"])
            st.session_state.gc = gc
        except Exception as e:
            st.error(f"Erro ao conectar ao Google Sheets: {e}")
            return None
    return st.session_state.gc

# Função para logar acessos no Google Sheets
def log_acesso_google(nome, email, pagina):
    gc = conectar_planilha()
    if not gc:
        return
    try:
        planilha = gc.open("Logs-gestao-custos")  # Nome da planilha
        worksheet = planilha.worksheet("Acessos")   # Aba "Acessos"

        worksheet.append_row([
            nome,
            email or "anonimo",
            pagina,
            str(datetime.now())
        ])
    except Exception as e:
        st.warning(f"Erro ao salvar no Google Sheets (acesso): {e}")

# Função para logar interações no Google Sheets
def log_interacao_google(nome, pagina, acao):
    gc = conectar_planilha()
    if not gc:
        return
    try:
        planilha = gc.open("Logs-gestao-custos")
        worksheet = planilha.worksheet("Interações")  # Aba "Interações"

        worksheet.append_row([
            nome,
            pagina,
            acao,
            str(datetime.now())
        ])
    except Exception as e:
        st.warning(f"Erro ao salvar no Google Sheets (interação): {e}")

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

def inicializar_log_interacoes():
    """Cria o arquivo de log se não existir"""
    if not os.path.exists("log_interacoes.csv"):
        with open("log_interacoes.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["nome", "pagina", "acao", "timestamp"])

def log_interacao(nome, pagina, acao):
    """Registra uma interação no CSV"""
    try:
        with open("log_interacoes.csv", "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([nome, pagina, acao, datetime.now()])
    except Exception as e:
        st.warning(f"Erro ao salvar interação: {e}")
