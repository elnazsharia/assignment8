def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


class Fractiion:
    def __init__(self, sourat, makhraj):
        self.sourat = sourat
        self.makhraj = makhraj

    def show(self):
        print(str(self.sourat) + '/' + str(self.makhraj))

    def sum_fract(self, other):
        _sum = Fractiion(self.sourat * other.makhraj + other.sourat *
                         self.makhraj, self.makhraj * other.makhraj)
        return _sum

    def sub_fract(self, other):
        _sub = Fractiion(self.sourat * other.makhraj - other.sourat *
                         self.makhraj, self.makhraj * other.makhraj)
        return _sub

    def mul_fract(self, other):
        _mul = Fractiion(self.sourat * other.sourat,
                         self.makhraj * other.makhraj)
        return _mul

    def div_fract(self, other):
        s = (self.sourat * other.makhraj)
        m = self.makhraj * other.sourat
        _gcd = gcd(s, m)
        sour = s/_gcd
        makh = m/_gcd
        _div = Fractiion(sour, makh)
        return _div

    def gcd_fract(self):
        _sade = gcd(self.sourat, self.makhraj)
        __kasr_sade = Fractiion(self.sourat/_sade, self.makhraj/_sade)
        return __kasr_sade


def menu():
    while True:
        user_choice = int(input(
            "please enter your choice:\n1-sumation of 2 fractions\n2-subtract of 2 fractions\n3-multiply of 2 fractions\n4-divide of 2 fractions\n1-simplification of fraction"))
        if user_choice == 1:
            a = int(input('please enter sourat1:   '))
            b = int(input('please enter makhraj1:   '))
            c = Fractiion(a, b)
            d = int(input('please enter sourat2:   '))
            e = int(input('please enter makhraj2:   '))
            f = Fractiion(d, e)
            m = c.sum_fract(f)
            m.show()
            break
        if user_choice == 2:
            a = int(input('please enter sourat1:   '))
            b = int(input('please enter makhraj1:   '))
            c = Fractiion(a, b)
            d = int(input('please enter sourat2:   '))
            e = int(input('please enter makhraj2:   '))
            f = Fractiion(d, e)
            m = c.sub_fract(f)
            m.show()
            break
        if user_choice == 3:
            a = int(input('please enter sourat1:   '))
            b = int(input('please enter makhraj1:   '))
            c = Fractiion(a, b)
            d = int(input('please enter sourat2:   '))
            e = int(input('please enter makhraj2:   '))
            f = Fractiion(d, e)
            m = c.mul_fract(f)
            m.show()
            break
        if user_choice == 4:
            a = int(input('please enter sourat1:   '))
            b = int(input('please enter makhraj1:   '))
            c = Fractiion(a, b)
            d = int(input('please enter sourat2:   '))
            e = int(input('please enter makhraj2:   '))
            f = Fractiion(d, e)
            m = c.div_fract(f)
            m.show()
            break
        else:
            a = int(input('please enter sourat1:   '))
            b = int(input('please enter makhraj1:   '))
            c = Fractiion(a, b)
            p = c.gcd_fract()
            p.show()
            break


menu()
