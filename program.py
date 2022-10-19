# Glavni modul programa:

import dobavljac
import json

lista = dobavljac.load("dobavljaci.txt")

suma = sum(d.get_adekvatnost() for d in lista)
sr_vr = suma / len(lista)

lista2 = list(filter(lambda d : d.get_adekvatnost() >= sr_vr, lista))

izlaz = f'adekvatnih_{len(lista2)}.json'
json.dump(lista2, open(izlaz, "w"), default=lambda d : d.__dict__)