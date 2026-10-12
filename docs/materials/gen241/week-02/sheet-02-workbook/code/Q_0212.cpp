// GEN 241 - Sheet 2 - Q12
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  triangle area in square units
//   HAVE  three coordinate pairs in one unit
//   CONVERT  points to three distances, then semiperimeter
//   RELATE  Heron from derived lengths
//   CHECK  translation preserves area; scale changes area
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    double x1,y1,x2,y2,x3,y3; cin >> x1 >> y1 >> x2 >> y2 >> x3 >> y3;
    double a=sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1));
    double b=sqrt((x3-x2)*(x3-x2)+(y3-y2)*(y3-y2));
    double c=sqrt((x1-x3)*(x1-x3)+(y1-y3)*(y1-y3));
    double s=(a+b+c)/2.0;
    double area=sqrt(s*(s-a)*(s-b)*(s-c));
    cout << "a=" << a << "\nb=" << b << "\nc=" << c << "\ns=" << s << "\narea=" << area << endl;
    return 0;
}
