from speech_to_text import transcribe_audio
from chatbot import ask_toy


def main():
    audio_path = "data/audio/sample.wav"

    print("🎤 Listening to audio...")

    user_text = transcribe_audio(audio_path)

    print("\n👧 Child said:")
    print(user_text)

    print("\n🤖 Buddy is thinking...")

    response = ask_toy(user_text)

    print("\n🤖 Buddy says:")
    print(response)


if __name__ == "__main__":
    main()