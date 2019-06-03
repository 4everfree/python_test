#'a' здесь только на запись файла
#'r+' файл будет открыт в режиме чтения и для записи
products_file = open("дробные числа.txt",encoding='cp1251')	#открытие файла, переменная отвечающая за работу с файлом
products = products_file.read().strip()	#чтение содержимого файла
products = products.replace("масло\n","").title()
products_file.close()

#python открывая файл в режиме записи - стирает его
new_products_file = open("new_products_file.txt",'w')
new_products_file.write(products)
new_products_file.close()

# products_file.write('\nмолоко')
# products_file.close()n
