#словарь
d = { "name":"Сокольники", "buses":[55,669,565],"bench":True }

print(d["name"])

d["light"] = False	#добавление нового ключа-значения в словарь

print(d["light"])

print(d.get("bench1","???"))	#получение значения, которого может не быть 