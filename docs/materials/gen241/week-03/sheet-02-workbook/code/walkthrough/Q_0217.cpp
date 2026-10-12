// GEN 241 - Sheet 2 - Q17
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  line equation in slope-intercept form
//   HAVE  two coordinate pairs
//   CONVERT  derive slope then intercept
//   RELATE  m=dy/dx; b=y1-m*x1; format by signs
//   CHECK  substitute both points and test m=1 with nonzero b
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read both points
    double x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    // 2. no y = mx + b for a vertical line or a repeated point
    if (x1 == x2)
    {
        if (y1 == y2)
        {
            cout << "No unique line" << endl;
        }
        else
        {
            cout << "Vertical line: x=" << x1 << endl;
        }
        return 0;
    }
    // 3. slope, then intercept
    double m = (y2 - y1) / (x2 - x1);
    double b = y1 - m * x1;
    // 4. print y = mx + b, hiding m = 1 and b = 0
    cout << "m=" << m << "\nb=" << b << "\ny = ";
    if (m == 0)
    {
        cout << b;
    }
    else
    {
        if (m == 1)
        {
            cout << "x";
        }
        else if (m == -1)
        {
            cout << "-x";
        }
        else
        {
            cout << m << "x";
        }
        if (b > 0)
        {
            cout << " + " << b;
        }
        else if (b < 0)
        {
            cout << " - " << -b;
        }
    }
    cout << endl;
    return 0;
}
