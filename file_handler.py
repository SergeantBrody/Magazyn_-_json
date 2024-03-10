import json


class FileHandler:
    def __init__(self, sciezka_do_pliku_z_historia, sciezka_do_pliku_z_magazynem_i_saldem):
        self.plik_z_historia: str = sciezka_do_pliku_z_historia
        self.plik_z_magazynem_i_saldem: str = sciezka_do_pliku_z_magazynem_i_saldem

    def odczyt_danych_z_pliku_z_magazynem_i_saldem(self):
        with open(self.plik_z_magazynem_i_saldem) as plik:
            dane = json.loads(plik.read())
            dane.get("budzet_firmy")
            print((dane.get("budzet_firmy"), dane.get("magazyn")))
            return dane.get("budzet_firmy"), dane.get("magazyn")

    def odczyt_danych_z_pliku_z_historia(self):
        with open(self.plik_z_historia, "r") as plik:
            dane = json.loads(plik.read())
            return dane

    def zapis_do_pliku_z_magazynem_i_saldem(self, budzet_firmy, magazyn):
        with open(self.plik_z_magazynem_i_saldem, mode="w") as file:
            file.write(json.dumps({
                "budzet_firmy": budzet_firmy,
                "magazyn": magazyn
            }))

    def zapis_do_pliku_z_historia(self, lista_operacji):
        with open(self.plik_z_historia, mode="w") as file:
            file.write(json.dumps(lista_operacji))
