mylist = [1, 2, 3, 4, 5]

def somar(list):
    soma = 0
    # for num in list:
    #     soma += num
    soma = sum(list)

    return soma

result = somar(mylist)
print(result) 