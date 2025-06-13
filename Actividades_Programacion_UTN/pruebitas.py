animales = [{"perro": [ {"ataque":5, "velocidad":6, "defensa":8 } ]},
            {"gato": [ {"ataque":4, "velocidad":7, "defensa":6 } ]},
            {"loro": [ {"ataque":8, "velocidad":3, "defensa": 2 } ]}]

estudiantes=[{
  "legajo": 1,
  "nombre": "Juan",
  "apellido": "Linarez",
  "edad": 21,
  "notas": [    8,    9,    6  ],
  "programa": { "nombre": "Ingenieria en Informatica", "nivel": "pregrado" },
  "grupos": [    {"nombre": "Club de Ajedrez","descripcion": "Grupo de jugadores de Ajedrez"},
    			{"nombre": "Club de Informatica","descripcion": "Grupo para fanaticos de Tecnologia"}]
},
{
  "legajo": 2,
  "nombre": "Carla",
  "apellido": "Salas",
  "edad": 18,
  "notas": [    7,    5  ],
  "programa": {"nombre": "Medicina","nivel": "pregrado"},
  "grupos": [ {"nombre": "Club de Volleyball","descripcion": "Equipo de Volleyball de la universidad."} ]
}
]
for estudiante in estudiantes:
        for un_dato in estudiante["grupos"]:
            for keys in un_dato:
                if un_dato[keys] == "Club de Informatica":
                    print(un_dato[keys])