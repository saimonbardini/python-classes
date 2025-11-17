name = input('input your complete name: ')

print(f'your name in all uppercase: {name.upper()}')
print(f'your name in all lowercase: {name.lower()}')
no_spaces = (len(name) - (name.count(' ')))
print(f'your name but not count spaces: {no_spaces}')
print('your name have: {}'.format(name.find(' ')))