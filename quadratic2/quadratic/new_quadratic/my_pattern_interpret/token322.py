token_empty = 0
token_number = 1
token_error = 2
token_inf = 3
token_nan = 4

class Token:

    def __init__(self, type, value, length):
        self.type = type
        self.value = value
        self.length = length

    def __str__(self):
        result = ''
        if self.type == token_empty:
            result += 'empty'
        elif self.type == token_number:
            result += 'number: '
        elif self.type == token_error:
            result += 'Неправильный ввод'
        elif self.type == token_inf:
            result += 'inf: '
        elif self.type == token_nan:
            result += 'nan:'
        result += self.value
        return result

    def empty(self):
       self.type = token_empty
       self.value = ''
       self.length = 0

    def error(self):
       self.type = token_error
       self.value = ''
       self.length = 0