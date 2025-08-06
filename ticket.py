'''ticket can be sell to an adult only if you are 18 years and above
and 60 years and above will be giving a discount, 12 and not equal to 18 years is a teenage
ticket if you are lessthan 12 your ticket is for kids'''

age = int(input('enter your age '))

if age >= 18:
   print("you can buy ticket")
   if age >= 60:
      print("senior discount")
else:
  if age >= 12:
   print('teen ticket')
  else:
   print("kids ticket")

'''checking budget to know which phone is 
suitable for you to access'''

budget = float(input('enter your budget '))
if budget >= 500:
   if budget >=1000:
      print("Google Pixel 9pro")
   else:
      print('Iphone')
else:
   if budget >= 200:
      print('Redmi')
   else:
      print('save more')

 '''below is a student if he has registered he will sit for exam as well access the
 internet else he should check the internet connection or pay his school first'''

student = {'name':'legolas','Registered': True, 'paid':True, 'has_airtime':False}
if student['Registered']:
   if student['paid']:
       if student['has_airtime']:
          print("you can sit for exam")
       else:
          print("check your internet")
   else:
      print('pay your fees')
else:
    print("access denied")
       
