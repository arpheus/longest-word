import string
import requests
from random import choice

class Game:

    def __init__(self):
        self.grid = self.random_grid()

    def random_grid(self):
        grid = []
        for i in range(0,9):
            grid.append(choice(string.ascii_uppercase))
        return grid

    def is_valid(self, word):
        if len(word) > 0:
            #check if word is valid english
            is_english = requests.get("https://wagon-dictionary.herokuapp.com/"+word)
            json_is_english = is_english.json()
            if json_is_english["found"] != True:
                return False
            grid_letters = self.grid.copy()
            for letter in word:
                if letter in grid_letters:
                    grid_letters.remove(letter)
                else:
                    return False
        else:
            return False
        return True
