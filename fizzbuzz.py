def fizzbuzz(n):
    list = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            if i % 5 == 0:
                list.append("fizzbuzz")
            else:
                list.append("fizz")
        elif i % 5 == 0:
            list.append("buzz")
        else:
            list.append(i)
    return list

n = int(input("Enter a number: "))
print(fizzbuzz(n))