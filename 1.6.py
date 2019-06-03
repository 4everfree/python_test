import sys

print(
	1,2,3,
	sep=' ',#разделитель выводимых объектов
	end='\n',#конечный символ
	file=sys.stdout,#стандартный вывод
	flush=False) #при FALSE выводимое значение записывается в файл


#large amount of text with saved text formatting
print("""Строка 1
	строка 2
	строка 3""")

#аналог вывода через sys
#не вставляет перенос строки в конец
sys.stdout.write("Строка\n")

