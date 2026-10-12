// GEN 241 - Sheet 2 - Q18
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  BMI value and the sheet table label
//   HAVE  fictional kg and height in cm
//   CONVERT  cm/100.0 to metres before squaring
//   RELATE  kg/(metres*metres), then ascending table bounds
//   CHECK  test each exact threshold in the supplied table
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    double kg,cm; cin >> kg >> cm;
    if(kg<=0 || cm<=0) { cout << "Invalid input" << endl; return 0; }
    double metres=cm/100.0;
    double bmi=kg/(metres*metres);
    cout << "metres=" << metres << "\nbmi=" << bmi << endl;
    if(bmi<18.5) cout << "Underweight" << endl;
    else if(bmi<25) cout << "Normal" << endl;
    else if(bmi<30) cout << "Overweight" << endl;
    else cout << "Obese" << endl;
    return 0;
}
