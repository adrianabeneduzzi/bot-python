contatos = {"bene@teste.com": {"nome": "Adriana", "telefone": "4040-4040"}}

#contatos["chave"] # simulação de erro

resultado = contatos.get("chave")
print(resultado)

resultado = contatos.get("chave", {})
print(resultado)

resultado = contatos.get(
    "bene@teste.com", {}
)
print(resultado)