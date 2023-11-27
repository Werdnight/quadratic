from my_pattern_interpret.token_Q import *
from my_pattern_interpret.token_e import *
from my_pattern_interpret.token_sign import *
from my_pattern_interpret.token_digit import *
from my_pattern_interpret.token_digits import *
from my_pattern_interpret.token322 import *
from my_pattern_interpret.token_Z import *

class Tokenizer_R(TokenInterface):

    def __init__(self):
        super().__init__()
        self.tokenizer_q = Tokenizer_Q()
        self.tokenizer_e = Tokenizer_exp()
        self.tokenizer_sign = Tokenizer_sign()
        self.tokenizer_digit = Tokenizer_digit()
        self.tokenizer_digits = Tokenizer_digits()
        self.tokenizer_z = Tokenizer_Z()


    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty
        curr = pos
        token_q = self.tokenizer_q.interpret(string, curr)
        if token_q.type != token_empty:
            curr += token_q.length
            token_e = self.tokenizer_e.interpret(string, curr)

            if token_e.type != token_empty and token_q.value != zero:
                curr += token_e.length
                token_z = self.tokenizer_z.interpret(string, curr)
                if token_z.type != token_empty:
                    return Token(token_number, token_q.value + token_e.value + token_z.value, \
                                      token_q.length + token_e.length + token_z.length)
                    # if token_z.value != zero:
                    #     return Token(token_number, token_q.value + token_e.value + token_z.value, \
                    #                  token_q.length + token_e.length + token_z.length)
                else:
                     return error
            elif token_e.type != token_empty and token_q.value == zero:
                return error
            else:
                return token_q
        else:
            return error