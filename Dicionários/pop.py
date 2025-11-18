# Remove uma chave do dicionário e também insere um valor padrão

contatos = {"bene@teste.com": {"nome": "Adriana", "telefone": "5050-5023"}}

resultado = contatos.pop("bene@teste.com")
print(resultado)

resultado = contatos.pop("bene@teste.com", {})
print(resultado)

resultado = contatos.pop("bene@teste.com", "outro exemplo")
print(resultado)