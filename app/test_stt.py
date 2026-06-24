from speech_to_text import transcribe_audio

text = transcribe_audio("data/audio/sample.wav")

print("\nTranscription:")
print(text)