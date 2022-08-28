import wave
import matplotlib.pyplot as plt
import numpy as np

# Open wav file
obj = wave.open("data/experimental/StarWars3.wav", 'rb')
# Read frames
signal_wave = obj.readframes(-1)
# Get number of frames
n_frames = obj.getnframes()
# Get frame rate
frame_rate = obj.getframerate()
obj.close()
# Get time duration
t = n_frames/frame_rate

x = np.linspace(0, t, num=n_frames) 
y = np.frombuffer(signal_wave, dtype='int16')

plt.figure(figsize=(15, 7))
plt.plot(x, y)
plt.xlim(0, t)
plt.title("Audio signal")
plt.xlabel("Sample value")
plt.ylabel("Time (sec)")
plt.show()