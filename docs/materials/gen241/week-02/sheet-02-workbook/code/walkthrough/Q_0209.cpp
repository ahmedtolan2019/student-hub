// GEN 241 - Sheet 2 - Q9
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  real roots or no-real-roots message
//   HAVE  coefficients a,b,c including signs
//   CONVERT  no unit conversion
//   RELATE  branch on D=b*b-4*a*c before sqrt
//   CHECK  substitute roots; test positive, zero, negative D
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    // 1. read a, b and c
    double a, b, c;
    cin >> a >> b >> c;
    // 2. a = 0 is not a quadratic
    if (a == 0)
    {
        cout << "Not a quadratic equation" << endl;
        return 0;
    }
    // 3. the discriminant decides how many roots
    double D = b * b - 4 * a * c;
    cout << "D=" << D << endl;
    // 4. one branch for each sign of D
    if (D > 0)
    {
        cout << "r1=" << (-b + sqrt(D)) / (2 * a) << "\nr2=" << (-b - sqrt(D)) / (2 * a) << endl;
    }
    else if (D == 0)
    {
        cout << "root=" << -b / (2 * a) << endl;
    }
    else
    {
        cout << "The equation has no real roots." << endl;
    }
    return 0;
}
