
class Time:
    def __init__(self, Hour=None, Minute=None, Second=None):
        self.Hour = Hour
        self.Minute = Minute
        self.Second = Second

    def Sum_time(self, t):
        sum__t = Time()
        sum__t.Second = self.Second + t.Second
        sum__t.Minute = self.Minute + t.Minute
        sum__t.Hour = self.Hour + t.Hour
        if sum__t.Second >= 60:
            sum__t.Second -= 60
            sum__t.Minute += 1
        if sum__t.Minute >= 60:
            sum__t.Minute -= 60
            sum__t.Hour += 1
        return sum__t

    def sub_time(self, t):
        sub__t = Time()
        sub__t.Second = self.Second - t.Second
        sub__t.Minute = self.Minute - t.Minute
        sub__t.Hour = self.Hour - t.Hour
        if sub__t.Second < 0:
            sub__t.Minute -= 1
            sub__t.Second += 60
        if sub__t.Minute < 0:
            sub__t.Minute += 60
            sub__t.Hour -= 1
        return sub__t

    def ConvertStoT(self):
        result = Time()
        result.Second = (self.Second % 3600) % 60
        result.Minute = (self.Second % 3600)//60
        result.Hour = (self.Second)//3600
        return result

    def ConvertTtoS(self):
        result = Time()
        result.Hour = self.Hour * 3600
        result.Minute = self.Minute * 60
        result.Second = self.Second
        secs = result.Hour + result.Minute + result.Second
        print("the time you enterd converted to ", secs, " seconds")

    def show(self):
        print(self.Hour, ":", self.Minute, ":", self.Second)


def menu():
    user = int(input('please choose your number:  \n 1-summation of two time\n2-subtrct of two time\n3-convert seconds to time\n4-convert time to seconds\n'))
    if user == 1:
        h = int(input("please enter hour1:  "))
        m = int(input("please enter minute1:  "))
        s = int(input("please enter second1:  "))
        time_a = Time(h, m, s)
        h2 = int(input("please enter hour2:  "))
        m2 = int(input("please enter minute2:  "))
        s2 = int(input("please enter second2:  "))
        time_b = Time(h2, m2, s2)
        jm = time_a.Sum_time(time_b)
        jm.show()
    if user == 2:
        h = int(input("please enter hour1:  "))
        m = int(input("please enter minute1:  "))
        s = int(input("please enter second1:  "))
        time_a = Time(h, m, s)
        h2 = int(input("please enter hour2:  "))
        m2 = int(input("please enter minute2:  "))
        s2 = int(input("please enter second2:  "))
        time_b = Time(h2, m2, s2)
        km = time_a.sub_time(time_b)
        km.show()
    if user == 3:
        h = int(input("please enter hour:  "))
        m = int(input("please enter minute:  "))
        s = int(input("please enter second:  "))
        a = Time(h, m, s)
        a.ConvertTtoS()

    if user == 4:
        s = int(input("please enter seconds:  "))
        time_a = Time(Second=s)
        n = time_a.ConvertStoT()
        n.show()


menu()
