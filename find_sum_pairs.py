def find_pairs(arr,target):
  for i in range(len(arr)):
    for j in range(i+1,len(arr)):
      if arr[i] == arr[j]:
        continue
      elif arr[i] + arr[j] == target:
        print(i, j)
arr = [1,2,3,9,6,7,8,5]
result = find_paris(arr,5)
print(result) 
    
