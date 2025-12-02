def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)

criar_carro("Palio", 1999, "ABF-1104", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro(modelo="Palio", ano=1999, placa="AFB-1104", marca="Fiat", motor="1.0", combustivel="Gasolina") #invalido