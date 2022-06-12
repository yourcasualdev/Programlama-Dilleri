#include <iostream>
#include <string>

using namespace std;

int perfectnumber(int number);

int main()
{
    int number = 0;

    cin >> number;

    perfectnumber(number) ? cout << "mükemmel" << endl
                          : cout << "mükemmel değil" << endl;

    return 0;
}

int perfectnumber(int number)
{
    int sum = 0;
    int i = 1;
    while (i < number)
    {
        if (number % i == 0)
        {
            sum += i;
        }
        i++;
    }
    if (sum == number)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}
