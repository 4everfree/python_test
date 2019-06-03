#'a' здесь на запись файла
products_file = open("дробные числа.txt",encoding='cp1251')	#открытие файла, переменная отвечающая за работу с файлом

products = products_file.read().strip()	#чтение содержимого файла

print(products)	#показать внутренности

print(products[0])	#показать внутренности
print(products[1])
print(products[2])
print(products[3])


# products_file.write('\nмолоко')n