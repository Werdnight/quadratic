from my_pattern_interpret.token_R import *
from my_pattern_interpret.token_nan import *
from my_pattern_interpret.token_inf import *
from my_pattern_interpret.token322 import *


class Tokenizer_NUMBER(TokenInterface):

    def __init__(self):
        super().__init__()
        self.tokenizer_r = Tokenizer_R()
        self.tokenizer_inf = Tokenizer_inf()
        self.tokenizer_nan = Tokenizer_nan()
        self.number = 0


    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty

        curr = pos
        token_r = self.tokenizer_r.interpret(string, curr)
        if token_r != empty and token_r != error:
            curr += token_r.length
            if self.check_bounds(string, curr):
                return error
            self.number = token_r.value
            return token_r
        else:
            token_nan = self.tokenizer_nan.interpret(string, curr)
            if token_nan != empty and token_nan != error:
                curr += token_nan.length
                if self.check_bounds(string, curr):
                    return error
                return token_nan
            else:
                token_inf = self.tokenizer_inf.interpret(string, curr)
                if token_inf != empty and token_inf != error:
                    curr += token_inf.length
                    if self.check_bounds(string, curr):
                        return error
                    return token_inf
                else:
                    return error