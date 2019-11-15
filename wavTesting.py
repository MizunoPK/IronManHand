import matplotlib.pyplot as plt
from scipy.io import wavfile as wv

samplerate, data = wv.read("blastSound.wav")
print(samplerate)
print(data.shape)