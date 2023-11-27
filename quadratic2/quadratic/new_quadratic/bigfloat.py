from treat_for_bigfloat import *


class Container:
    def __init__(self, value):
        self.value = value

    def make_dict(self):
        value_dict = {}
        for i in range(self.len_()-1, -1, -1):
            value_dict[i] = self.value[self.len_() - 1 - i]
        return value_dict

    def len_(self):
        l = 0
        for _ in self.value:
            l += 1
        return l


class BigFloat:

    max_deg = 0
    min_deg = 0

    def __init__(self, value):
        self.prep = Preparation()
        self.value = self.prep.interpret_number(str(value))


    def __add__(self, other):
        self.check_add(other)
        res = RES
        res = self.res_to_str(res)
        return BigFloat(res)

    def __sub__(self, other):
        self.check_diff(other)
        res = RES
        res = self.res_to_str(res)
        return BigFloat(res)

    def __mul__(self, other):
        exp = self.exp_prod(other)
        a, b = self.do_container(other)
        RES[MANT] = self.dict_of_prod(a, b)
        RES[EXP] = exp
        RES[MIN] = self.sign_prod_div(other)
        res = RES
        res = self.res_to_str(res)
        return BigFloat(res)

    def __truediv__(self, other):
        exp = self.exp_div(other)
        division = ''
        a = self.value[MANT] + '0' * 1000
        b = other.value[MANT]
        exp -= 999
        end = - len(a) + len(b) 
        while end != 0:
            d, r = self.bin_div(a[:end], b)
            r = self.del_e(r)
            a = str(r) + a[end:]
            division += str(d)
            end += 1
        RES[MANT] = division
        RES[EXP] = exp
        RES[MIN] = self.sign_prod_div(other)
        res = RES
        res = self.res_to_str(res)
        return BigFloat(res)
    
    def sqrt(self):
        return self.sqrt_column()

    def __str__(self):
        value = self.value
        return self.res_to_str(value)
    
    def float(self):
        value = self.value
        if len(value[MANT]) > 1:
            while len(value[MANT]) > 1:
                if value[MANT][len(value[MANT]) - 1] == '0':
                    value[MANT] = value[MANT][0: len(value[MANT]) - 1]
                    value[EXP] = int(value[EXP]) + 1
                else:
                    break
        if len(value[MANT]) > 1:
            while len(value[MANT]) > 1:
                if value[MANT][0] == '0':
                    value[MANT] = value[MANT][1: len(value[MANT])]
                else:
                    break
        if value[MIN] % 2 == 0:
            minus = ''
        else:
            minus = '-'

        if len(value[MANT]) > 1:
            value[MANT] = value[MANT][0] + '.' + value[MANT][1:]
            value[EXP] += len(value[MANT][2:])
            if len(value[MANT]) > 102:
                value[MANT] = value[MANT][:102]

        if str(value[EXP]) == '0':
            exp = ''
        else:
            exp = 'e' + str(value[EXP])

        if value[MANT] == '0':
            exp = ''
            minus = ''

        str_res = minus + value[MANT] + exp
        RES[MIN] = 0
        RES[MANT] = ''
        RES[EXP] = ''
        return str_res
    
    def __lt__(self, other):
        a, b = self.eq_mantis(other)
        return self.value[MIN] > other.value[MIN] or (other.value[MIN] == 0 and a < b) or (self.value[MIN] == 1 and a > b)

    def __le__(self, other):
        a, b = self.eq_mantis(other)
        return self.value[MIN] > other.value[MIN] or (other.value[MIN] == 0 and a <= b) or (self.value[MIN] == 1 and a >= b)

    def __eq__(self, other):
        a, b = self.eq_mantis(other)
        return self.value[MIN] == other.value[MIN] and a == b

    def __ne__(self, other):
        a, b = self.eq_mantis(other)
        return self.value[MIN] != other.value[MIN] or a != b

    def __gt__(self, other):
        a, b = self.eq_mantis(other)
        return self.value[MIN] < other.value[MIN] or (self.value[MIN] == 0 and a > b) or (other.value[MIN] == 1 and a < b)

    def __ge__(self, other):
        a, b = self.eq_mantis(other)
        return self.value[MIN] < other.value[MIN] or (self.value[MIN] == 0 and a >= b) or (other.value[MIN] == 1 and a <= b)

    def del_e(self, r):
        if 'e' in r:
            i = r.find('e')
            r = r[0:i] + '0' * int(r[i+1:])
        return r


    def check_add(self, other):
        if self.value[MIN] == 1:
             if other.value[MIN] == 1:
                self.add(other)
                RES[MIN] += 1
             else:
                other.sub(self)
        else:
            if other.value[MIN] == 1:
                self.sub(other)
            else:
                self.add(other)

    def check_diff(self, other):
        if self.value[MIN] == 1:
            if other.value[MIN] == 1:
                other.sub(self)
            else:
                other.add(self)
                RES[MIN] += 1
        else:
            if other.value[MIN] == 0:
                self.sub(other)
            else:
                self.add(other)

    def add(self, other):
        # self.eq_deg(other)
        self.value[MANT], other.value[MANT] = self.eq_mantis(other)
        exp_sum = self.value[EXP]
        a, b = self.do_container(other)
        sum_dict = self.dict_of_sum(a, b)
        RES[MANT] = self.dict_to_str(sum_dict)
        RES[EXP] = exp_sum

    def sub(self, other):
        # self.eq_deg(other)
        self.value[MANT], other.value[MANT] = self.eq_mantis(other)
        exp_diff = self.value[EXP]
        a, b = self.do_container(other)
        a, b = self.larg_small(a, b)
        diff_dict = self.dict_of_diff(a, b)
        RES[MANT] = self.dict_to_str(diff_dict)
        RES[EXP] = exp_diff

    def sqrt_column(self):
        val = self.value[MANT]
        exp = self.value[EXP]
        # val += '0' * 200
        # exp -= 200
        if len(val) < 300:
            val += '0' * 300
            exp -= 300
        val += '0'
        exp_root = exp // 2  
        val += '0' * (exp % 2)
        end = -len(val) + 1 + (len(val) % 2)
        str_ans = ''
        while end < 0:
            root_number, r = self.bin_root(val[:end], str_ans)
            r = self.del_e(r)
            str_ans += str(root_number)
            val = str(r) + val[end:]
            end += 2
        RES[MANT] = str_ans
        RES[EXP] = exp_root
        RES[MIN] = 0
        res = RES
        res = self.res_to_str(res)
        return BigFloat(res)
    

    def dict_of_sum(self, a, b):
        dict_sum = {}
        for key in range(0, BigFloat.max_deg + 1):
            if key not in dict_sum:
                dict_sum[key] = 0
            if key in a:
                dict_sum[key] += int(a[key])
            if key in b:
                dict_sum[key] += int(b[key])
            dict_sum[key + 1] = dict_sum[key] // 10
            dict_sum[key] = dict_sum[key] % 10
            if key == BigFloat.max_deg:
                BigFloat.max_deg = key + 1
        return dict_sum

    def dict_of_diff(self, a, b):
        dict_diff = {}
        for key in range(0, BigFloat.max_deg + 1):
            if key not in dict_diff:
                dict_diff[key] = int(a[key])
            if key in b:
                dict_diff[key] -= int(b[key])
            if dict_diff[key] < 0:
                dict_diff[key + 1] = int(a[key + 1])
                dict_diff[key + 1] -= 1
                dict_diff[key] = 10 + dict_diff[key]
        return dict_diff

    def dict_of_prod(self, a, b):
        dict_prod = {}
        for key_a in range(0, BigFloat.max_deg + 1):
            for key_b in range(0, BigFloat.max_deg + 1):
                if (key_a + key_b) not in dict_prod:
                    dict_prod[key_a + key_b] = 0
                if key_a in a and key_b in b:
                    a_b = int(a[key_a]) * int(b[key_b])
                    dict_prod[key_a + key_b] += a_b 

        for key in range(0, BigFloat.max_deg + BigFloat.min_deg + 1):
            if key + 1 not in dict_prod:
                dict_prod[key + 1] = 0
            dict_prod[key + 1] += dict_prod[key] // 10
            dict_prod[key] = dict_prod[key] % 10
            if key == BigFloat.max_deg + BigFloat.min_deg:
                BigFloat.max_deg += 1
        BigFloat.max_deg = BigFloat.max_deg + BigFloat.min_deg
        prod_str = self.dict_to_str(dict_prod)
        return prod_str

    def bin_div(self, a, b):
        a = BigFloat(a)
        b = BigFloat(b)
        low = 0
        high = 10
        while low <= high:
            mid = (low + high) // 2
            mid_high = mid + 1
            mid_bf = BigFloat(mid)
            mid_bf_high = BigFloat(mid_high)
            guess = mid_bf * b
            guess_high = b * mid_bf_high
            if guess <= a and guess_high > a:
                ost = a - guess
                return mid, ost.__str__()
            elif guess > a:
                high = mid - 1
            else:
                low = mid + 1
        return -1
    
    def bin_root(self, val, str_ans):
        if str_ans == '':
            str_ans = '0'
        val_bf = BigFloat(val)
        twenty = BigFloat(20)
        str_ans = BigFloat(str_ans)
        coef = str_ans * twenty
        low = 0
        high = 10
        while low <= high:
            mid = (low + high) // 2
            mid_high = mid + 1
            mid_bf = BigFloat(mid)
            mid_bf_high = BigFloat(mid_high)
            guess = (mid_bf + coef) * mid_bf
            guess_high = (mid_bf_high + coef) * mid_bf_high
            if guess <= val_bf and guess_high > val_bf:
                r = val_bf - guess
                return mid, str(r) 
            elif guess > val_bf:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    def res_to_str(self, value):
        if len(value[MANT]) > 1:
            while len(value[MANT]) > 1:
                if value[MANT][len(value[MANT]) - 1] == '0':
                    value[MANT] = value[MANT][0: len(value[MANT]) - 1]
                    value[EXP] = int(value[EXP]) + 1
                else:
                    break    
        if len(value[MANT]) > 1:
            while len(value[MANT]) > 1:
                if value[MANT][0] == '0':
                    value[MANT] = value[MANT][1: len(value[MANT])]
                else:
                    break
        if value[MIN] % 2 == 0:
            minus = ''
        else:
            minus = '-'

        if str(value[EXP]) == '0':
            exp = ''
        else:
            exp = 'e' + str(value[EXP])
        
        if value[MANT] == '0':
            exp = '' 
            minus = ''

        str_res = minus + value[MANT] + exp
        RES[MIN] = 0
        RES[MANT] = ''
        RES[EXP] = ''
        return str_res

    def eq_mantis(self, other):
        self.eq_deg(other)
        f = len(self.value[MANT])
        s = len(other.value[MANT])
        module = abs(f - s)
        a = self.value[MANT]
        b = other.value[MANT]
        if f < s:
            a = module * '0' + a
        else:
            b = module * '0' + b
        return a, b
    

    def larg_small(self, a, b):
        for i in range(BigFloat.max_deg, -1, -1):
            if i not in b:
                b[i] = '0'
            elif i not in a:
                RES[MIN] += 1
                return b, a
            if b[i] < a[i]:
                break
            elif b[i] > a[i]:
                RES[MIN] += 1
                return b, a
            else:
                continue
        return a, b

    def sign_prod_div(self, other):
        minus = self.value[MIN] + other.value[MIN]
        if minus % 2 == 0:
            return 0
        else:
            return 1

    def eq_deg(self, other):
        if self.value[EXP] > other.value[EXP]:
            self.value[MANT] += '0' * (self.value[EXP] - other.value[EXP])
            self.value[EXP] = other.value[EXP]
        else:
            other.value[MANT] += '0' * (other.value[EXP] - self.value[EXP])
            other.value[EXP] = self.value[EXP]

    def exp_prod(self, other):
        exp_prod = self.value[EXP] + other.value[EXP]
        return exp_prod

    def exp_div(self, other):
        if len(other.value[MANT]) > len(self.value[MANT]):
            q = len(other.value[MANT]) - len(self.value[MANT])
            self.value[MANT] += '0' * q
            self.value[EXP] -= q
        exp_diff = self.value[EXP] - other.value[EXP]
        return exp_diff 

    def do_container(self, other):
        a = Container(self.value[MANT])
        b = Container(other.value[MANT])
        BigFloat.min_deg = min(a.len_(), b.len_()) - 1
        BigFloat.max_deg = max(a.len_(), b.len_()) - 1
        return a.make_dict(), b.make_dict()
    
    def dict_to_str(self, dict):
        int_str = ''
        for key in range(BigFloat.max_deg, - 1, -1):
            if BigFloat.max_deg != 0 and dict[key] == 0 and BigFloat.max_deg == key:
                BigFloat.max_deg -= 1
                continue
            int_str = int_str + str(dict[key])
        return int_str