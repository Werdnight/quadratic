from my_pattern_interpret.interface import *
from my_pattern_interpret.token322 import *

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

class Tokenizer_digit(TokenInterface):

    def __init__(self):
        super().__init__()

    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty

        if string[pos] in digits:
            return Token(token_number, string[pos], 1)
        else:
            return Token(token_empty, '', 1)