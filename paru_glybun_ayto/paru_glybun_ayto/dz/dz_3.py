#вывести треугольник паскаля с нормальными пробелами с введённым числом до 9
user_nimber = int(input("Введите ваше число (позязя): "))
treyg =[]
for i in range(user_nimber):
    strok=[1]
    if i > 0:
        pred_strok= treyg[i-1]
        for i2 in range(len(pred_strok)-1):
            strok.append(pred_strok[i2] + pred_strok [i2+1])
        strok.append(1)
    treyg.append(strok)
for strok in treyg:
    strok_str = ' '.join(str(x) for x in strok)
    print(strok_str)