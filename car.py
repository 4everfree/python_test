class Auto:
    
    def __init__(self,number=""):
        self._number = []
        if number:
            self._number = number(number)


    @property
    def number(self):
        return "".join(self._number)

    @number.setter
    def number(self,number):
        if number.__len__() != 6:
            print("not number")
        else:
            self._number = []
            for i in number:
                self._number.append(i)

auto1 = Auto("a222k1d")
print(auto1._number)
