#Norma
#sunrange.py

start = int(input("Input starting integer: "))
stop = int(input("Input stopping integer: "))

if start <= stop:
    def epsilon(start, stop):
        total = 0
        while start <= stop:
            total = total + start**2
            start = start+1
        return total


    result = epsilon(start, stop)

    print(result)
else:
    def epsilon(start, stop):
        total = 0
        while stop <= start:
            total = total + stop**2
            stop = stop+1
        return total

    result = epsilon(start, stop)

    print(result)