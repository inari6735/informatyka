/*
 * zad1.cpp
 */


#include <iostream>

using namespace std;

int main(int argc, char **argv)
{
	int suma = 0;
    for(int i = 10; i < 100; i+=2)
        suma += i;
    cout << suma << endl;
	return 0;
}

