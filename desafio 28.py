import random

num = random.randint(0, 5)

a = 'GUESS THE NUMBER'
print('{:=^30}'.format(a))

user_num = int(input("the number is..."))
if  user_num == num:
    print('he got it right')
else:
    print(f'wrong, the correct response is: {num}')
