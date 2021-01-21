class Generator:
    def generate(self, number_of_shares, lower_price_limit, upper_price_limit):
        return 0
    def generate_decreasing(self,number_of_shares, p):
        return 0

class Osoba:
    def __init__(self, imie, nazwisko, wiek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.wiek = wiek
    def przedstaw_sie(self):
        return "Jestem " + self.imie + " " + self.nazwisko +" Mam " + self.wiek + " lat."
