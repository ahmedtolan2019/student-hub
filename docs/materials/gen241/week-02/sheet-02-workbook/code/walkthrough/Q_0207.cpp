// GEN 241 - Sheet 2 - Q7
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  valid triangle area or invalid message
//   HAVE  three side lengths in one unit
//   CONVERT  lengths to semiperimeter
//   RELATE  validate all pair sums then apply Heron
//   CHECK  valid, flat, impossible and fractional cases
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read the three side lengths
    double a, b, c;
    cin >> a >> b >> c;
    // 2. can these sides close into a triangle?
    bool valid = a > 0 && b > 0 && c > 0 && a + b > c && a + c > b && b + c > a;
    cout << "valid=" << valid << endl;
    // 3. Heron only for a valid triangle
    if (valid)
    {
        double s = (a + b + c) / 2.0;
        double area = sqrt(s * (s - a) * (s - b) * (s - c));
        cout << "s=" << s << "\narea=" << area << endl;
    }
    else
    {
        cout << "Invalid input" << endl;
    }
    return 0;
}
