# Atualiza o dicionário com outro dicionário

contatos = {"belina@teste.com": {"nome": "Belina", "telefone": "2356-8963"}}

contatos.update({"belina@teste.com": {"nome": "Lina"}})
print(contatos)

contatos.update({"aleci@gmail.com": {"nome": "Aleci", "telefone": "2356-8181"}})
print(contatos)