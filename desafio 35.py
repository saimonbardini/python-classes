r1 = float(input('input length'))
r2 = float(input('input length'))
r3 = float(input('input length'))

if r1 < (r2 + r3) and r2 < (r1 + r3) and r3 < (r1 + r2):
    print('can form a triangle')
else:
    print('it cannot form a triangle')