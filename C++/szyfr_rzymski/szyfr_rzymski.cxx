/*
 * szyfr_rzymski.cxx
 */


#include <iostream>
#include <string.h>
using namespace std;

#define MAKS 100

void deszyfruj(char tb[], int klucz){
    klucz = klucz % 26;
    int i = 0;
    int kod = 0;
    while (tb[i] != '\0'){
        ;
    }
}

void szyfruj(char tb[], int klucz){
    klucz = klucz % 26;
    int i = 0;
    int kod = 0;
    while (tb[i] != '\0'){
        kod = (int)tb[i];
        if(tb[i] == ' '){
            ;
        }else if(kod < 91){
            kod += klucz;
            if(kod > 90) kod -= 26;
        }else{
            kod += klucz;
            if(kod > 122) kod -= 26;
        }
        
        
        cout << (char)kod;
        tb[i] = (char)kod;
        i++;
    }
    cout << endl;
}

int main(int argc, char **argv)
{
    char tb[MAKS];
    int klucz = 0;
    cout << "Podaj tekst:\n";
    cin.getline(tb, MAKS);
    cout << "Podaj klucz: ";
    cin >> klucz;
    szyfruj(tb, klucz);
    
	return 0;
}

