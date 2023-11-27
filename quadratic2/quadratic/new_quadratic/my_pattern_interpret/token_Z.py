from my_pattern_interpret.token322 import *
from my_pattern_interpret.token_N import *
from my_pattern_interpret.token_sign import *

class Tokenizer_Z(TokenInterface):

    def __init__(self):
        super().__init__()
        self.tokenizer_N = Tokenizer_N()
        self.tokenizer_sign = Tokenizer_sign()

    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty


        token_sign = self.tokenizer_sign.interpret(string, pos)
        if token_sign.type != token_empty:
            pos += token_sign.length

        token_n = self.tokenizer_N.interpret(string, pos)
        if token_n.type != token_empty:
            return Token(token_number, token_sign.value + token_n.value,
                                 token_sign.length + token_n.length)
        else:
            return empty