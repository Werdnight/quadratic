from my_pattern_interpret.token322 import *
from my_pattern_interpret.token_Z import *
from my_pattern_interpret.token_dot import *
from my_pattern_interpret.token_sign import *
from my_pattern_interpret.token_digits import *

class Tokenizer_Q(TokenInterface):

    def __init__(self):
        super().__init__()
        self.tokenizer_z = Tokenizer_Z()
        self.tokenizer_dot = Tokenizer_dot()
        self.tokenizer_digits = Tokenizer_digits()
        self.tokenizer_sign = Tokenizer_sign()

    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty
        curr = pos
        token_z = self.tokenizer_z.interpret(string, curr)
        if token_z.type != token_empty:
            curr += token_z.length
            token_dot = self.tokenizer_dot.interpret(string, curr)
            if token_dot.type != token_empty:
                curr += token_dot.length
                token_digits = self.tokenizer_digits.interpret(string, curr)
                if token_digits.type != token_empty and token_digits.value != zero:
                    return Token(token_number, token_z.value + token_dot.value + token_digits.value,
                                 token_z.length + token_dot.length + token_digits.length)
                else:
                    return Token(token_number, token_z.value, token_z.length + token_dot.length + token_digits.length)
            else:
                if token_z.value == sign_minus + zero:
                    return Token(token_number, zero, token_z.length)
                return token_z
        else:
            token_sign = self.tokenizer_sign.interpret(string, curr)
            if token_sign.type != token_empty:
                curr += token_sign.length
            token_dot = self.tokenizer_dot.interpret(string, curr)
            if token_dot.type != token_empty:
                curr += token_dot.length

                token_digits = self.tokenizer_digits.interpret(string, curr)
                if token_digits.type != token_empty:
                    return Token(token_number, token_sign.value + zero + token_dot.value + token_digits.value,
                                 token_sign.length + token_dot.length + token_digits.length)
                else:
                    return error
            else:
                return error
