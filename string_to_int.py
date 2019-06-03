#полученное при вводе число в питоне это всегда строка
salary = '50000.5'

#преобразование строки в целое число
#year_salary = int(salary) * 12

#преобрахование строки в число с плавающей точкой
year_salary = float(salary) * 12

#вывод без преобразование в строку
print("year salary:",year_salary)

#вывод с преобразованием числа в строку
print("year salary: " + str(year_salary)) 