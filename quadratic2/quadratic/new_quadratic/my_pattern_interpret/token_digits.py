from my_pattern_interpret.token_digit import *
from my_pattern_interpret.token322 import *

class Tokenizer_digits(TokenInterface):

    def __init__(self):
        super().__init__()
        self.tokenizer = Tokenizer_digit()

    def interpret(self, string, pos):
        if not self.check_bounds(string, pos):
            return empty
        curr_pos = pos
        token = self.tokenizer.interpret(string, curr_pos)
        while token.type != token_empty:
            if self.check_bounds(string, curr_pos + token.length):
                curr_pos += token.length
                token = self.tokenizer.interpret(string, curr_pos)
            else:
                return Token(token_number, string[pos:], len(string) - pos)
        return Token(token_number, string[pos: curr_pos], curr_pos - pos)