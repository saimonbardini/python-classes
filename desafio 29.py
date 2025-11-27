vel = int(input('input the velocity: '))
fine = float((vel - 80) * 7)
if vel >=80:
    print('you was fined.')
    if vel > 80:
        print(f'your fine is: R${fine}')