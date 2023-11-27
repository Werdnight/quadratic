from my_pattern_interpret.token322 import *
from my_pattern_interpret.token_digit import *
from my_pattern_interpret.token_digits import *

class Tokenizer_N(TokenInterface):

    def __init__(self):
        super().__init__()
        self.tokenizer_digits = Tokenizer_digits()
        self.tokenizer_digit = Tokenizer_digit()

    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty

        token_digit = self.tokenizer_digit.interpret(string, pos)
        if token_digit.type != token_empty:
            if token_digit.value != zero:
                token_digits = self.tokenizer_digits.interpret(string, pos + token_digit.length)
                if token_digits != token_empty:
                    return Token(token_number, token_digit.value + token_digits.value,
                                 token_digit.length + token_digits.length)
                else:
                    return token_digit
            else:
                return token_digit
        else:
            return empty
