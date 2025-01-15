def custom_sort(arr):
  mid = len(arr)//2

  first_half = sorted(arr[:mid])
  second_half = sorted(arr[mid:])
  result = first_half + second_half
  return result 
arr = [10,2,0,3,4,5,6]
final_res = custom_sort(arr)
print(final_res)
