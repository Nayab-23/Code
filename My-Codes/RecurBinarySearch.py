## for 1D Array

def binary_search_1d(arr, low, high, target):
  if high >= low:
      mid = (low + high) // 2

      if arr[mid] == target:
          return mid
      elif arr[mid] > target:
          return binary_search_1d(arr, low, mid - 1, target)
      else:
          return binary_search_1d(arr, mid + 1, high, target)

  return -1  # Not found


## for 2D Array

def binary_search_2d(matrix, row, low, high, target):
  if high >= low:
      mid = (low + high) // 2

      if matrix[row][mid] == target:
          return (row, mid)
      elif matrix[row][mid] > target:
          return binary_search_2d(matrix, row, low, mid - 1, target)
      else:
          return binary_search_2d(matrix, row, mid + 1, high, target)

  return None  # Not found in the row

def search_2d_matrix(matrix, target):
  for row in range(len(matrix)):  # Check each row
      result = binary_search_2d(matrix, row, 0, len(matrix[row]) - 1, target)
      if result:
          return result  # If found, return (row, col)

  return -1  # Not found in the entire matrix
