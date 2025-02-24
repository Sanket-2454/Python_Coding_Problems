def sort_arr(arr):
  n = len(arr) # length of the array 
  for i in range(n):
    for j in range(n-i-1):
      if arr[j] > arr[j+1]:
        arr[j],arr[j+1] = arr[j+1], arr[j] # swapping 

      arr.sort()
  return arr[-1]* arr[-2]

arr = [1, 7, 3, 4, 9, 5]
result = sort_arr(arr)
print(result)
