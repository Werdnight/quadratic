from my_pattern_interpret.interface import *
from my_pattern_interpret.token322 import *


class Tokenizer_dot(TokenInterface):

    def __init__(self):
        super().__init__()

    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty

        if string[pos] == '.' or string[pos] == ',':
            return Token(token_number, '.', 1)
        else:
            return Token(token_empty, '', 0)