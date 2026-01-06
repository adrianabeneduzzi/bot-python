def meu_gerador(numeros: list[int]):    
    for numero in numeros:
        yield numero * 2 #Quando for simples a estrutura usa gerador

for i in meu_gerador(numeros=[1, 2, 3]):
    print(i)