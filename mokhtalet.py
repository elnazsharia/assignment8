class complex_num:
    def __init__(self, imag=None, real=None):
        self.real = real
        self.imag = imag

    def add(self, other):
        add = complex_num()
        add.real = self.real + other.real
        add.imag = self.imag + other.imag
        return add

    def sub(self, other):
        add = complex_num()
        add.real = self.real - other.real
        add.imag = self.imag - other.imag
        return add

    def mul(self, other):
        add = complex_num()
        add.real = self.real * other.real
        add.imag = self.imag * other.imag
        return add

    def show(self):
        print(self.real, '+', self.imag, 'i')


while True:
    user = int(input(
        "please enter your number:  \n1-jam 2 adade mokhtalet\n2-tafrigh 2 adade mokhtalet\n3-zarbe 2 adade mokhtalet\n4-exit\n"))
    if user == 1:
        print('enter first complex number:  ')
        real1 = int(input())
        imag1 = int(input())
        com1 = complex_num(real1, imag1)
        print("enter complex number 2:  ")
        real2 = int(input())
        imag2 = int(input())
        com2 = complex_num(real2, imag2)
        com1.show()
        com2.show()
        sum = com1.add(com2)
        sum.show()
    if user == 2:
        print('enter first complex number:  ')
        real1 = int(input())
        imag1 = int(input())
        com1 = complex_num(real1, imag1)
        print("enter complex number 2:  ")
        real2 = int(input())
        imag2 = int(input())
        com2 = complex_num(real2, imag2)
        com1.show()
        com2.show()
        subt = com1.sub(com2)
        subt.show()
    if user == 3:
        print('enter first complex number:  ')
        real1 = int(input())
        imag1 = int(input())
        com1 = complex_num(real1, imag1)
        print("enter complex number 2:  ")
        real2 = int(input())
        imag2 = int(input())
        com2 = complex_num(real2, imag2)
        com2.show()
        com1.show()
        mult = com1.mul(com2)
        mult.show()
    else:
        break
