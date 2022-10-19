# Modul Dobavljac:

import math

class Dobavljac:
    def __init__(self, dob, god, kol, cena, ocena):
        if len(dob) == 0:
            print("Dobavljac mora imati ime.")
            exit()
        
        if god < 1900:
            print("Godina nije ispravna.")
            exit()

        if kol < 500:
            print("Godisnja kolicina pro. voca nije ispravna.")
            exit()
        
        # cena

        # ocena

        self.dob = dob
        self.god = god
        self.kol = kol
        self.cena = cena
        self.ocena = ocena
    
    def get_adekvatnost(self):
        return (self.ocena * math.sqrt(self.kol)) / (3.7 * (1000 + self.cena))
    
def load (fajl):
    lista = []

    try:
        with open(fajl, "r") as ulaz:
            while True:
                god_str = ulaz.read(5).strip()

                if god_str == '':
                    break

                god = int(god_str)
                kol = int(ulaz.read(5).strip())
                ocena = float(ulaz.readline().strip())

                cena = float(ulaz.read(8).strip())
                naziv = ulaz.readline().strip()
                
                d = Dobavljac(naziv, god, kol, cena, ocena)

                lista.append(d)
    
    except:
        print("Doslo je do greske")
        exit()
    
    lista.sort(key=lambda d : d.get_adekvatnost(), reverse=True)

    return lista