import time
time.sleep(3)
print("lecture-6")
def def_name(names:str = "notWowa", age:int = 18):
    print(f"hello{names}, age {age}")
#if __name__ = "__main___" :
print(def_name('andrei'))

from functools import lru_cache
#_ = def_name("notIlya")

def my_calplay(name:str = "notWowa"):
    if name in MY_CASH.keys():
        return MY_CASH(None)
    time.sleep(2)
    surname = "wowa" + "chin"
    MY_CASH(None) = surname
    return 

MY_CASH = dict(str, str) = ("")
print(my_calplay('ilia'))



# дополнить результат task2 предыдущей лекции (фибоначчи)
# самописным кэшем и проверить на больших числах

# для себя сравните скорости выполнения fib_cached и fib_regular
# на больших числах (больше 60)

MY_CACHE: dict[str, str] = {}
def calculate_surname(name: str = "Vova"):
    if name in MY_CACHE:
        return MY_CACHE[name]
    time.sleep(2)
    surname = name + "4kin"
    MY_CACHE[name] = surname
    return surname