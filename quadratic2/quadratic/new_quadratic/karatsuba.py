    # def karatsuba(self, f, s):
    #     if len(f) == 1 or len(s) == 1:
    #         return str(int(f) * int(s))

    #     max_len = max(len(f), len(s))

    #     if max_len % 2 == 1:
    #         max_len += 1

    #     mid = max_len // 2
    #     f = f.zfill(max_len)
    #     s = s.zfill(max_len)
    #     a = f[:mid]
    #     b = f[mid:]
    #     c = s[:mid]
    #     d = s[mid:]
    #     ac = self.karatsuba(a, c)
    #     bd = self.karatsuba(b, d)
    #     a = BigFloat(a)
    #     b = BigFloat(b)
    #     c = BigFloat(c)
    #     d = BigFloat(d)
    #     a_b = (a + b).__str__()
    #     c_d = (c + d).__str__()
    #     a_b = self.add_zeros(a_b)
    #     c_d = self.add_zeros(c_d)
    #     abcd = self.karatsuba(a_b, c_d)
    #     abcd = BigFloat(abcd)
    #     ac = BigFloat(ac)
    #     bd = BigFloat(bd)
    #     adbc = (abcd - ac - bd)
    #     adbc = adbc.__str__()
    #     adbc = self.add_zeros(adbc)
    #     ac = ac.__str__()
    #     ac = self.add_zeros(ac)
    #     bd = bd.__str__()
    #     bd = self.add_zeros(bd)
    #     result = ac + '0' * (10 ** (max_len - mid - len(adbc))) + adbc + '0' * (10 ** (mid - len(bd.__str__()))) + bd
    #     return result