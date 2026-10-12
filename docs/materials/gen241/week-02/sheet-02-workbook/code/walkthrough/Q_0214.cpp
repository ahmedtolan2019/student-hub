// GEN 241 - Sheet 2 - Q14
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  point inside or outside including boundary
//   HAVE  point x,y; centre (0,0); radius 10
//   CONVERT  coordinates to distance
//   RELATE  sqrt(x*x+y*y)<=10
//   CHECK  test inside, outside, boundary and centre
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read the point
    double x, y;
    cin >> x >> y;
    // 2. distance from the centre (0, 0)
    double distance = sqrt(x * x + y * y);
    cout << "distance=" << distance << endl;
    // 3. compare with radius 10 (the boundary counts as inside)
    if (distance <= 10)
    {
        cout << "Inside (boundary included)" << endl;
    }
    else
    {
        cout << "Outside" << endl;
    }
    return 0;
}
