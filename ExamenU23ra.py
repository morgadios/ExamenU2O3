import json

lista = []

def genJSON():
    contactos = [
        ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
        ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
        ("Javier", "Analista de datos", "javier@ejemplo.com"),
        ("Marta", "Experta en python", "marta@ejemplo.com")
    ]

    for cont in contactos:
        n, f, c = cont
        dicc = {
            "nombre": n,
            "funcion": f,
            "correo": c
        }
        lista.append(dicc)
    return lista

data = genJSON()
with open('Contactos.json', 'w') as file:
    json.dump(data, file, indent=4)

print(json)