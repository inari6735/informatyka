/*
 * znaki.cpp
 * 
 * Copyright 2018 kl2ag2 <kl2ag2@ubu02>
 */


#include <iostream>

using namespace std;

void licz_znaki(char tb[], int roz){
    //for(int i = 0; i < roz; i++){
        //cout << tb[i];
    //}
    int i = 0;
    while(tb[i] != '\0'){
        cout << tb[i];
        i++;
    }
}

int main(int argc, char **argv)
{
    const int rozmiar = 21;
    char znaki[rozmiar]; // max 20 znaków ostatni to \0
    cin.getline(znaki, 21);
    licz_znaki(znaki, rozmiar);
	return 0;
}

