// GEN 241 - Sheet 2 - Q5
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  slope as rise/run
//   HAVE  two coordinate pairs
//   CONVERT  coordinates to dx and dy
//   RELATE  dy/dx when dx is nonzero
//   CHECK  horizontal versus vertical line
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    double x1,y1,x2,y2; cin >> x1 >> y1 >> x2 >> y2;
    double dx=x2-x1, dy=y2-y1;
    cout << "dx=" << dx << "\ndy=" << dy << endl;
    if (dx == 0) cout << "Undefined slope" << endl;
    else cout << "m=" << dy/dx << endl;
    return 0;
}
