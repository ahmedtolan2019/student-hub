// GEN 241 - Sheet 2 - Q11
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  triangle type or invalid message
//   HAVE  three positive edge lengths
//   CONVERT  no unit conversion
//   RELATE  validity then all equal, then any equal pair
//   CHECK  equal pairs cannot rescue an invalid triangle
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    double a,b,c; cin >> a >> b >> c;
    bool valid=a>0 && b>0 && c>0 && a+b>c && a+c>b && b+c>a;
    cout << "valid=" << valid << endl;
    if(!valid) cout << "Invalid triangle" << endl;
    else if(a==b && b==c) cout << "Equilateral Triangle" << endl;
    else if(a==b || a==c || b==c) cout << "Isosceles Triangle" << endl;
    else cout << "Scalene Triangle" << endl;
    return 0;
}
