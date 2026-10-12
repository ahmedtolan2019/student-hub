// GEN 241 - Sheet 2 - Q15
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  geometric relation of circle2 to circle1
//   HAVE  two centres and positive radii
//   CONVERT  centres to distance d
//   RELATE  directional containment then tangency/overlap/separation
//   CHECK  reverse radii; clarify source hint before submission
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read both circles
    double x1, y1, r1, x2, y2, r2;
    cin >> x1 >> y1 >> r1 >> x2 >> y2 >> r2;
    // 2. reject a non-positive radius
    if (r1 <= 0 || r2 <= 0)
    {
        cout << "Invalid radius" << endl;
        return 0;
    }
    // 3. distance between the centres
    double d = sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
    cout << "distance=" << d << "\nradiiSum=" << r1 + r2 << "\nabsoluteDifference=" << fabs(r1 - r2) << endl;
    // 4. where is circle 2 relative to circle 1?
    // Teaching clarification: directional geometry, not an approved marking rule.
    if (d == 0 && r1 == r2)
    {
        cout << "Identical circles" << endl;
    }
    else if (d + r2 <= r1)
    {
        cout << "circle2 inside circle1" << endl;
    }
    else if (d + r1 <= r2)
    {
        cout << "circle1 inside circle2" << endl;
    }
    else if (d > r1 + r2)
    {
        cout << "Separate" << endl;
    }
    else if (d == r1 + r2)
    {
        cout << "External tangency" << endl;
    }
    else
    {
        cout << "Overlap" << endl;
    }
    return 0;
}
