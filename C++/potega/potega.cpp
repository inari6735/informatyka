/*
 * potega.cpp
 * 
 * Copyright 2018 kl2ag2 <kl2ag2@ubu02>

 */


#include <iostream>

using namespace std;

int potega_it(int a, int n){
    int wynik = 1;
    for(int i=0; i < n; i++)
        wynik = wynik * a;
    return wynik;
}

int main(int argc, char **argv)
{
    int a, n;
    cout << "Podaj podstawę i wykładnik: ";
    cin >> a >> n;
    cout << "Potęga: " << potega_it(a, n) << endl;

	return 0;
}

