num = int(input("Enter the number:"))
for row1 in range(num,0,-1):
  for col1 in range(1,num+1):
  print("*",end="")
for row in range(1,num+1):
  for col in range(1,num+1):
    print("*",end= "")
  print()
