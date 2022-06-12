/* Collatz sanısı
   Kodunuzu main fonksiyonunun içine yazınız.
*/

#include <iostream>
using namespace std;

int main()
{
    int sayi = 0;
    int count = 0;

    cin >> sayi;

    while (sayi != 1)
    {
        if (sayi % 2 == 0)
        {
            sayi = sayi / 2;
        }
        else
        {
            sayi = sayi * 3 + 1;
        }
        count++;
    }
    cout << count << endl;
    return 0;
}