class Word:
    @staticmethod
    def length(word):
        """
        Показывает длину строки
        :параметр word: строка, длина которой должна быть возвращена
        :return: длина строки в int
        """
        print(len(word))

    @staticmethod
    def word(obj,times=3,depth=5):
        print(obj*times*depth)


Word.length("ырваиоывлаивыалыоват")
Word.word('asmr',1,1)

my_list = []

with open("hello.py","r") as f:
    my_list.append(f.read())

print(my_list)