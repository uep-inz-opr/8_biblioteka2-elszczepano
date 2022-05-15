import re


class Biblioteka:
    limit_wypozyczen = 3
    ksiazki = []
    egzemplarze = []
    czytelnicy = []

    def _get_ksiazka(self, tytul, autor):
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul and ksiazka.autor == autor:
                return ksiazka
        return False

    def _get_czytelnik(self, nazwisko):
        for czytelnik in self.czytelnicy:
            if czytelnik.nazwisko == nazwisko:
                return czytelnik
        return False
    
    def _get_egzemplarz(self, tytul):
        for egzemplarz in self.egzemplarze:
            if egzemplarz.tytul == tytul and egzemplarz.wypozyczony == False:
                return egzemplarz
        return False


    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania ):
        ksiazka = self._get_ksiazka(tytul, autor)

        if ksiazka == False:
            ksiazka = Ksiazka(tytul, autor)

            self.ksiazki.append(ksiazka)

        self.egzemplarze.append(Egzemplarz(ksiazka, rok_wydania))

        return True
    
    def wypozycz(self, nazwisko, tytul):
        czytelnik = self._get_czytelnik(nazwisko)

        if czytelnik == False:
            czytelnik = Czytelnik(nazwisko)

            self.czytelnicy.append(czytelnik)


        # przyjmij też, że domyślnie można wypożyczyć maksymalnie 3 egzemplarze różnych książek
        if( len( czytelnik.wypozyczenia ) > 3 ):
            return False

        # można wypożyczyć tylko jeden egzemplarz tej samej książki
        if( czytelnik.get_egzemplarz( tytul ) == True ):
            return False
        
        egzemplarz = self._get_egzemplarz(tytul)

        # brak ksiazek na stanie
        if( egzemplarz == False ):
            return False
        
        egzemplarz.wypozyczony == True

        czytelnik.wypozycz(egzemplarz)

        return True

    def oddaj(self, nazwisko, tytul):
        czytelnik = self._get_czytelnik(nazwisko)

        if(czytelnik == False):
            return False

        egzemplarz = czytelnik.get_egzemplarz(tytul)

        if(egzemplarz == False):
            return False

        egzemplarz.wypozyczony == False

        czytelnik.oddaj(tytul)

        return True

class Czytelnik:
    wypozyczenia = []

    def __init__(self, nazwisko):
        self.nazwisko = nazwisko

    def get_egzemplarz(self, tytul):
        for egzemplarz in self.wypozyczenia:
            if egzemplarz.tytul == tytul:
                return egzemplarz
        return False

    def wypozycz(self, egzemplarz):
        self.wypozyczenia.append(egzemplarz)

        return True

    def oddaj(self, tytul):
        for egzemplarz in self.wypozyczenia:
            if egzemplarz.ksiazka_ref.tytul == tytul:
                # TODO remove from array
                return True
        
        return False

class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

class Egzemplarz:
    wypozyczony = False

    def __init__(self, ksiazka_ref, rok_wydania):
        self.ksiazka_ref = ksiazka_ref
        self.rok_wydania = rok_wydania
        self.wypozyczony = False
    
actions_count = int( input() )

biblioteka = Biblioteka()

for index in range(0, actions_count):
    command = input().replace('(', '').replace(')', '').replace(' "', '').replace('"', '').split(",")

    action = book[0]

    if action == 'dodaj':
        czytelnik = book[1]
        tytul = book[2]
        rok = book[3]
        is_success = biblioteka.dodaj_egzemplarz_ksiazki(tytul, autor, rok)
        print( is_success )
    
    if action == 'wypozycz':
        czytelnik = book[1]
        tytul = book[2]
        is_success = biblioteka.wypozycz(czytelnik, tytul)
        print(is_success)

    if action == 'oddaj':
        czytelnik = book[1]
        tytul = book[2]
        is_success = biblioteka.oddaj(czytelnik, tytul)
        print(is_success)
