def reverse(str):
  size = len(str)
  if(size==0):
    return
  last_char = str[size-1]
  print(last_char, end = "")
  reverse(str[0:size-1])

reverse("India")
