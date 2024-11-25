def common_letter_between_twostring():

  str1 = input("Enter the String1:")
  str2 = input("Enter the String2:")

# Convert to set to find the unique value
  s1 = set(str1)
  s2 = set(str2)
  result = s1 & s2
  print(result)
common_letter_between_twostring()
