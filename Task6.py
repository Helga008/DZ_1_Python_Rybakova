# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = int(input('Введите шестизначный номер билета: '))
if number > 999999 or number < 100000:
    print('Число не является шестизначным')
else:
    n1 = number // 100000
    n2 = int((number - (n1 * 100000)) // 10000)
    n3 = int((number - (number // 10000 * 10000))//1000)
    n4 = int((number - (number // 1000 * 1000))//100)
    n5 = int((number - (number // 100 * 100))//10)
    n6 = int(number % 10)
    if n1 + n2 + n3 == n4 + n5 + n6:
        print('Поздравляем, билет счастливый!')
    else:
        print('Это не счастливый билет')

        