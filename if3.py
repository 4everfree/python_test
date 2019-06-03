age = 27
sex = 'f'
credit = True
has_military_id = True

if age >= 18 and age< 65:
    if age < 27 and sex == 'm' and not has_military_id:
        credit = False
    if(age == 22 or has_military_id) and sex == 'f':
        credit = False     
else:
    credit = False 

if credit:
    print('Кредит одобрен!')
else:
    print('Кредит не одобрен')        