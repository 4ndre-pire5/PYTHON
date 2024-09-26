print("Números de 0 a 10, mostrados em ordem inversa")
numeros = []
for i in range(11):
    numeros.append(i)

numeros.reverse()
print(numeros)
print("\n")

print("Números pares de 0 a 10")
pares = 0
for i in range(11):
    if (i % 2) == 0:
        pares += 1
        print(i)
print("\n")

print("Soma de números entre 100 e 200")
soma = 0
for i in range(100, 201):
    soma += i
print(soma)
print("\n")

