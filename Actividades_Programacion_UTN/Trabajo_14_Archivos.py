with open("texto.txt","r+") as archivo:
    archivo.seek(7)
    texto = archivo.read()
    print(texto)