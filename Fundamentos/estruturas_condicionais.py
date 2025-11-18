MAIOR_IDADE = 18
IDADE_ESPECIAL = 16

idade = int(input("Informe sua idade: "))

#Exemplo 1

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH. ")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH.")

#Exemplo 2

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH. ")
else:
    print("Ainda não pode tirar a CNH.")

#Exemplo 3

if idade >= MAIOR_IDADE:
    print("Maior idade, pode tirar a CNH. ")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer as aulas teóricas,mas não pode fazer aulas práticas. ")
else:
    print("Ainda não pode tirar a CNH.")