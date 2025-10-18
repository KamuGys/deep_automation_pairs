name = str(input("Введите любое имя на ваш вкус (позязя): "))
def change_names(name):
    resilt =''
    for i, sumv in enumerate(name):
        if i% 2 ==1:
            resilt += sumv.upper()
        else: 
            resilt += sumv.lower()
    return resilt

def greet (name):
    print(f"Hello {name}")

new_name=change_names(name)
greet(new_name)