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
    double x1,y1,x2,y2; cin >> x1 >> y1 >> x2 >> y2;
    double dx=x2-x1, dy=y2-y1;
    double squared=dx*dx+dy*dy;
    double distance=sqrt(squared);
    cout << "dx=" << dx << "\ndy=" << dy << "\nsquared=" << squared << "\ndistance=" << distance << endl;
    return 0;
}
