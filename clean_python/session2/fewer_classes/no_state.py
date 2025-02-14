
# TODO which class can we drop? Extract the functionality of the class you think does not need to be a class

class TemperatureLogger:
    def __init__(self):
        self.temp_log = []

    def get_latest_temp(self):
        return self.temp_log[-1]

class TextFormatter:

    def __init__(self):
        pass

    def format_sentence(self, sentence):
        return " ".join(word.upper() if len(word) > 3 else word for word in sentence.split())
