texto = input ("Informe seu texto: ")
#texto = ""
VOGAIS = "AEIOU"

#Exemplo com iterável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")
else:
    print()    
    print("Executa no final do laço")  


#Exemplo com a função built-in-range
for numero in range(5, 51, 5) :
    print(numero, end = "") 