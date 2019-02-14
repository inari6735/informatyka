/*
 * szyfr_rzymski.cxx
 */


#include <iostream>
#include <string.h>
using namespace std;

#define MAKS 100

void szyfruj(char tekst[], int klucz){
    int tekstSize = strlen(tekst);
    int kod = 0;
    for(int i=0; i < tekstSize; i++){
        cout << tekst[i] << endl;
    };
    for(int j=0; i < tekstSize; i++){
        kod = (int)tekst[i];
        if kod
    }
}

int main(int argc, char **argv)
{
    char tekst[MAKS];
    int klucz = 0;
    cout << "Podaj tekst:\n";
    cin.getline(tekst, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(tekst, klucz);
    
	return 0;
}

