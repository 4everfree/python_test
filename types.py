l = [7,'sdkjfndsknf',2.6,[]]
print('оригинальный список',l)

l[0] = 10	#замена элемента списка на другой
print('замена элемента списка на другой',l)

el1 = 'djsnfsdkjfns'
el2 = 67576
l.append(el1)
l.append(el2)	#добавление элемента к списку

print('добавление элемента {el1},{el2} к списку',l)

string = l.pop(1)	#извлечение элемента в переменную
print(l)
print('извлечение элемента {string} в переменную')


l.remove(10) #удаление из списка по первому вхождению значения

print('удаление 10 из списка по первому вхождению значения',l)

l.insert(0,33)	#вставка элемента по индексу
print('вставка элемента по индексу',l)

#работает только для списков со значениями одного типа
# l.sort()	#упорядочивает список в порядке возрастания значения элементов
# print(l)

# l.reverse()	#упорядочивает по убыванию