# Used to record audio
import pyaudio
# Used to save the recorded audio
import wave
import os
import datetime
import logging

logging.basicConfig(level=logging.INFO)

# RECORD AUDIO
FRAMES_PER_BUFFER = 3200
FORMAT = pyaudio.paInt16
CHANNELS = 1
FRAME_RATE = 16000
SAVE_PATH = "data/audio-recording"

def record_mic(record_duration):

    p = pyaudio.PyAudio()

    stream = p.open(
        format=FORMAT,
        channels=CHANNELS,
        rate=FRAME_RATE,
        input=True,
        frames_per_buffer=FRAMES_PER_BUFFER
    )

    # Recorded frames
    frames = []
    # Duration of recording
    seconds = record_duration

    logging.info(f"Question prompt will be recorded for {record_duration} seconds")
    logging.info("Started recording...")

    # Frames is composed of buffers. With each iteration we record each buffer and append it to `frames` list.
    for i in range(int(FRAME_RATE/FRAMES_PER_BUFFER*seconds)):
        data_chunk = stream.read(FRAMES_PER_BUFFER)
        frames.append(data_chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()

    logging.info("Ended recording")

    # SAVE AUDIO AS WAVE FILE
    current_timestamp = str(datetime.datetime.now())
    current_timestamp = "-".join(current_timestamp.split())
    filename = f"{current_timestamp}"+"-recording.wav"
    save_path = os.path.join(SAVE_PATH, filename)
    obj = wave.open(save_path, "wb")
    obj.setnchannels(1)
    obj.setsampwidth(p.get_sample_size(FORMAT))
    obj.setframerate(FRAME_RATE)
    
    # Join all buffers/data chunks in frames list in binary format
    obj.writeframes(b"".join(frames))
    obj.close()
    logging.info(f"Saved recording at {save_path}")

    return save_path

def main():
    record_mic(4)

if __name__ == "__main__":
    main()