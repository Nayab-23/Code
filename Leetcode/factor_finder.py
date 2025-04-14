
## USING DOUBLE for loops
usr = int(input("Input your factor : "))
factor = []
for i in range(1,usr+1) : ## i will be compared to j till len(usr)

    for j in range(1,usr+1) :

        if i * j == usr :

            factor.append(i)


print(factor)




### EFFICIENT

def factor_finder(number):
    factors = []  # Store factors in a list
    for i in range(1, number + 1):  # Iterate up to number (inclusive)
        if number % i == 0:  # Check if i is a factor
            factors.append(str(i))  # Append factor as string

    return " , ".join(factors)  # Convert list to a comma-separated string

print(factor_finder(60))
