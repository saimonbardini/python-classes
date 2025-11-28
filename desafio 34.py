wage = float(input('insert your salary: R$'))

if wage >1250:
    wage *= 1.10
else:
    wage *= 1.15

print(f'your new salary is: R${wage:.2f}')