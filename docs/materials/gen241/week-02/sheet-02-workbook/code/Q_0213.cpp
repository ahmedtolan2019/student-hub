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
    int n; cin >> n;
    if(n<100 || n>999) { cout << "Invalid three-digit integer" << endl; return 0; }
    int hundreds=n/100, tens=(n/10)%10, units=n%10;
    cout << "hundreds=" << hundreds << "\ntens=" << tens << "\nunits=" << units << "\nsum=" << hundreds+tens+units << endl;
    return 0;
}
