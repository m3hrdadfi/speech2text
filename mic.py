import speech_recognition as sr


class MicroPhoneReader:
    """A class based on the speech recognition package to listen to audio continuously via microphone inputs."""

    UnknownValueError = {
        "en-US": "Google Speech Recognition could not understand audio",
        "fa-IR": "تشخیص گفتار گوگل نتوانست صدا را درک کند."
    }
    RequestError = {
        "en-US": "Could not request results from Google Speech Recognition service: {0}",
        "fa-IR": "درخواست نتایج از سرویس شناسایی گفتار گوگل امکان پذیر نیست: {0}"
    }
    ADJUST_AMB_NOISE = {
        'en-US': "Adjusting microphone.",
        'fa-IR': "تنظیم میکروفن."
    }
    ENERGY_THRESHOLD = {
        "en-US": "Set the minimum energy threshold to {0}.",
        "fa-IR": "حداقل آستانه انرژی را به {0} تنظیم کنید."
    }
    RECORD = {
        "en-US": "Say something!",
        "fa-IR": "چیزی بگو!"
    }

    def __init__(self, language='fa-IR', verbose=False):
        self.sr = sr
        self.r = sr.Recognizer()
        self.language = language
        self.verbose = verbose

    @staticmethod
    def _print(message, verbose=False):
        if verbose:
            print(message)

    def read(self):
        self.adjust_amb_noise(self.language)
        audio = self.record(self.language)
        return self.recognize_google(audio, self.language)

    def recognize_google(self, audio, language):

        try:
            text = self.r.recognize_google(audio, language=language)
        except self.sr.UnknownValueError:
            err = self.UnknownValueError.get(language, '')
            self._print(err, self.verbose)
            return False, err
        except self.sr.RequestError as e:
            err = self.RequestError.get(language, '').format(e)
            self._print(err, self.verbose)
            return False, err

        return True, text

    def adjust_amb_noise(self, language):
        self._print(self.ADJUST_AMB_NOISE.get(language, ''), self.verbose)

        with sr.Microphone() as source:
            self.r.adjust_for_ambient_noise(source)

        self._print(self.ENERGY_THRESHOLD.get(language, '').format(self.r.energy_threshold), self.verbose)
        return self

    def record(self, language):
        with sr.Microphone() as source:
            self._print(self.RECORD.get(language, ''), self.verbose)
            return self.r.listen(source)
