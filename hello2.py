# -*- coding: utf-8 -*-
#импорт настроек 
import encodings.aliases

#получение алиасов кодировок
arr = encodings.aliases.aliases

#создание списка из названий кодировок
#список заключается в скобки
keys = list(arr.keys())

#сортировка ключей
keys.sort()

#перебор ключей по списку с выводом в консоль 
for key in keys:
	print ("%s => %s" % (key,arr[key]))
