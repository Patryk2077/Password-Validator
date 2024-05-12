from abc import ABC, abstractmethod
import re


class Validator(ABC):
    @abstractmethod
    def __init__(self, text):
        pass

    @abstractmethod
    def is_valid(self):
        pass


class LenghtValidator(Validator):
    def __init__(self, text, lenght=8):
        self.text = text
        self.lenght = lenght

    def is_valid(self):
        if len(self.text) >= self.lenght:
            return True
        else:
            False


class NumberValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if re.search(r"\d", self.text):
            return True
        else:
            return False


class SpecialCharactersValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if re.search(r"[^\w\s]", self.text):
            return True
        else:
            return False


class UpperCharactersValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if re.search(r"[A-Z]", self.text):
            return True
        else:
            return False


class LowerCharactersValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        if re.search(r"[a-z]", self.text):
            return True
        else:
            return False


class PasswordLeakValidator(Validator):
    def __init__(self, text):
        self.text = text

    def is_valid(self):
        pass


class PasswordValidator():
    def __init__(self, text):
        pass
