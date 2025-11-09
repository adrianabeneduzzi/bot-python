#Exemplo 1 - Break + Continue
#opcao = -1
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

    if numero % 2 == 0:
      continue   
    
    print(numero)

#Exemplo 2 - Break
"""for numero in range(100):

    if numero == 12:
        break

    print(numero, end=" ")"""

#Exemplo 3 - Continue
"""for numero in range(100):

    if numero % 2 == 0:
       continue

    print(numero, end=" ")"""