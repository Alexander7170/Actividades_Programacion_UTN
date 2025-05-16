#Ejercicio 3
""""
Ingresar 5 números enteros, distintos de cero.
Informar:
a. Cantidad de pares e impares.
b. El menor número ingresado.
c. De los pares el mayor número ingresado.
d. Suma de los positivos.
e. Producto de los negativos.
"""
contador_numero_pares = 0
contador_numero_inpares = 0
acumulador_numero_positivos = 0
menor_numero = 0
producto_Negativo = 1
par_mayor = 0
flag = True
flag_par_mayor = True
contador = 0
for i in range(5):
    numero = int(input("dime un numero: "))

    if numero == 0:
        print("error, diga culquier numero menos el 0")
    else:                 #cantidad de pares
        if numero % 2 == 0:
            contador_numero_pares += 1
            if flag_par_mayor == True:
                par_mayor = numero
                flag_par_mayor = False
            else:
                if par_mayor < numero:
                    par_mayor = numero
        else:
            contador_numero_inpares +=1
        #menor numero
        if flag == True:
            menor_numero = numero
            flag = False
        else:
            if numero < menor_numero:
                menor_numero = numero
        

        if numero > 0:
            acumulador_numero_positivos += numero
            contador = contador + 1
            if contador == 5:
                producto_Negativo = 0
        else:
            producto_Negativo = producto_Negativo * numero

    
print(""
"")
print(f"los numeros pares son {contador_numero_pares}")
print(f"los numeros impares son {contador_numero_inpares}")
print(f"El menor numero es {menor_numero}")
print(f"De los pares el mayor numero ingresado es {par_mayor}")
print(f"la suma de los numeros positivo es {acumulador_numero_positivos}")
print(f"la multiplicacion de los negativos es {producto_Negativo}")