from mic import MicroPhoneReader
from audio import AudioReader
import random


def mic_example():
    mic = MicroPhoneReader(language='fa-IR', verbose=True)
    status, text = mic.read()
    if status:
        print(text)


def audio_example():
    audio = AudioReader(audio_file='sample.wav', language='fa-IR', verbose=True)
    status, text = audio.read()
    if status:
        print(text)


if __name__ == '__main__':
    examples = [mic_example, audio_example]
    idx = random.randint(0, len(examples) - 1)
    example = examples[idx]
    example()
