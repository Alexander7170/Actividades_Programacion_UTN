nombre = "alex"
Score = 5

archivo = open("Score.csv","w+")

archivo.write("Nombre ; Score \n")
archivo.write("alex;5")
archivo.seek(0)
linea = archivo.readline()

print(linea)

archivo.close()
