from TTS.api import TTS

tts = TTS(
    model_name="tts_models/multilingual/multi-dataset/your_tts",
    gpu=True
)

def clone_voice(text, reference_wav, output_path):
    tts.tts_to_file(
        text=text,
        speaker_wav=reference_wav,
        file_path=output_path
    )
