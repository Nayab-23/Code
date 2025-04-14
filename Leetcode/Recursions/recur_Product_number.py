# Calculates the product of the digits of a given number.

# recurprod(x): Uses recursion to multiply the last digit with the product of the remaining digits.

# Example:
# x = 234 → 2 * 3 * 4 = 24
# iterative_prod(234) → 24
# recurprod(234) → 24


def recurprod(x) :
  if x < 10 :
      return x
  else :
      return (x % 10) * recurprod(x // 10)