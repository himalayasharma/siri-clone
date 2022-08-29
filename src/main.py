from record_mic import record_mic
from speech_to_text import speechToText
from openai_response import get_answer

RECORD_DURATION=4

def main():
    # 1. RECORD AND SAVE AUDIO
    audio_file_path = record_mic(record_duration=RECORD_DURATION)
    # audio_file_path = "data/audio-recording/2022-08-29-15:15:14.353041-recording.wav"
    # 2. UPLOAD AUDIO FILE TO ASSEMBLY AI
    obj = speechToText()
    # Audio url in json is returned
    audio_url = obj.upload_audio(audio_file_path)
    # 3. SUBMIT UPLOADED FILE FOR TRANSCRIPTION
    transcription_job_id = obj.submit_for_transcription(audio_url=audio_url)
    # 4. GET TRANSCRIPTION
    question = obj.get_transcription(transcription_job_id=transcription_job_id)
    print(f"ME: {question}")
    # 5. SUBMIT QUESTION TO OPEN AI AND GET RESPONSE
    answer = get_answer(question=question)
    print(f"JARVIS: {answer}")

if __name__ == "__main__":
    main()