# task 2
# создать **рекурсивную** функцию fibonacci, которая принимает целое число N
# и возвращает N-ное число в последовательности Фибоначчи
# важно - у вас при больших числах (больше 20 и далее) - программа будет тупить
# пока что это норма

# дополнить результат task2 предыдущей лекции (фибоначчи)
# самописным кэшем и проверить на больших числах

# для себя сравните скорости выполнения fib_cached и fib_regular
# на больших числах (больше 60)
import time

MY_CACHE: dict[str, str] = {}
def calculate_surname(name: str = "Vova"):
    if name in MY_CACHE:
        return MY_CACHE[name]
    time.sleep(2)
    surname = name + "4kin"
    MY_CACHE[name] = surname
    return surname

'''
rec = int(input("Введите ваше число (позязя): "))
strok=[]
def fubon(rec):
    spus = []
    for i in range(rec):
        number=[1]
        if i>0:
            pred_num=spus[i-1]
            spus.append(pred_num [i] + pred_num[i+1])
            print(spus)
        else:
            break
fubon(rec)
'''

rec = int(input("Введите ваше число (позязя): "))
spis = {0: '0',1: '1',2:'1',3:"2",4:'3', 5:'5', 6:'8', 7:'13', 8:'21', 9:'34', 10:'55', 11:'89', 12:'144', 13:'233', 14:'377', 15:'610', 16:'987', 17:'1597', 18:'2584', 19:'4181', 20:'6765'}
def fib(rec):
    if rec ==0:
        print (spis[0])
    elif rec == 1 or rec == 2:
        print (spis[1])
    else:
        print(spis[rec])
fib(rec)


