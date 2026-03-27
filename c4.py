import numpy as np
import librosa

y, sr = librosa.load("preview.mp3", sr=None)

frame_length = int(0.02 * sr)
energy = []

for i in range(0, len(y), frame_length):
    frame = y[i:i+frame_length]
    energy.append(np.sum(frame**2))

threshold = np.mean(energy)

for i,e in enumerate(energy):
    if e > threshold:
        start = i*0.02
        end = start+0.02
        print("Time:", start, "-", end)
