from abc import ABC, abstractmethod
import re
import hashlib
import requests


class Validator(ABC):
    @abstractmethod
    def __init__(self, text):
        pass

    @abstractmethod
    def is_valid(self):
        pass


class LengthValidator(Validator):
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
        password_hash = hashlib.sha1(
            self.text.encode("utf-8")).hexdigest().upper()
        response = requests.get(
            "https://api.pwnedpasswords.com/range/" + password_hash[0:5])
        hash_suffixes = (line.split(":")
                         for line in response.text.splitlines())
        for suffix, count in hash_suffixes:
            if password_hash[5:] == suffix:
                return False
        return True


class PasswordValidator:
    def __init__(self, text):
        self.validators = [
            LengthValidator(text),
            NumberValidator(text),
            SpecialCharactersValidator(text),
            UpperCharactersValidator(text),
            LowerCharactersValidator(text),
            PasswordLeakValidator(text)
        ]

    def is_valid(self):
        return all(validator.is_valid() for validator in self.validators)


hasło = "hhfhfhhfhdkkdkkd"
validator = PasswordValidator(hasło)
if validator.is_valid():
    print("Hasło jest dobre")
else:
    print("Hasło jest złe")
