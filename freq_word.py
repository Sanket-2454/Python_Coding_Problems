def frequancy_word():
  str = input("Enter the string")
  li = str.split() # spliting the string and converted into the string
  d = {}
  for i in li:
    if i not in d.keys(): # finding the value not in the dict
      d[i] = 0
    d[i] = d[i] + 1
print(d)
    
