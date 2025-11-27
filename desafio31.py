dist = float(input('insert the distance of your trip: '))
if dist < 200:
    dist *= 0.50
    print(f'your ticket cost: R${dist}')
else:
    dist *= 0.45
    print(f'your ticket cost: R${dist}')