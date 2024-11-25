def List_to_Dict():
  L1 = input("Enter the list")
  L2 = input("Enter the list")

  d = dict(zip(L1,L2)) # zip map the values between the two list and then dict convert it into the dict
  print(d)

List_to_Dict() # called the function

