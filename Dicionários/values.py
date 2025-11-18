# Não retorna chaves, apenas valores das chaves

contatos = {
    "primavera@gmail.com": {"nome": "Primavera", "telefone": "88888-8888"},
    "verao@gmail.com": {"nome": "Verão", "telefone": "7777-7777"},
    "outono@gmail.com": {"nome": "Outono", "telefone": "3333-3333"},
    "inverno@gmail.com": {"nome": "Inverno", "telefone": "1111-1111"},
}

resultado = (
    contatos.values()
)
print(resultado)