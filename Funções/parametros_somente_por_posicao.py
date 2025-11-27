def criar_carro(modelo, ano, placa, /, marca, motor, combustível):
    print(modelo, ano, placa, marca, motor, combustível)

criar_carro("Palio", 1999, "BEB-1104", "Fiat", motor="1.0", combustível="Gasolina") #válido
#criar_carro(modelo = "Palio", ano = 1999, placa="BEB-1104", marca="Fiat", motor="1.0") #inválido