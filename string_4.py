#Strings triplas
nome = "Adriana"

mensagem = f"""
    Olá meu nome é {nome},
Eu estou aprendendo Python.
    Essa mensagem tem diferentes recuos.
"""
print(mensagem)

print("""
      ============= MENU =============

      1 - Depositar
      2 - Sacar
      0 - Sair

      =================================
      
            Obrigado por preferir nosso sistema!!!      
      
""")

PI = 3.14159 
print(f"Valor de PI: {PI:.2f}")

curso = "Python" 
print(f"Bem vindo ao curso de {curso.upper()}!")

texto = " Python y".lstrip()
print(texto)