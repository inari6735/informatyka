/*
Miejsce na komentarze wielowierszowe
 */


#include <iostream> /* Niektóre komendy działają tylko wtedy jak podepniemy biblioteki io(input/output) */

using namespace std; // dzięki temu mogę pozbyć się std np. std:cout

int main(int argc, char **argv) /* Funkcja główna int(integer) */
{
	int a; // deklaracja zmiennej
    a = 0; // inicjacja zmiennej
    
    cout << "Podaj liczbę: "; // stała napisowa nie takie '' tylko takie ""
    cin >> a; // metoda wejścia
    cout << a; //przekieruj na ekran(terminal) wartość zmiennej a - cout metoda wyjścia
    
	return 0;
}

