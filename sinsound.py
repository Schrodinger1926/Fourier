from __future__ import division
import pyaudio
import numpy as np

p = pyaudio.PyAudio()

volume = 1     # range [0.0, 1.0]
fs = 44100       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

# generate samples, note conversion to float32 array
octave = [0, 2, 3, 5, 7, 8, 10, 12]
for i in octave:
	samples = (np.sin(2*np.pi*np.arange(fs*duration)*f*(2**(i/12))/fs)).astype(np.float32)

	# for paFloat32 sample values must be in range [-1.0, 1.0]
	stream = p.open(format=pyaudio.paFloat32,
	                channels=1,
	                rate=fs,
	                output=True)

	# play. May repeat with different volume values (if done interactively) 
	stream.write(volume*samples)

	stream.stop_stream()
	stream.close()

p.terminate()
