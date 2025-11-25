def salvar_carro(marca, modelo, ano, placa):
    
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carro("Fiat", "Palio", 1999, "AFB-1104") #N]ao efetivos para alterações de ordenações
salvar_carro(marca="Fiat", modelo="Palio", ano="1999", placa="AFB-1104")
#salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "AFB-1104"})