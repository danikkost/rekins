import rekins

def print_info():
    print('Programma rekina sagatavosanai')

def lietotaja_ievade():
    
    vards = input('Ieraksti vardu: ')
    teksts = input('Ievadi veltijuma tekstu kastitei: ')
    platums = input('Cik plata kastite? Noraadi milimetrus. Tikai veseli skaitli!')
    garums = input('Cik  plata garumaa? Noraadi milimetrus.Tikai veseli skaitli!')
    augstums = input('Cik  augsta? Noraadi milimetrus.Tikai veseli skaitli!')
    materials = input('Kokmateriala cena')
    return vards, teksts, platums, garums, augstums, materials

    darba_samaksa = 15
    PVN = 21
    produkta_cena = tekst * 1.2 + width / 100 * length / 100 * height / 100 / 3 * material
    PVN_summa = produkta_cena + darba_samaksa * PVN / 100
    rekina_summa = produkta_cena + darba_samaksa + PVN_summa
    print("Produkta cena: €" + format(produkta_cena, ",.2f"))
    print("PVN summa: €" + format(PVN_summa, ",.2f"))
    print("rekina_summa: €" + format(rekina_summa, ",.2f"))
    
    
from datetime import date
today = date.today()
print("Today's date:", today)
    
    	

if __name__ == '__main__':
    print_info()
    while True:
       lietotaja_ievade()
       restart = input('Vai velies sagatavot rekinu velreiz? JAA - 1, NEE - 0')
       if restart == 1:
           print_info()
       else:
           break
