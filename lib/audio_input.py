import pyaudio


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
