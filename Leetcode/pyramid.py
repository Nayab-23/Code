n = int(input("How many rows of stars do you want? "))

for i in range(1, n+1):  # Loop from 1 to n
    print((n-i) * ' ' + i * '* ')
