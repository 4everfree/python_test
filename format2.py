age = 18
name = 'vlad'
day = 'monday'

d = (age,name,day)

# %d это спецификатор целого числа
age_str = 'привет мне {0} лет, меня зовут {1}, сегодня {2}'.format(age,name,day)	#использование форматирования строки 
print(age_str)

age_str = 'привет мне {age} лет, меня зовут {name}, сегодня {day}'.format(age=age,name=name,day=day)	#использование форматирования строки 
print(age_str)


percent = 10.55
percent_str = "year income = {0:.1f}%".format(percent)
print(percent_str)