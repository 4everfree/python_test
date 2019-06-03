lang = "Python" #нельзя изменить строку или срез - это неизменяемый тип данных

language_lower = "p" + lang[1:]
print(language_lower)

lang_f = lang.lower() #приведение заглавной буквы к строчной
print(lang_f)

lang = "p" + lang[1:]
print(lang)
