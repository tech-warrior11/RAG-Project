import sounddevice as sd
from scipy.io.wavfile import write
import os

def record_audio(duration=3.0, fs=16000):
    folder = "test_audio"
    os.makedirs(folder, exist_ok=True)
    file_count = len([f for f in os.listdir(folder) if f.endswith('.wav')]) + 1
    filename = os.path.join(folder, f"ultra_fast_{file_count}.wav")
    print(f"\nRecording for {duration} seconds... Bolna shuru karo!")
    myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait() 
    write(filename, fs, myrecording)
    print(f"Saved: {filename}")

if __name__ == "__main__":
    record_audio(duration=3.0)