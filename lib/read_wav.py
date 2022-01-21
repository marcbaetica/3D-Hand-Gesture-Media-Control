import wave


def print_wave_file_characteristics(file):
    with wave.open(file, 'rb') as wave_read:
        # print(wave_read.getnchannels())
        # print(wave_read.getsampwidth())
        # print(wave_read.getframerate())
        # print(wave_read.getnframes())
        # print(wave_read.getcomptype())
        # print(wave_read.getcompname())
        # print(wave_read.getmarkers())
        print(wave_read.getparams())


def read_wave_file_first_frame(file):
    with wave.open(file, 'rb') as wave_read:
        for i in range(2):
            frame_red = wave_read.readframes(1)
            # print(type(frame_red), frame_red)
            # frame_red = wave_read.readframes(2)
            # print(type(frame_red), frame_red)
            # frame_red = wave_read.readframes(10)
            # print(type(frame_red), frame_red)
            print(frame_red, [int(hex_value, base=16) for hex_value in frame_red.hex('-').split('-')])
            # print(int(frame_red, base=16))


FILE = 'recording_16bit.wav'
print_wave_file_characteristics(FILE)
read_wave_file_first_frame(FILE)
