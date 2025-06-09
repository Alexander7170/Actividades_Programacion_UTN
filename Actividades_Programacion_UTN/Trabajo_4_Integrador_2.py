# flag = True
# contado_jugadores = 0
# contador_a = 0
# contador_b = 0
# acumulador_edad = 0
# menor_edad = 0
# jugador_menor = "nadie"
# categoria_menor = "nadie"
# saque_plano = 0
# saque_liftado = 0
# saque_cortado = 0
# saque_str = ""
# while flag == True:
#     nombre_jugador = input("diga su nombre: ")

#     edad = int(input("diga su edad: "))
#     while edad <= 0:
#         edad = int(input("eror, diga de nuevo su edad: "))

#     cantidad_puntos = int(input("dime tu cantidad de puntos: "))
#     while cantidad_puntos <= 0 or cantidad_puntos > 60:
#         cantidad_puntos = int(input("error, dime tu cantidad de puntos: "))

#     partidas_ganadas = int(input("Dime cuantas partidas ganaste: "))
#     while partidas_ganadas <= 0 or partidas_ganadas > 35:
#         partidas_ganadas = int(input("error, dime cuantas partidas ganaste: "))

#     tipo_saque = input("dime tu tipo de saque (plano/cortado/liftado): ")

#     categoria = input("dime tu categoria (elite/expeto/avanzado): ")

#     contado_jugadores += 1

#     if categoria == "elite" and tipo_saque == "plano" and edad >= 19 and edad <= 25:
#         contador_a += 1

#     if cantidad_puntos > 50:
#         menor_edad = edad
#         jugador_menor = nombre_jugador
#         categoria_menor = categoria
#         if menor_edad < edad:
#             menor_edad = edad
#             jugador_menor = nombre_jugador
#             categoria_menor = categoria

#     if categoria == "experto":
#         contador_b += 1
#     elif categoria == "avanzado":
#         acumulador_edad += edad
#     elif categoria == "elite":
#         if tipo_saque == "plano":
#             saque_plano += 1
#         elif tipo_saque == "liftado":
#             saque_liftado += 1
#         elif tipo_saque == "cortado":
#             saque_cortado += 1

#     continuar = input("quieres seguir(s/n)?: ")
#     if continuar == "n":
#         flag = False
# saque_mas_usado = saque_plano
# saque_str = "saque plano"
# if saque_mas_usado < saque_cortado:
#     saque_mas_usado = saque_cortado
#     saque_str = "saque cortado"
# if saque_mas_usado < saque_liftado:
#     saque_mas_usado = saque_liftado
#     saque_str = "saque liftado"
# porcentaje = contador_b / contado_jugadores * 100
# promedio_edad = acumulador_edad / contado_jugadores

# print(f"la cantidad de jugadores de elite con saque plano y que este entre los 19 y 25 años son {contador_a}")
# print(f"el jugador de menor edad y con mas de 50 puntos es {jugador_menor} de categoria {categoria_menor} ")
# print(f"el porcetanje de jugadores en la categoria experto es de un %{porcentaje}")
# print(f"El promedio de edad de los jugadores que eligieron categoria avanzada es {promedio_edad}")
# print(f"El saque mas usado en la categoria elite es {saque_str}")