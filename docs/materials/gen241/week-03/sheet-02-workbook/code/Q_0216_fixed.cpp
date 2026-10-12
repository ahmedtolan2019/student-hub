// GEN 241 - Sheet 2 - Q16
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  local hour:minute:second in 12-hour format
//   HAVE  elapsed seconds and integer GMT-hour offset
//   CONVERT  seconds to minutes and hours; wrap hours
//   RELATE  AM if hour24<12; display hour24%12, replacing 0 with 12
//   CHECK  test midnight, noon, rollover and negative offset
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    long totalSeconds; int offset;
    // Deterministic teaching harness: input fixed seconds and integer offset.
    cin >> totalSeconds >> offset;
    long second=totalSeconds%60;
    long minute=(totalSeconds/60)%60;
    long hour24=((totalSeconds/3600+offset)%24+24)%24;
    long hour12=hour24%12;
    if(hour12==0) hour12=12;
    cout << "second=" << second << "\nminute=" << minute << "\nhour24=" << hour24 << "\nhour12=" << hour12 << endl;
    cout << "time=" << hour12 << ":" << minute << ":" << second << " ";
    if(hour24<12) cout << "AM" << endl; else cout << "PM" << endl;
    return 0;
}
