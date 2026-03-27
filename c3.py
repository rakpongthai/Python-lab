import librosa
import numpy as np
import soundfile as sf

y, sr = librosa.load("preview.mp3", sr=None)
intervals = librosa.effects.split(y, top_db=40)
y_trimmed = np.concatenate([y[start:end] for start, end in intervals])

print("Before:", len(y)/sr)
print("After:", len(y_trimmed)/sr)

sf.write("trimmed.wav", y_trimmed, sr)
