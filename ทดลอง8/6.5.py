
import librosa
import librosa.display
import matplotlib.pyplot as plt

y, sr = librosa.load("preview.mp3", sr=None)

plt.figure(figsize=(12, 4))
librosa.display.waveshow(y, sr=sr)
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.title("Waveform of dog Voice Sound")
plt.show()
