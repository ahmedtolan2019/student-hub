// GEN 241 - Sheet 2 - Q13
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  digit sum or invalid message
//   HAVE  integer input; accepted range 100..999
//   CONVERT  integer division and remainder extract digits
//   RELATE  n/100 + (n/10)%10 + n%10
//   CHECK  test 99,100,999,1000
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read the integer
    int n;
    cin >> n;
    // 2. accept only 100 to 999
    if (n < 100 || n > 999)
    {
        cout << "Invalid three-digit integer" << endl;
        return 0;
    }
    // 3. split into digits
    int hundreds = n / 100;
    int tens = (n / 10) % 10;
    int units = n % 10;
    // 4. display the digits and their sum
    cout << "hundreds=" << hundreds << "\ntens=" << tens << "\nunits=" << units << "\nsum=" << hundreds + tens + units << endl;
    return 0;
}
