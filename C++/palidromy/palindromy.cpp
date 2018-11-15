/*
 * palindromy.cpp
 */


#include <iostream>
#include <string.h>


using namespace std;

bool palindrom(char wyraz[], int rozmiar){ // funkcja zwraca PRAWDA albo FAŁSZ
    bool pal = true;
    for(int i = 0; i < w; i ++){
        if(w[i] != w[romiar - i - 1]){
            pal = false;
            break;
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

