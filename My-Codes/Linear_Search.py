def linear_search(x, arr):
  for i in range(0, len(arr) - 1):
    j = arr[i] + arr[i + 1]
    if j == x:
      return x

  return -1


arr = [1, 3, 4, 5, 3, 2, 4, 5, 5]
x = 10
