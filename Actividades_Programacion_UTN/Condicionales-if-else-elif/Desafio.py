"""
Cliente Residencial:
Si el consumo es menor a 30 m³, se aplica una bonificación del 10% sobre el costo del consumo.
Si el consumo supera los 80 m³, se aplica un recargo del 15% sobre el costo del consumo.
Cliente Comercial:
Si el consumo es superior a 150 m³, se aplica una bonificación del 8% sobre el costo del consumo.
Si el consumo supera los 300 m³, la bonificación aumenta al 12%.
Si el consumo es menor a 50 m³, se aplica un recargo del 5%.
Cliente Industrial:
Si el consumo es superior a 500 m³, se aplica una bonificación del 20% sobre el costo del 
consumo.
Si el consumo supera los 1,000 m³, la bonificación aumenta al 30%.
"""
tipo_de_cliente = input("Dime que tipo de cliente eres(Residencial/Comercial/industrial): ")
metros_cubicos_consumidos = int(input("dime cuantos metros cubicos consumiste: "))
tarifa_base = 7000
costo_metro_cubico = 200
bonificacion = 0
recargo = 0
descuento_adicional = 0
IVA = 0.21
if tipo_de_cliente == "residencial":
    if metros_cubicos_consumidos < 30:
        bonificacion = 8
    elif metros_cubicos_consumidos > 80:
        recargo= 15
elif tipo_de_cliente == "comercial":
    if metros_cubicos_consumidos < 50:
        recargo = 5
    elif metros_cubicos_consumidos > 150 and metros_cubicos_consumidos < 300:
        bonificacion = 8
    elif metros_cubicos_consumidos > 300:
        bonificacion = 12
else:
    if metros_cubicos_consumidos > 1000:
        bonificacion = 30
    elif metros_cubicos_consumidos > 500:
        bonificacion = 20
    elif metros_cubicos_consumidos < 200:
        recargo = 10

subtotal = costo_metro_cubico * metros_cubicos_consumidos + tarifa_base
if subtotal < 35000 and tipo_de_cliente == "residencial":
    bonificacion += 5
subtotal_con_descuentos_recargas = subtotal + (subtotal * recargo / 100) - (subtotal * bonificacion / 100)
total = subtotal_con_descuentos_recargas + subtotal_con_descuentos_recargas * IVA

print(f"El subtotal es: ${subtotal}")
print(f"Con una bonificacion de {bonificacion}%")
print(f"Con un recargo de {recargo}%")
print(f"Con un subtotal incluido descuentos y bonificaciones es ${subtotal_con_descuentos_recargas}")
print(f"Con IVA aplicado ${total}")
print(f"Total a final a pagar es ${total}")