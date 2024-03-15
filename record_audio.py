import pyaudio
import wave

def record(WAVE_OUTPUT_FILENAME = "output.wav", RECORD_SECONDS = 10):
    FORMAT = pyaudio.paInt16 # формат аудио
    CHANNELS = 2 # стерео запись
    RATE = 44100 # частота дискретизации
    CHUNK = 1024 # буфер записи
    p = pyaudio.PyAudio()

    # Начало записи
    stream = p.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)
    print("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Остановка записи
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Сохранение файла
    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

