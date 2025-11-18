contatos = {"adrianagb@teste.com": {"nome": "Adriana", "telefone": "7045-8989"}}

copia = contatos.copy()
copia["adrianagb@teste.com"] = {"nome": "Adri"}

print(contatos["adrianagb@teste.com"])

print(copia["adrianagb@teste.com"])
