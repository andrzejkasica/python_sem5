import math

class Complex_numb():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return '(%s, %s)' % (self.a, self.b)

    def __add__(self, n):
        a = self.a
        b = self.b
        c = n.a
        d = n.b
        new_real = a + c
        new_imag = b + d
        return Complex_numb(new_real_part, new_imag_part)

    def __sub__(self, n):
        a = self.a
        b = self.b
        c = n.a
        d = n.b
        new_real = a - c
        new_imag = b - d
        return Complex_numb(new_real_part, new_imag_part)



