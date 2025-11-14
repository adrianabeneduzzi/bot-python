gaveta = ["meia", "lenço", "camisa", "cinto", "pijama"]
gaveta.sort()  
print(gaveta)

gaveta = ["meia", "lenço", "camisa", "cinto", "pijama"]
gaveta.sort(reverse=True)  
print(gaveta)

gaveta = ["meia", "lenço", "camisa", "cinto", "pijama"]
gaveta.sort(key=lambda x: len(x))  
print(gaveta)

gaveta = ["meia", "lenço", "camisa", "cinto", "pijama"]
gaveta.sort(key=lambda x: len(x), reverse=True)  
print(gaveta)