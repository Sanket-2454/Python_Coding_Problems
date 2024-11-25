def cone_pattern(num):
  for row in range(1,num+1):
    for space in range(1,num-row+1): # this loop is for space 
      print("-") # here - is considered as a space 
    for col in range(1,row+1):
      print("*",end="")
    print()

cone_pattern(5)
