import pyaudio
import wave


def record_audio(sample_frequency, bit_rate, audio_channels):
    port_audio = pyaudio.PyAudio()

    stream = port_audio.open(rate=sample_frequency,
                             channels=audio_channels,
                             format=pyaudio.paInt16,
                             input=True,
                             frames_per_buffer=1024)
    print('Recording!')

    frames = []

    for i in range(int(44100/1024*2)):
        frames.append(stream.read(1024))

    print('Done recording!')
    port_audio.terminate()


def save_recording(frames, port_audio, sample_frequency, bit_rate, audio_channels):
    with wave.open('recording_16bit.wav', 'wb') as wave_writer:
        wave_writer.setsampwidth(port_audio.get_sample_size(pyaudio.paInt16))
        wave_writer.setframerate(sample_frequency)
        wave_writer.setnchannels(audio_channels)
        wave_writer.writeframes(b''.join(frames))


def read_wave_file(file):
    port_audio = pyaudio.PyAudio()

    with wave.open(str(file.absolute()), 'rb') as wave_read:
        print(wave_read.getnchannels())
        print(wave_read.getsampwidth())
        print(wave_read.getframerate())
        print(wave_read.getnframes())
        print(wave_read.getcomptype())
        print(wave_read.getcompname())
        print(wave_read.getmarkers())

    stream = port_audio.open(rate=32000,
                             channels=1,
                             format=port_audio.get_format_from_width(int(16/8)),
                             output=True,
                             frames_per_buffer=1024)
    print(file, type(file), file.absolute(), type(file.absolute()), dir(file))
    with wave.open(str(file.absolute()), 'rb') as wave_reader:
        frames = wave_reader.readframes(1000000)
        stream.write(frames)
    port_audio.terminate()


def convert_microphone_byte_frames_to_int(frames):
    return [int(item, base=16) for item in frames.hex('-', bytes_per_sep=2).split('-')]
