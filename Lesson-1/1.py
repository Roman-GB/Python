
# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
a = int(input('Введите трехзначное число: '))
sum_dig = 0
mult_dig = 1


while int(a) > 0:
    digit = a % 10
    sum_dig += digit
    mult_dig *= digit
    a = a//10


print('Сумма:', sum_dig)
print('Произведение:', mult_dig)




