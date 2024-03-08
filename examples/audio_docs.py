#!/usr/bin/env rye run python
# --8<-- [start:common_imports]
from pathlib import Path

from openai import OpenAI
# --8<-- [end:common_imports]

# --8<-- [start:common_setup]
openai = OpenAI()

speech_file_path = Path(__file__).parent / "speech.mp3"
# --8<-- [end:common_setup]

def main() -> None:

    stream_to_speakers()

    # --8<-- [start:speech]
    # Create text-to-speech audio file
    with openai.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        input="The quick brown fox jumps over the lazy dog.",
    ) as response:
        response.stream_to_file(speech_file_path)
    # --8<-- [end:speech]

    # --8<-- [start:transcription]
    # Create transcription from audio file
    transcription = openai.audio.transcriptions.create(
        model="whisper-1",
        file=speech_file_path,
    )
    print(transcription.text)
    # --8<-- [end:transcription]

    # --8<-- [start:translation]
    # Create translation from audio file
    translation = openai.audio.translations.create(
        model="whisper-1",
        file=speech_file_path,
    )
    print(translation.text)
    # --8<-- [end:translation]

# --8<-- [start:speech.with_streaming_response]
def stream_to_speakers() -> None:
    import pyaudio
    import time

    player_stream = pyaudio.PyAudio().open(format=pyaudio.paInt16, channels=1, rate=24000, output=True)

    start_time = time.time()

    with openai.audio.speech.with_streaming_response.create(
        model="tts-1",
        voice="alloy",
        response_format="pcm",  # similar to WAV, but without a header chunk at the start.
        input="""I see skies of blue and clouds of white
                The bright blessed days, the dark sacred nights
                And I think to myself
                What a wonderful world""",
    ) as response:
        print(f"Time to first byte: {int((time.time() - start_time) * 1000)}ms")
        for chunk in response.iter_bytes(chunk_size=1024):
            player_stream.write(chunk)

    print(f"Done in {int((time.time() - start_time) * 1000)}ms.")
# --8<-- [end:speech.with_streaming_response]

if __name__ == "__main__":
    main()
