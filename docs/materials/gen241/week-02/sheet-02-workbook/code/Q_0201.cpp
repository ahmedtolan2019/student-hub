// GEN 241 - Sheet 2 - Q1
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  temperature in Fahrenheit
//   HAVE  Celsius double
//   CONVERT  scale by 9.0/5 and add 32
//   RELATE  f=(9.0/5)*c+32
//   CHECK  test zero and a nonzero Celsius value
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    double c; cin >> c;
    // 1. keep fractional division
    double ratio = 9.0 / 5;
    double f = ratio * c + 32;
    cout << "ratio=" << ratio << "\nf=" << f << endl;
    return 0;
}
