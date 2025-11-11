#Exemplo 1
nome = "aDRiaNA"


print(nome.upper())
print(nome.lower())
print(nome.title()) 

#Exemplo 2
texto = " Olá mundo!    "

print(texto + ".")
print(texto.strip() + ".")
print(texto.rstrip() + ".")
print(texto.lstrip() + ".")

#Exemplo 3
menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))

#Exemplo 4
for letra in menu:
    print(letra, end="-")
print()