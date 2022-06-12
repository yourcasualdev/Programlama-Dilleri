#include <iostream>
#include <vector>
using namespace std;

/*
Parametre olarak gelen matrisi kullanarak Pascal üçgenini oluşturan fonksiyonu yazınız.
Parametre referans olarak gönderilmiştir, dolayısıyla geriye bir şey döndürmeye gerek yoktur.
Bu örnek için ekrana değerler yazdırmanıza gerek yoktur, önemi de yoktur.
*/
void pascal(vector<vector<int>> &vec)
{
    int row = vec.size();
    int col = vec[0].size();
    for (int i = 0; i < row; i++)
    {
        for (int j = 0; j < col; j++)
        {
            if (i < j)
            {
                vec[i][j] = 0;
            }
            else
            {
                if (i == 0 || j == 0 || i == j)
                {
                    vec[i][j] = 1;
                }
                else
                {
                    vec[i][j] = vec[i - 1][j] + vec[i - 1][j - 1];
                }
            }
        }
    }
}