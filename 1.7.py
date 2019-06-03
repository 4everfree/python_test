#input получает данные с stdin ввода
name = input("стандартное выписываемое значение")

try:
	s = input("Введите данные")
	print(s)
except EOFError:
	print("Обработали исключение EOFError")

#функция eval обрабатывает вводимое значение 
result = eval(input("введите инструкцию: "))
print(result)


