# desafio


print('Loop com o break: ')

for numero in range(1,11):
    if numero > 5:
        break
    print(numero)


print('Loop com o continue: ')

for numero in range(1,11):
    if numero == 5:
        continue # o continue não imprimir a condição acima!
    print(numero)
