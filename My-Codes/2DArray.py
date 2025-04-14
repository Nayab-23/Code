# display_array function would print a grid-like output for a 2D array:

def display_array(array):
  for row in array:
      print(" ".join(f"{num:3}" for num in row))
  print()

## Another method of declaring 2D Arrays
Array = [[0 for X in range(3)] for Y in range(20)]

# Example 2D Array (Matrix)
ArrayData = [
  [1, 23, 456, 7],
  [89, 10, 234, 5],
  [67, 89, 123, 9],
  [6, 78, 901, 12]
]

display_array(ArrayData)
