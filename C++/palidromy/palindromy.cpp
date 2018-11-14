/*
 * palindromy.cpp
 */


#include <iostream>
#include <string.h>


using namespace std;

bool palindrom(char wyraz[], int rozmiar){ // funkcja zwraca PRAWDA albo FAŁSZ
    bool pal = True;
    int d;
    d = rozmiar / 2;
    for(int i = 0; i < d; i ++){
        if(w[i] != w[d - i - 1]){
            pal = False;
        };
    };
    return pal;
}

int main(int argc, char **argv)
{
	int rozmiar = 20;
    char wyraz[rozmiar];
    cout << "Podaj wyraz: ";
    cin.getline(wyraz, rozmiar);
    cout << cin.gcount() << endl;
    cout << strlen(wyraz) << endl;
	return 0;
}

