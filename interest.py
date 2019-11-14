#Norma
#interest

P = 10000
n = 12
rate = 0.08
t = int(input("Number of years: "))

b = n*t
r = rate/n +1

def power(r,b):
    result = 1  # local variables can't be seen outside function

    for counter in range(b):
        result = result * r

    return result

x = power(r,b)

def amount(P, x):
    pay = P*x
    return pay

A = amount(P,x)

print("Final amount paid after ", t," years is $", A)