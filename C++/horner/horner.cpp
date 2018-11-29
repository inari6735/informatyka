/*
 * horner.cpp
 * 
 * Copyright 2018 kl2ag2 <kl2ag2@ubu02>
 */


#include <iostream>
using namespace std;

void drukujw(int st, float tb[]){
    
    for(int i = 0; i < st; i++){
        cout << tb[i] << "x^" << st-i << " + ";
    }
    cout << tb[st] << endl;
}

int main(int argc, char **argv)
{
    int stopien = 0;
    float *tbwsp; // wskaznik
    float x = 0; // argument
	cout << "Stopień wielomianu: ";
    cin >> stopien;
    tbwsp = new float [stopien+1];
    
    for(int i=0; i<= stopien; i++) {
        cout << "Podaj współczynnik przy potędzie " << stopien-i << ": ";
        cin >> tbwsp[i];
    }
    
    cout << "Argument: ";
    cin >> x;
    cout << "Wartość wielomianu o postaci: ";
    drukujw(stopien, tbwsp);
    
	return 0;
}

