#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  petla.py
#
# DANE WEJŚCIOWE:
# liczby dodatnie przez użytkownika
# DANE WYJŚCIOWE:
# suma liczb podanych przez użytkownika
# program musi zapewnić poprawność danych,
# program kończy działanie po wprowadzeniu wartości 0

def pobierzMiesiac(args):
    
    miesiac = 9
    nazwa_miesiaca = ['styczen', 'luty', 'marzec', 'kwiecien', 'maj', 'czerwiec', 'lipiec', 'sierpien', 'wrzesien', 'pazdziernik', 'listopad', 'grudzien']
    
    for i in range(3):
        miesiac = int(input("Jaki mamy miesiąc(numer)?:"))
        if miesiac == 9:
            print("Odgadłeś!", nazwa_miesiaca[miesiac - 1])
            break

def main(args):
    
    koniec = "kontynuuj"
    suma = 0
    
    while koniec == "kontynuuj":
        liczba = int(input("Wprowadź liczbę: "))
        if liczba == 0:
            koniec = "jejwew"
        suma += liczba
        
        koniec = input("Aby zakończyć działanie wpisz (zakoncz) aby kontynuować wpisz (kontynuuj)")
    print("Suma: ", suma)
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(pobierzMiesiac(sys.argv))
