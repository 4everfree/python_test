domain1 = 'www.yandex.ru'
domain2 = 'google.com'

print(domain1.find(".ru"))
print(domain2.find(".ru"))	# возвращает -1 если такого символа нет

#чем заканчивается
print(domain1.endswith('.ru'))	#возвращает True
print(domain2.endswith('.ru'))	#возвращает False


#чем начинается
print(domain1.startswith('www'))	#возвращает True
print(domain2.startswith('www'))	#возвращает False

#является ли первая буква строчной
print(domain1.islower())	#возвращает True

#является ли первая буква заглавной
print(domain2.isupper())	#возвращает False
