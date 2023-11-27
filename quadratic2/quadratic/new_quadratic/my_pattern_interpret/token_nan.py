from my_pattern_interpret.token_sign import *
from my_pattern_interpret.token322 import *


class Tokenizer_nan(TokenInterface):

    def __init__(self):
        super().__init__()
        self.tokenizer_sign = Tokenizer_sign()


    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty

        curr = pos

        token_sign = self.tokenizer_sign.interpret(string, curr)
        if token_sign.type != token_empty:
            curr += 1

        if string[curr:] == 'nan':
            return Token(token_nan, token_sign.value + string[curr:], token_sign.length + 3)
        else:
            return empty