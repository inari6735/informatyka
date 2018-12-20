/*
 * zad2.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
    int tablica[2];
    bool end = false;
    while(end == false){
        cin >> tablica[0];
        cin >> tablica[1];
        cin >> tablica[2];
        int suma = tablica[0] + tablica[1];
        if(tablica[2] == suma)
            end = true;
        cout << "Liczba wynosi: " << suma << endl;
    }
	return 0;
}

