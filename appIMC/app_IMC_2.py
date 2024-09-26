def main():

    print("\nCálculo de IMC")
    peso = input("\nDigite seu peso(kg): ")
    altura = input("\nDigite sua altura(m): ")
    imc = calcularImc(peso, altura)
    label = labelImc(imc)

    print(f'\nAltura = {altura}m, Peso = {peso}kg, IMC: {label}\n')

# calcula o índice de massa corporal, conforme fórmula clássica
# Obs: cálculo sempre realizado truncando resultado em duas casa decimais
# IMC = Peso / Altura²
def calcularImc(peso, altura):
        return ((float(peso) / float(altura) ** 2))

# Traduz um valor de IMC em texto conforme a regra abaixo:
# Magreza, quando o resultado é menor que 18, 5 kg / m2;
# Normal, quando o resultado está entre 18, 5 e 24, 9 kg / m2;
# Sobrepeso, quando o resultado está entre 24, 9 e 30 kg / m2;
# Obesidade, quando o resultado é maior que 30 kg / m2;
def labelImc(imc):
    if (imc < 18.5) : return "Magreza"
    if (imc < 24.9) : return "Normal"
    if (imc < 30.0) : return "Sobrepeso"
    return "Obesidade"             

# Este código se propõe a validar o comportamento central do app
# em relação aos cálculos e traduçoes
def sanityCheck():
    print("====================================")
    print("Start running sanity check...\n")

    scenarios = {
        'Magreza':{
            "altura": 1.70,
            "peso": 50.0,
            "imc": 17.30
        },
        'Normal':{
            "altura": 1.70,
            "peso": 70.0,
            "imc": 24.22
        },
        'Sobrepeso':{
            "altura": 1.70,
            "peso": 75.0,
            "imc": 25.95
        },
        'Obesidade':{
            "altura": 1.70,
            "peso": 90.0,
            "imc": 31.14
        }
    }

    for range, values in scenarios.items():        
        imc = round(calcularImc(scenarios[range]['peso'], scenarios[range]['altura']), 2)
        label = labelImc(imc)

        if (imc == scenarios[range]['imc']) : print(f'{range} imc: ok')
        if (label == range) : print(f'{range} label: ok')

    print("\nFinish running sanity check...")
    print("====================================")        
     
sanityCheck()
main()    


