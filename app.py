from mic import MicroPhoneReader


def mic_example():
    mic = MicroPhoneReader(language='fa-IR', verbose=True)
    status, text = mic.read()
    if status:
        print(text)


if __name__ == '__main__':
    mic_example()
