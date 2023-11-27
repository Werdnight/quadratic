from my_pattern_interpret.token322 import *

empty = Token(token_empty, '', 0)
error = Token(token_error, '', 0)
pos_zero = 0
zero = '0'
sign_minus = '-'

class TokenInterface:

    def __init__(self):
        pass

    def check_bounds(self, string, pos):
        if pos >= len(string) and len(string) > 0:
            return False
        return True

    def interpret(self, string, pos):
        self.string = string
        self.pos = pos