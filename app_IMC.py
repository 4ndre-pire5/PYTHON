print("\nCálculo de IMC")
peso = input("\nDigite seu peso(kg): ")
altura = input("\nDigite sua altura(m): ")
imc = (float(peso)/(float(altura)**2))

print(f'\nSeu IMC é igual a: {round(imc, 2)}')

if imc <= 18.5 : range = "Magreza"
if imc > 18.5: range = "Normal"
if imc > 24.9 : range = "Sobrepeso"
if imc > 30: range = "Obesidade"

print(f'\nSeu IMC é classificado como: {range}\n')