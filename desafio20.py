from random import shuffle

name1 = input('first name: ')
name2 = input('second name: ')
name3 = input('third name: ')
name4 = input('fourth name: ')
list = [name1, name2, name3, name4]

shuffle(list)

print(f'the selected students is: {list}')