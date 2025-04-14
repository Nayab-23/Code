# Calculates the product of the digits of a given number.

# iterative_prod(x): Uses a while loop to repeatedly extract and multiply each digit.


# Example:
# x = 234 → 2 * 3 * 4 = 24
# iterative_prod(234) → 24
# recurprod(234) → 24


def digit_product(x):
    product = 1  
    for i in str(x):  # Convert number to string and iterate over each digit
        y = i
        product *= int(y)  # Convert it back to integer and multiply
    return product




def recurprod(x) :
  if x < 10 : ## will suffice when SINGLE digit
      return x
  else :
      return (x % 10) * recurprod(x // 10)


