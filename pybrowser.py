print("""
**********************
──▄────▄▄▄▄▄▄▄────▄───
─▀▀▄─▄█████████▄─▄▀▀──
─────██─▀███▀─██──────
───▄─▀████▀████▀─▄────
─▀█────██▀█▀██────█▀──
----------------------
> creador: migue-280
> script: PyBrowser
> mas scripts: https://github.com/migue-280
**********************
""")

from googlesearch import search

google_query = str(input("INTRODUSCA UN TERMINO DE BUSQUEDA: "))
print("")
print("Realizando la busqueda...")
print("Filtrando resultados...")
print("")
for i in search(google_query, start = 0, pause = 2):
	print(i)
