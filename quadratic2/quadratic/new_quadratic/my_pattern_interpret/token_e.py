from my_pattern_interpret.interface import *
from my_pattern_interpret.token322 import *


class Tokenizer_exp(TokenInterface):

    def __init__(self):
        super().__init__()

    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty

        if string[pos] == 'e':
            return Token(token_number, string[pos], 1)
        else:
            return Token(token_empty, '', 0)