import json

data = r"C:\Users\marlo\data.json.json"

with open(data, encoding="utf-8") as archivo:
    datos = json.load(archivo)

# Consulta 1: Imprime todos los títulos de las películas, que es la lista principal
print("Títulos de todas las películas:")
for pelicula in datos["peliculas"]:
    print("-", pelicula["titulo"])

# Consulta 2: Accede e imprime el nombre del director de "Scarface"
print("\nDirector de 'Scarface':")
for pelicula in datos["peliculas"]:
    if pelicula["titulo"] == "Scarface":
        print(pelicula["director"]["nombre"])

# Consulta 3: Filtra e imprime películas dirigidas por Martin Scorsese
print("\nPelículas dirigidas por Martin Scorsese:")
for pelicula in datos["peliculas"]:
    if pelicula["director"]["nombre"] == "Martin Scorsese":
        print(f"- {pelicula['titulo']} ({pelicula['año']})")
