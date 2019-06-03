lang = "Языки: Python, PHP, SQL, HTML, Java"
langs_position = lang.find(": ") + 2

langs = lang[langs_position:]

print(langs)

#положение php
second_lang_start_position = lang.find(", ") + 2	#начальная позиция php
second_lang_end_position = lang.find(", ", second_lang_start_position)	#конечная позиция php

second_lang = lang[second_lang_start_position:second_lang_end_position]

print(second_lang)

last_language_position = lang.rfind(", ") + 2
last_language = lang[last_language_position:].strip(".")	#удаление точки из подстроки
print(last_language)