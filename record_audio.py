import threading
import pyaudio
import wave
from PyQt5.QtCore import QThread, pyqtSignal

class Recorder(QThread):
    finished = pyqtSignal(str)
    
    def __init__(self, output_filename="output.wav"):
        super().__init__()
        self.output_filename = output_filename
        self.is_recording = False

    def stop(self):
        self.is_recording = False
        self.finished.emit(self.output_filename)
  #
    def run(self):
        FORMAT = pyaudio.paInt16
        CHANNELS = 2
        RATE = 44100
        CHUNK = 1024
        frames = []
        p = pyaudio.PyAudio()
        stream = p.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
        print("Recording...")
        
        self.is_recording = True
        while self.is_recording:
            data = stream.read(CHUNK)
            frames.append(data)
        
        print("Finished recording.")
        
        stream.stop_stream()
        stream.close()
        p.terminate()
        
        wf = wave.open(self.output_filename, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()

        self.finished.emit(self.output_filename)
        
    def stop(self):
        self.is_recording = False
