/*
 * liczby23.cxx
 */


#include <iostream>

using namespace std;

int liczby2(){
    int ile = 0;
    for(int i = 1; i<= 10; i++){
        for(int j = 0; j <= 10; i++){
            for(int k = 0; k < 10; k++){
            if(i != j && i != k && j != k){
                cout << i << j << k << " ";
                ile++;
            }
        }
        }
    }
    return ile;
}


int main(int argc, char **argv)
{
    int ile = liczby2();
	cout << "\n\nLiczb 2-cyfrowych:" << ile << endl;
	return 0;
}

