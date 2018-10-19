/*
 * sumacyfr.cpp
 */


#include <iostream>

using namespace std;

int sumuj_cyfry1(int liczba){
    int suma = 0;
    while(liczba > 0){
        suma += liczba % 10;
        liczba = int(liczba / 10);
    }
    return suma;
}

int main(int argc, char **argv)
{
    int liczba = 0;
    while(liczba < 10){
        cout << "Podaj liczbę 2-cyfrową:";
        cin >> liczba;
    }
    int x = sumuj_cyfry1(liczba);
    cout << x;
	return 0;
}

