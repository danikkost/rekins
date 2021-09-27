import rekins


def print_info():
    print('Programma rekina sagatavosanai')


def lietotaja_ievade():
    vards = input('Ieraksti vardu: ')
    teksts = input('Ievadi veltijuma tekstu kastitei: ')
    platums = float(input('Cik plata kastite? Noraadi milimetrus. Tikai veseli skaitli!'))
    garums = float(input('Cik  plata garumaa? Noraadi milimetrus.Tikai veseli skaitli!'))
    augstums = float(input('Cik  augsta? Noraadi milimetrus.Tikai veseli skaitli!'))
    materials = input('Kokmateriala cena')
    return vards, teksts, platums, garums, augstums, materials

    darba_samaksa = 15
    PVN = 21
    produkta_cena = teksts * 1.2 + platums / 100 * garums / 100 * augstums / 100 / 3 * materials
    PVN_summa = produkta_cena + darba_samaksa * PVN / 100
    rekina_summa = produkta_cena + darba_samaksa + PVN_summa

    print("Produkta cena: €" + format(produkta_cena, ",.2f"))
    print("PVN summa: €" + format(PVN_summa, ",.2f"))
    print("rekina_summa: €" + format(rekina_summa, ",.2f"))

    guy = [format(produkta_cena),format(PVN_summa),format(rekina_summa)]

    f = open("rekins.txt", "x")
    f.write("\n")
    f.write("Produkta cena: " + format(produkta_cena, ",.2f") + "€")
    f.write("\n")
    f.write("PVN summa: " + format(PVN_summa, ",.2f")+ "€")
    f.write("\n")
    f.write("rekina_summa: " + format(rekina_summa, ",.2f")+ "€")
    f.close()


from datetime import date

today = date.today()
print("Today's date:", today)

if __name__ == '__main__':
    print_info()
    while True:
       lietotaja_ievade()
       restart = input('Gribat vel?').lower()
       if restart == "yes":
           print_info()
       else:
           break
