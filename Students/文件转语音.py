
import asyncio
import edge_tts
from docx import Document
VOICE = "zh-CN-YunjianNeural"
# VOICE = "es-CL-LorenzoNeural"
async def word_2_voice(txt_path,voice_path):
    document = Document(txt_path)
    all_paragraphs = document.paragraphs
    txt=''
    for paragraph in all_paragraphs:
        txt=txt+paragraph.text+'\n'
    communicate = edge_tts.Communicate(txt, VOICE)
    await communicate.save(voice_path)

asyncio.run(word_2_voice("F:\\背影.docx" ,"F:\\背影.mp3"))
