'''
pip install gtts
pip install playsound
pip install pygame

#1
from gtts import gTTS
from datetime import datetime
import playsound

name = input("ชื่อ: ")
now = datetime.now()

text = f"สวัสดีคุณ{name} วันนี้เป็นวันเกิดของคุณ ขอให้มีความสุขมากๆ"

tts = gTTS(text=text, lang='th')
tts.save("birthday.mp3")

playsound.playsound("birthday.mp3")


#2
from gtts import gTTS
import pygame

name = input("กรอกชื่อ: ")

text = f"สวัสดีคุณ{name} วันนี้เป็นวันครบรอบวันเกิดของคุณ ขอให้คุณมีความสุขมากมากนะครับ"

tts = gTTS(text=text, lang='th')
tts.save("birthday.mp3")

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load("birthday.mp3")
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    continue
'''
#3
from gtts import gTTS
from datetime import datetime
import os

name = input("กรอกชื่อ: ")
now = datetime.now()

text = f"สวัสดีคุณ{name} วันนี้เป็นวันครบรอบวันเกิดของคุณ ขอให้คุณมีความสุขมากมากนะครับ"

tts = gTTS(text=text, lang='th')
tts.save("birthday.mp3")

print("บันทึกไฟล์เสียงแล้ว: birthday.mp3")

os.startfile("birthday.mp3")   # ใช้ได้บน Windows
