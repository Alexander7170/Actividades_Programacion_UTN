"""
Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:
6, 7, 8, 9 y 10  ---> Promoción directa, la nota es ...
4 y 5                ---> Aprobado, la nota es ...
1, 2 y 3            ---> Desaprobado, la nota es ...

"""
from random import*
numero_random = randint (0, 10)
if numero_random < 4:
    print(f"Desaprobado, tu nota fue {numero_random}")
elif numero_random < 6:
    print(f"Aprobado, tu nota fue {numero_random}")
else:
    print(f"Promocion directa, tu nota fue {numero_random}")