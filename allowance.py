print("allowance is 2000 naira only")

Allowance = 2000
Allowance -= 400
print(f"the remain balance after book was bought is {Allowance}")
Allowance += 100
print(f"after i found 100 naira the new balance is {Allowance}")
Allowance -=250
print(f"after spending of on snack the new balance is {Allowance}")
percent = 25/100
percent *= Allowance
Allowance -= percent
print("After 25% of used the allowance is", Allowance)
onethird = 1/3
onethird *= Allowance
Allowance -= onethird
print("After onethird been used the allowance become", Allowance)
Allowance //=2
print("After the allowance was equally divided for saving and tithe balance become", Allowance)
Allowance %=100
print("The remaining balance is now ", Allowance)
