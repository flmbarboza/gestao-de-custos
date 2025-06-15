import gtts
from io import BytesIO

def leitor_de_texto(texto):
    tts = gtts.gTTS(texto, lang='pt-br')
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)
    return audio_bytes
