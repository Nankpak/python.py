'''using match to check some conditional
statement'''
name = input("enter your name ").upper()
score = int(input('enter your score '))
bio = {'name': name, 'score': score}
match bio:
    case bio if score >= 70 and score <=100:
        print('you get A')
    case bio if score >= 60 and score < 70:
        print('you get B')
    case bio if score >= 50 and score < 60:
        print('you get C')
    case bio if score >= 45 and score < 50:
        print("you get D")
    case bio if score >= 40 and score < 45:
        print("you get E")
    case bio if score >= 0 and score < 40:
        print('you fail try again next time')
    case _:
        print('invlid score')
print(bio)    
