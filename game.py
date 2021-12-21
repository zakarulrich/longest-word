# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string
import requests


class Game:
    def __init__(self) -> None:
        self.grid = [random.choice(string.ascii_uppercase) for _ in range(9)]

    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy()
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.is_checked(word)

    @staticmethod
    def is_checked(world):
        data = requests.get(
            f"https://wagon-dictionary.herokuapp.com/{world}")

        response = data.json()
        return True if response['found'] == 'true' else False
