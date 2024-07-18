# Yio

import time
meme_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "AGGRO":"Ponerne agresivo",
            "AESTHETIC":"algo lindo",
            "GHOSTEAR":"Dejar en visto un mensaje de otra persona",            }
word = input("Escribe una palabra que no entiendas (¡con mayúsculas!): ")
for i in range(100):
    print("Hola!,Bienvenido al diccionario de palabras de generacion z busque aqui su significado")

    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("No se encrontro, ponga otra")
