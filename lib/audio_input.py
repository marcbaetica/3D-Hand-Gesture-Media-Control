import pyaudio
import wave
from bokeh.plotting import figure, show


port_audio = pyaudio.PyAudio()

stream = port_audio.open(rate=44100,
                         channels=1,
                         format=pyaudio.paInt24,
                         input=True,
                         frames_per_buffer=1024)
print('Recording!')

frames = []

for i in range(int(44100/1024*2)):
    frames.append(stream.read(1024))

print('Done recording!')
port_audio.terminate()

with wave.open('recording.wav', 'wb') as wave_writer:
    wave_writer.setnchannels(1)
    wave_writer.setsampwidth(port_audio.get_sample_size(pyaudio.paInt24))
    wave_writer.setframerate(44100)
    wave_writer.writeframes(b''.join(frames))


y = list(range(len(frames)))
# print(frames[2])
# print(frames[2].decode('latin-1'))

p = figure()
p.vbar(x=frames, top=y, width=0.8)
show(p)  # Ignored in bokeh serve call. Will only render in run. Will not render if saving to file is called.