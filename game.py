# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods

import random
import string


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
        return True
