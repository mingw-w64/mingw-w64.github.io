#include <iostream>
using namespace std;

int main() {
    int *pBil;
    int bilX = 77;

    pBil = &bilX;

    cout << "isi bilX = " << bilX << endl;
    cout << "nilai yang ditunjuk pBil = " << *pBil << endl;

    *pBil = *pBil + 3;

    cout << "isi bilX sekarang = " << bilX << endl;
    cout << "nilai yang ditunjuk pBil = " << *pBil << endl;

    return 0;
}
