#pip install soundfile numpy scipy
import soundfile as sf
import numpy as np

audio, sr = sf.read("preview.mp3")
peak = np.max(np.abs(audio))

print("Before")
print("Peak:", peak)

target = 10 ** (-1 / 20) 
gain = target / peak

normalized = audio * gain

print("After")
print("Peak:", np.max(np.abs(normalized)))

sf.write(r"C:\Users\Aunyone\Downloads\Normalized.wav", normalized, sr)
