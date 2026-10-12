// GEN 241 - Sheet 2 - Q10
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  three integers in descending order
//   HAVE  three integers, possibly equal or negative
//   CONVERT  preserve original values during swaps
//   RELATE  compare a,b then a,c then b,c
//   CHECK  same multiset; first>=second>=third
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read three integers
    int a, b, c, temp;
    cin >> a >> b >> c;
    cout << "start=" << a << "," << b << "," << c << endl;
    // 2. put the larger of a and b in a
    if (a < b)
    {
        temp = a;
        a = b;
        b = temp;
    }
    cout << "pair1=" << a << "," << b << "," << c << endl;
    // 3. bring the largest into a
    if (a < c)
    {
        temp = a;
        a = c;
        c = temp;
    }
    cout << "largest=" << a << "," << b << "," << c << endl;
    // 4. order b and c
    if (b < c)
    {
        temp = b;
        b = c;
        c = temp;
    }
    cout << "order=" << a << "," << b << "," << c << endl;
    return 0;
}
