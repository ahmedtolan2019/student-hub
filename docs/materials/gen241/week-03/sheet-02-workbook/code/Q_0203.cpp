// GEN 241 - Sheet 2 - Q3
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  whole years, assumed months, remaining days
//   HAVE  nonnegative whole days
//   CONVERT  365-day years, explicitly assumed 30-day months
//   RELATE  remove full years then split remaining days
//   CHECK  reconstruct days; confirm months versus weeks
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    int days; cin >> days;
    if (days < 0) { cout << "Invalid days" << endl; return 0; }
    int years = days / 365;
    int rem = days % 365;
    int months = rem / 30;
    int left = rem % 30;
    cout << "years=" << years << "\nremaining=" << rem << "\nmonths=" << months << "\ndays=" << left << endl;
    return 0;
}
