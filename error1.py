import traceback

while True:
    x = input("Введите число\n")

    try:
        x = float(x)
        if x == 1:
            x = None
        y = 100/x
        break
    except (ValueError,NameError):
        print("Ошибка - введите число")
    except TypeError:
        print('Ошибка, не вводите 1')    
    except Exception:
        # y = "бесконечность" 
        # break
        # print(traceback.format_exc())
        f = open('log.txt','a+')
        traceback.print_exc(file=f)
        f.close()

print(y)