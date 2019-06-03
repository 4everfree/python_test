age = 18
name = 'vlad'
day = 'monday'

d = (age,name,day)

# %d это спецификатор целого числа
age_str = 'привет мне %d лет, меня зовут %s, сегодня %s' % d	#использование кортежа
print(age_str)

d1 = {"name":name,"age":age,"day":day}

age_str = 'привет мне %(age)d лет, меня зовут %(name)s, сегодня %(day)s' % d1	#использование словаря
print(age_str)


percent = 10.54
percent_str = 'Кредитная ставка %.3f%% процента годовых' % percent
print(percent_str)