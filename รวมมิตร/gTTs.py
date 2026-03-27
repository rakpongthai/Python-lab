# =========================
# 1. ติดตั้ง (รันใน terminal)
# =========================
# pip install gTTS
# pip install playsound
# pip install sounddevice
# pip install numpy scipy
# pip install librosa matplotlib

# =========================
# 2. TEXT TO SPEECH (gTTS)
# =========================
from gtts import gTTS

# อังกฤษ
tts = gTTS('hello world', lang='en')
tts.save('hello.mp3')

# ไทย
text_th = "สวัสดี นี่คือการทดลองแปลงข้อความเป็นเสียง"
tts_th = gTTS(text_th, lang='th')
tts_th.save('thai.mp3')


# =========================
# 3. อ่านไฟล์ txt → เสียง
# =========================
with open("THsong.txt", "r", encoding="utf-8") as f:
    text = f.read()

tts = gTTS(text, lang='th')
tts.save("THsong.mp3")


# =========================
# 4. เล่นเสียง (playsound)
# =========================
from playsound import playsound

playsound("hello.mp3")


# =========================
# 5. อัดเสียง (SoundDevice)
# =========================
import sounddevice as sd
from scipy.io.wavfile import write

duration = 10      # ระยะเวลา (วินาที)
fs = 44100         # ความถี่เสียง

print("กำลังอัดเสียง...")
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=2)

sd.wait()  # รอจนบันทึกเสร็จ
write('record.wav', fs, myrecording)

print("บันทึกเสร็จแล้ว")

# เล่นเสียงที่อัด
sd.play(myrecording, fs)
sd.wait()


# =========================
# 6. วิเคราะห์เสียง (Librosa)
# =========================
import librosa
import matplotlib.pyplot as plt

# โหลดไฟล์เสียง
y, sr = librosa.load('hello.mp3')

print("Sampling rate:", sr)
print("Signal:", y)

# plot waveform
plt.plot(y)
plt.title("Signal")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()


# =========================
# 7. แสดง Spectrogram (ความถี่)
# =========================
import librosa.display
import numpy as np

D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

plt.figure(figsize=(10, 4))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title('Spectrogram')
plt.show()


import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
import os

# =========================
# โหลดไฟล์เสียง
# =========================
file = "hello.mp3"
y, sr = librosa.load(file)

# =========================
# 1. ข้อมูลพื้นฐาน
# =========================
print("ชื่อไฟล์:", file)
print("Sampling rate:", sr)
print("จำนวน sample:", len(y))

duration = librosa.get_duration(y=y, sr=sr)
print("ความยาวเสียง (วินาที):", duration)

# =========================
# 2. ขนาดไฟล์
# =========================
size = os.path.getsize(file) / 1024
print("ขนาดไฟล์ (KB):", size)

# =========================
# 3. Waveform (รูปคลื่นเสียง)
# =========================
plt.figure(figsize=(10,4))
librosa.display.waveshow(y, sr=sr)
plt.title("Waveform")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()

# =========================
# 4. Spectrogram (ความถี่)
# =========================
D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)

plt.figure(figsize=(10,4))
librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log')
plt.colorbar(format='%+2.0f dB')
plt.title("Spectrogram")
plt.show()

# =========================
# 5. ความถี่พื้นฐาน (Pitch)
# =========================
pitches, magnitudes = librosa.piptrack(y=y, sr=sr)

pitch_values = pitches[magnitudes > np.median(magnitudes)]
print("ค่า Pitch โดยประมาณ:", np.mean(pitch_values))

# =========================
# 6. Zero Crossing Rate (ลักษณะเสียง)
# =========================
zcr = librosa.feature.zero_crossing_rate(y)
print("Zero Crossing Rate:", np.mean(zcr))

# =========================
# 7. MFCC (Feature เสียง)
# =========================
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

plt.figure(figsize=(10,4))
librosa.display.specshow(mfcc, sr=sr, x_axis='time')
plt.colorbar()
plt.title("MFCC")
plt.show()
