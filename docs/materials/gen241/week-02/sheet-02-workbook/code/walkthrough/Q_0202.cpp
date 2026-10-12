// GEN 241 - Sheet 2 - Q2
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  base area in square units; volume in cubic units
//   HAVE  radius and length in one length unit
//   CONVERT  no conversion when units match
//   RELATE  area=PI*r*r; volume=area*length
//   CHECK  double length, then double radius separately
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read radius and length
    double r, length;
    cin >> r >> length;
    // 2. reject dimensions that cannot form a cylinder
    if (r <= 0 || length <= 0)
    {
        cout << "Invalid dimensions" << endl;
        return 0;
    }
    // 3. base area, then volume
    const double PI = 3.14159;
    double area = r * r * PI;
    double volume = area * length;
    // 4. display both results
    cout << "area=" << area << "\nvolume=" << volume << endl;
    return 0;
}
