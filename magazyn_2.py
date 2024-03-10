from file_handler import FileHandler


'''
budzet_firmy = 100000

magazyn = [
    {
        "nazwa_produktu": 'Razer Deathadder',
        "producent": 'Razer',
        "ilosc_sztuk": 5,
        "ilosc_sprzedanych_sztuk": 0,
        "cena": 120.00,

    }
]
'''

#lista_operacji = []
koniec_programu = False
filehandler = FileHandler(sciezka_do_pliku_z_historia="historia.json",
                          sciezka_do_pliku_z_magazynem_i_saldem="magazyn_i_saldo.json")
budzet_firmy, magazyn = filehandler.odczyt_danych_z_pliku_z_magazynem_i_saldem()
lista_operacji = filehandler.odczyt_danych_z_pliku_z_historia()

while not koniec_programu:
    operacja = input(("Wybierz co chcesz zrobic:\n 1. Saldo \n 2. Sprzedaz \n 3. Zakup \n 4. Konto"
                      "\n 5. Lista \n 6. Magazyn \n 7. Przeglad \n 8. Koniec\n"))
    if operacja == "1":  # Saldo
        dodaj_odejmij_srodki = int(input("Chcesz dodac srodki [0] do konta czy odjac srodki z konta [1]  ?"))
        if dodaj_odejmij_srodki != 0 and dodaj_odejmij_srodki != 1:
            (print("Cos poszlo nie tak... musisz podac 0 -> dodanie srodkow lub 1 -> wyplata srodkow"))
            continue
        kwota_operacji = int(input("Podaj kwote operacji: "))
        if dodaj_odejmij_srodki == 0:
            budzet_firmy = budzet_firmy + kwota_operacji
            lista_operacji.append(f"Dodano srodki w wysokosci {kwota_operacji}")
        elif dodaj_odejmij_srodki == 1:
            budzet_firmy = budzet_firmy - kwota_operacji
            lista_operacji.append(f"Wyplacono srodki w wysokosci {kwota_operacji}")

    elif operacja == "2":  # Sprzedaz
        nazwa = input("Podaj nazwe produktu, ktory chcesz sprzedac: ")
        producent_produktu = input("Podaj producenta produktu, ktory chcesz sprzedac: ")
        ilosc_do_sprzedazy = int(input("Ile sztuk chcesz sprzedac ?"))
        znaleziono_produkt = False
        sprzedano_produkt = False
        for produkt in magazyn:
            if produkt.get("nazwa_produktu") == nazwa and produkt.get("producent") == producent_produktu:
                znaleziono_produkt = True
                if produkt.get("ilosc_sztuk") >= ilosc_do_sprzedazy > 0:
                    sprzedano_produkt = True
                else:
                    print("Brak zadanej ilosci produktu lub wynosi ona 0")
                    print("stan magazynowy produktu: ", produkt["ilosc_sztuk"])
                    break

                if sprzedano_produkt:
                    budzet_firmy += (produkt.get("cena") * ilosc_do_sprzedazy)
                    produkt["ilosc_sprzedanych_sztuk"] += ilosc_do_sprzedazy
                    produkt["ilosc_sztuk"] -= ilosc_do_sprzedazy
                    lista_operacji.append(f"Sprzedano {ilosc_do_sprzedazy} szutki produktu {nazwa} ")
            else:
                print("brak takiej pozycji w magazynie")
                break
    elif operacja == "3":  # Zakup
        nazwa_produktu = input("POdaj nazwe produktu, ktory chcesz kupic")
        producent = input("Podaj producenta produktu, ktory chcesz kupic")
        ilosc_sztuk_do_zakupu = int(input("Podaj ilosc sztuk, ktore chcesz kupic"))
        cena_jednostkowa = float(input("Podaj cene produktu, ktory chcesz kupic"))
        produkt_w_magazynie = False
        if ilosc_sztuk_do_zakupu > 0 and cena_jednostkowa > 0:
            if budzet_firmy >= ilosc_sztuk_do_zakupu * cena_jednostkowa:
                for produkt in magazyn:
                    if produkt.get("nazwa_produktu") == nazwa_produktu and produkt.get("producent") == producent:
                        produkt_w_magazynie = True
                        if produkt_w_magazynie:
                            produkt["ilosc_sztuk"] += ilosc_sztuk_do_zakupu
                            break
                    else:
                        cena_do_sprzedazy = float(input("Podaj cene do sprzedazy dla nowego produktu"))
                        magazyn.append({
                            "nazwa_produktu": nazwa_produktu,
                            "producent": producent,
                            "ilosc_sztuk": ilosc_sztuk_do_zakupu,
                            "cena": cena_do_sprzedazy,
                            "ilosc_sprzedanych_sztuk": 0
                        })
                        break
                budzet_firmy = budzet_firmy - (ilosc_sztuk_do_zakupu * cena_jednostkowa)
                lista_operacji.append(f"Zakupiono {ilosc_sztuk_do_zakupu} sztuk produktu {producent} {nazwa_produktu}")
            else:
                print(f'Nie stac Cie, Twoj budzet to {budzet_firmy}')

        else:
            print("Ilosc sztuk do zakupu oraz cena powinny byc wieksze od 0 !")

    elif operacja == "4":  # konto
        print(budzet_firmy)

    elif operacja == "5":  # lista
        print(magazyn)

    elif operacja == "6":  # magazyn
        nazwa_produktu = input("Podaj nazwe produktu, dla ktorego chcesz wyswietlic stan magazynowy")
        producent = input("Podaj producenta produktu, dla ktorego chcesz wyswietlic stan magazynowy")
        for produkt in magazyn:
            if produkt.get("nazwa_produktu") == nazwa_produktu and produkt.get("producent") == producent:
                print(produkt)
            else:
                print("Brak poszukiwanego produktu w magazynie")
    elif operacja == "7":  # przeglad
        od = input("Podaj mi początkowy zakres: ")
        do = input("Podaj mi końcowy zakres: ")
        if od != "" and do != "":
            if not od.isnumeric() or not do.isnumeric():
                print(f'Podales liczbe spoza zakresu, zakres wynosi od 0 do {len(lista_operacji)}')

            elif int(od) < 0 or int(od) > len(lista_operacji) or int(do) > len(lista_operacji) or int(do) < int(od):
                print(f'Podales liczbe spoza zakresu, zakres wynosi od 0 do {len(lista_operacji)}')
            else:
                print(lista_operacji[int(od):int(do)])
        elif od != "" and do == "":
            if not od.isnumeric():
                print(f'Podales liczbe spoza zakresu, zakres wynosi od 0 do {len(lista_operacji)}')
            elif int(od) < 0 or int(od) > len(lista_operacji):
                print(f'Podales liczbe spoza zakresu, zakres wynosi od 0 do {len(lista_operacji)}')
            else:
                print(lista_operacji[int(od):])
        elif od == "" and do != "":
            if not do.isnumeric():
                print(f'Podales liczbe spoza zakresu, zakres wynosi od 0 do {len(lista_operacji)}')
            elif int(do) > len(lista_operacji):
                print(f'Podales liczbe spoza zakresu, zakres wynosi od 0 do {len(lista_operacji)}')
            else:
                print(lista_operacji[:int(do)])
        else:
            print(lista_operacji)

    elif operacja == "8":  # koniec
        koniec_programu = True
        filehandler.zapis_do_pliku_z_magazynem_i_saldem(budzet_firmy=budzet_firmy, magazyn=magazyn)
        filehandler.zapis_do_pliku_z_historia(lista_operacji=lista_operacji)
