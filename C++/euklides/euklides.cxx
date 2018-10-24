/*
 * euklides.cxx
 * 
 * Copyright 2018 kl2ag2 <kl2ag2@ubu02>
 */


#include <iostream>
using namespace std;

int nwd_optymalny(int a, int b){
    int licznik = 0;
    while(a > b){
        a = a % b;
        b = b - a;
        licznik++;
    }
    cout << "Powtórzeń: " << licznik << endl;
    return b;
}

int nwd_klasyczny(int a, int b){
    int licznik = 0;
    while(a > b){
        if(a > b){
            a = a - b;
        }
        else
            b = b - a;
        licznik++;
        
    }
    cout << "Powtórzeń: " << licznik << endl;
    return a;
}

int main(int argc, char **argv){
	int a, b;
    cout << "Podaj 2 liczby: ";
    cin >> a >> b;
    int nwd = nwd_klasyczny(a, b);
    cout << "NWD(" << a << "," << b << ") = " << nwd << endl;
    int nwd2 = nwd_optymalny(a, b);
    cout << "NWD(" << a << "," << b << ") = " << nwd2 << endl;

	return 0;
}

