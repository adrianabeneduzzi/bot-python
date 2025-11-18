nome = "Adriana"
idade = 36
profissao = "Engenheira de Qualidade de Software"
linguagem = "Python"
saldo = 45.435

dados = {"nome": "Adriana", "idade": 36}

print("Nome: %s Idade: %s" % (idade, nome))
print("Nome: %s Idade: %s" % (nome, idade))

print("Nome: {} Idade: {}". format(nome, idade))
print("Nome: {} Idade: {}". format(idade, nome))

print("Nome: {0} Idade: {1}". format(nome, idade))
print("Nome: {0} Idade: {1} Nome: {0} {0}". format(nome, idade))

print("Nome: {nome} Idade: {idade}". format(nome=nome, idade=idade))
print("Nome: {name} Idade: {age}". format(name=nome, age=idade))
print("Nome: {name} Idade: {age} {name} {name} {age}". format(name=nome, age=idade))
print("Nome: {nome} Idade: {idade}".format(**dados))

print(f"Nome: {nome} Idade: {idade}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}")
print(f"Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}")