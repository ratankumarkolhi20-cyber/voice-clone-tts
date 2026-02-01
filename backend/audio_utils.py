import librosa
import soundfile as sf

def normalize_audio(input_path, output_path):
    audio, sr = librosa.load(input_path, sr=22050, mono=True)
    audio = audio / max(abs(audio))
    sf.write(output_path, audio, 22050)
