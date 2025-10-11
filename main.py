import pyaudio
import wave

chunk = 1024
format = pyaudio.paInt16
channels = 1
rate = 44100
record_seconds = 20
wave_file_name = "sesDosya.wav"

p = pyaudio.PyAudio()

stream = p.open(format=format,rate = rate,channels=channels,input=True, frames_per_buffer=chunk)

print("recording")

frames = []

for i in range(0,int(rate/chunk*record_seconds)):
    data = stream.read(chunk)
    frames.append(data)

print("its done")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(wave_file_name,"wb")

wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(rate)

wf.writeframes(b"".join(frames))

wf.close()

print(f"ses {wave_file_name} dosyanica kaydedildi")