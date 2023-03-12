"""∑_(i=a)^n▒∑_(j=b)^m▒(i/j)/(i+2)"""
a = input("Enter a: ")
b = input("Enter b: ")
n = input("Enter n: ")
m = input("Enter m: ")
sum1 = 0.0

try:
    new_n = int(n)
    new_m = int(m)
    for i in range(int(a), new_n+1):
        for j in range(int(b), new_m+1):
            sum1 += (i/j)/(i+2)
    print("Answer is {0}".format(sum1))
except ZeroDivisionError:
    print("Невизначеність: ділення на нуль")
except (TypeError, ValueError):
    print("Ви ввели не цілі числа")

