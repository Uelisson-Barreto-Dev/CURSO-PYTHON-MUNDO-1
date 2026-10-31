n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
sub = n1 - n2
rest = n1 % n2
print(f'A soma entre {n1} e {n2} vale {s:.2f}')
print(f'A subtração entre {n1} e {n2} é igual a {sub:.2f}')
print(f'A multiplicação entre {n1} e {n2} é gual a {m:.2f}')
print(f'A divisão entre {n1} e {n2} é igual a {d:.2f}')
print(f'A divisão inteira entre {n1} e {n2} é igual a {di:.2f}')
print(f'O número {n1} elevado a {n2} é igual a {e:.2f}')
print(f'o resto da divisão entre {n1} e {n2} é igual a {rest:.2f}')