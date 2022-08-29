from record_mic import record_mic
from speech_to_text import speechToText

def main():
    audio_file_path = record_mic()
    obj = speechToText()
    response = obj.upload_audio(audio_file_path)
    print(response)

if __name__ == "__main__":
    main()