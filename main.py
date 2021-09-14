import rekins

def print_info():
    print('Programma rekina sagatavosanai')

def lietotaja_ievade():
    
    vards = input('Ieraksti vardu: ')
    veltijuma_teksts = input('Ievadi veltijuma tekstu kastitei: ')
    platums = input('Cik plata kastite? Noraadi milimetrus. Tikai veseli skaitli!')
    garums = input('Cik  plata garumaa? Noraadi milimetrus.Tikai veseli skaitli!')
    augstums = input('Cik  augsta? Noraadi milimetrus.Tikai veseli skaitli!')
    kokmateriala_cena = input('Kokmateriala cena')
    return vards, veltijuma_teksts, platums, garums, augstums, kokmateriala_cena

if __name__ == '__main__':
    print_info()
    while True:
       lietotaja_ievade()
       run_again = input('Vai velies sagatavot rekinu velreiz? JAA - 1, NEE - 0')
       if run_again == 1:
           continue
       else:
           exit(0)
