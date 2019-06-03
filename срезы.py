cardnumber = "2313232332320865"
bank_id = cardnumber[0:4]	#по какой символ исключительно
bank_id1 = cardnumber[:4]	#по какой символ исключительно
last4digits = cardnumber[-4:]	#срез от какого-то символа с конца до конца
last4digits2 = cardnumber[12:len(cardnumber)]	#срез от определенного симвлова по индекс списка
print(bank_id)
print(bank_id1)	
print(last4digits)
print(last4digits2)
print("*"*len(cardnumber[:-4])+cardnumber[-4:])