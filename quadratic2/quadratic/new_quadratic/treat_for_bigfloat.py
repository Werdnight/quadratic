MIN = 'minus'
MANT = 'int'
EXP = 'exponent'
RES = {MIN: 0, MANT: '', EXP: ''}


class Preparation:

    def __init__(self):
        pass

    def interpret_number(self, number):
        composite_float = {}
        if number[0] == '-':
            composite_float[MIN] = 1
            number = number[1:]
        else:
            composite_float[MIN] = 0
        if '.' in number:
            q = number.split('.')
            composite_float[MANT] = q[0]
            if composite_float[MANT] == '':
                composite_float[MANT] = '0'
            if 'e' in number:
                w = q[1].split('e')
                composite_float[MANT] += w[0]
                composite_float[EXP] = int(w[1]) - len(w[0])
            else:
                composite_float[MANT] += q[1]
                composite_float[EXP] = -len(q[1])
        else:
            if 'e' in number:
                q = number.split('e')
                composite_float[MANT] = q[0]
                composite_float[EXP] = int(q[1])
            else:
                composite_float[MANT] = number
                composite_float[EXP] = 0
        if len(composite_float[MANT])> 1:
            while len(composite_float[MANT]) > 1:
                if composite_float[MANT][len(composite_float[MANT]) - 1] == '0':
                    composite_float[MANT] = composite_float[MANT][0: len(composite_float[MANT]) - 1]
                    composite_float[EXP] = int(composite_float[EXP]) + 1
                else:
                    break    
        if len(composite_float[MANT])> 1:
            while len(composite_float[MANT]) > 1:
                if composite_float[MANT][0] == '0':
                    composite_float[MANT] = composite_float[MANT][1: len(composite_float[MANT])]
                else:
                    break
        return composite_float