from abc import ABC, abstractmethod


class Validator(ABC):
    @abstractmethod
    def __init__(self, text):
        pass

    @abstractmethod
    def is_valid(self):
        pass


class HasLenghtValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        pass
