/*
 * zad3.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int rozmiar = 8;
    int suma = 0;
	int tablica[rozmiar];
    for(int i=0; i < rozmiar; i++){
        cin >> tablica[i];
    }
    for(int i=0; i < rozmiar; i++){
        suma += tablica[i];
    }
    int srednia = suma / rozmiar;
    int licznik = 0;
    for(int i=0; i < rozmiar; i++){
        if(tablica[i] % 5 == 0){
            licznik += 1;
        }
    }
    cout << suma << endl;
    cout << srednia << endl;
    cout << licznik << endl;
	return 0;
}

