def move_zeros(arr):
  return [x for x in arr if x!=0] + [x for x in arr if x==0]
print(move_zeros([0,1,2,0,4,0,5,0]))
