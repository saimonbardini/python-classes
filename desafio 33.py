n1 = float(input('input the first number: '))
n2 = float(input('input the second number: '))
n3 = float(input('input the third number: '))

if n1 < n2 and n1 < n3:
    sml = n1
else:
    big = n1

if n2 <n1 and n2 < n3:
    sml = n2
else:
    big: n2

if n3 < n1 and n3 < n2:
    sml: n3
else:
    big = n3


print(f"""smaller: {sml} 
bigger: {big}""")