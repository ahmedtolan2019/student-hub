// GEN 241 - Sheet 2 - Q4
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  distance in length units
//   HAVE  two coordinate pairs in one unit
//   CONVERT  coordinates to differences
//   RELATE  sqrt(dx*dx+dy*dy)
//   CHECK  reverse points; distance should stay the same
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read both points
    double x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;
    // 2. horizontal and vertical change
    double dx = x2 - x1;
    double dy = y2 - y1;
    // 3. Pythagoras: square, add, square root
    double squared = dx * dx + dy * dy;
    double distance = sqrt(squared);
    // 4. display
    cout << "dx=" << dx << "\ndy=" << dy << "\nsquared=" << squared << "\ndistance=" << distance << endl;
    return 0;
}
