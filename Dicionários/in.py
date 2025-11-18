# Verifica se existe uma chave do dicionário

contatos = {
    "bene@teste.com": {"nome": "Bene", "telefone": "2356-4589"},
    "benuto@teste.com": {"nome": "Bene", "telefone": "2356-1289"},
    "vlar@teste.com": {"nome": "Bene", "telefone": "2356-4525"},
    "aparecida@teste.com": {"nome": "Bene", "telefone": "5656-4589"},
}

resultado = "bene@teste.com" in contatos
print(resultado)

resultado = "testenuvem@gmail.com" in contatos
print(resultado)

resultado = "idade" in contatos["bene@teste.com"]
print(resultado)

resultado = "telefone" in contatos["benuto@teste.com"]
print(resultado)