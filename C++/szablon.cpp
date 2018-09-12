/*
Miejsce na komentarze wielowierszowe
 */


#include <iostream> /* Niektóre komendy działają tylko wtedy jak podepniemy biblioteki io(input/output) */

using namespace std; // dzięki temu mogę pozbyć się std np. std:cout

int main(int argc, char **argv) /* Funkcja główna int(integer) */
{
	float a, b; // deklaracja zmiennej
    a = b = 0; // inicjacja zmiennej
    
    cout << "Podaj 1. liczbę: "; // stała napisowa nie takie '' tylko takie ""
    cin >> a; // metoda wejścia
    cout << a << endl; //przekieruj na ekran(terminal) wartość zmiennej a - cout metoda wyjścia
    
    cout << "Podaj 2. liczbę: ";
    cin >> b;
    cout << b << endl; // endl - znak nowej lini
    
    cout << "Suma: " << a + b << endl;
    cout << "Różnica: " << a - b << endl;
    cout << "Iloczyn: " << a * b << endl;
    cout << "Iloraz: " << a / b << endl;
    
	return 0;
}

