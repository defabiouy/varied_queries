"""Consumir con Request un recurso  expuesto en la plataforma abierta de web services de la IMM.
El programa pide un string y devuelve todas las calles que en su nombre contengan dicho string
Para implementarlo, el programa consume el recurso http://www.montevideo.gub.uy/ubicacionesRest/calles/?nombre=<substring_a_buscar> y procesa los datos devueltos (devuelve Json, pero solo nos interesa que se devuelva el nombre de la calle)
En caso de no encontrarse, da un mensaje acorde

Ejemplo: Supongamos que nuestro programa reciba “agra”, entonces deberá responder una lista de calles como agraciada y josé Luis villagran (entre otras), ya que contienen "agra"

> Ingrese (sub)string a buscar: agra
> Salida:
Av. Agraciada
José Luis Villagrán
...
...
...
La API completa de la IM puede ser chequeada en: https://github.com/dti-montevideo/servicios-abiertos/blob/master/ubicaciones.md
"""

__author__ = "Fabio Suárez"


import requests, json

print("----------------------------------------")
texto = input("Ingrese el (sub)string a buscar: ")
print("----------------------------------------")

url_base='http://www.montevideo.gub.uy/ubicacionesRest/calles/?nombre='

r = requests.get(url_base+texto, headers={'User-Agent': 'Mozilla/5.0'})

if r.status_code == 200:
    resultado = json.loads(r.text)

    if r.text == '[]':
        print("La consulta no devolvió datos")
    else:
        print("Resultado:\n")
        for calle in resultado:
            print(calle["nombre"])

    print("-----------------------------------------")

else:
    print("Error al consultar la api:", r.status_code)
