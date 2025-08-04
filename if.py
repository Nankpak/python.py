number = float(input("enter your score  "))
if number >= 70 and number <= 100:
   print("you get A")
elif number >= 50 and number <= 60.9:
  print("you get B")
elif number >= 40 and number <=49.9:
   print("you get C")
elif number >=30 and number <=39.9:
   print("you get D")
elif number >= 0 and number <=30:
   print("you fail score")
else:
   print(" invalid range")
