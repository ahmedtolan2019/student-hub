// GEN 241 - Sheet 2 - Q6
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  regular polygon area in square units
//   HAVE  integer n>=3 and side length
//   CONVERT  use radians for tan
//   RELATE  n*side*side/(4*tan(PI/n))
//   CHECK  compare a square with side*side
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read the number of sides and their length
    int n;
    double side;
    cin >> n >> side;
    // 2. reject shapes that are not polygons
    if (n < 3 || side <= 0)
    {
        cout << "Invalid polygon" << endl;
        return 0;
    }
    // 3. apothem, then area
    const double PI = 3.14159;
    double apothem = side / (2 * tan(PI / n));
    double area = n * side * side / (4 * tan(PI / n));
    // 4. display
    cout << "apothem=" << apothem << "\narea=" << area << endl;
    return 0;
}
