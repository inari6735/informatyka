/*
 * znaki.cpp
 * 
 * Copyright 2018 kl2ag2 <kl2ag2@ubu02>
 */


#include <iostream>

using namespace std;

void zamien_znaki(char tb[], int roz){
    for(int i = 0; i < roz; i++){
        zamień małe na duże;
        kod_ascii 'a' = 97
        kod_ascii 'A' = 65
        97 - 65 = 32
        (char)(kod_ascii - 32)
    }
}

void licz_znaki(char tb[], int roz){
    //for(int i = 0; i < roz; i++){
        //cout << tb[i];
    //}
    int i = 0;
    int biale, cyfry, literyD, literyM, reszta;
    biale = cyfry = literyD = literyM = reszta = 0;
    int znak_kod = 0;
    while(tb[i] != '\0'){
        znak_kod = (int)tb[i];
        if(znak_kod > 64 && znak_kod < 91)
            literyD++;
        else if(znak_kod > 96 && znak_kod < 123)
            literyM++;
        else if(znak_kod > 47 && znak_kod < 58)
            cyfry++;
        else
            reszta++;
        i++;
        }
    cout << "Białych: " << biale << endl;
    cout << "Duże: " << literyD << endl;
    cout << "Małe: " << literyM << endl;
    cout << "Cyfry: " << cyfry << endl;
    cout << "Reszta: " << reszta << endl;
}

int main(int argc, char **argv)
{
    const int rozmiar = 21;
    char znaki[rozmiar]; // max 20 znaków ostatni to \0
    cin.getline(znaki, 21);
    licz_znaki(znaki, rozmiar);
	return 0;
}

