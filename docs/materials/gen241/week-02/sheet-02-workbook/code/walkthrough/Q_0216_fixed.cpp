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
    // 1. read fixed seconds and the hour offset
    long totalSeconds;
    int offset;
    // Deterministic teaching harness: input fixed seconds and integer offset.
    cin >> totalSeconds >> offset;
    // 2. second and minute within the current hour
    long second = totalSeconds % 60;
    long totalMinutes = totalSeconds / 60;
    long minute = totalMinutes % 60;
    // 3. whole hours, add the offset, wrap into 0..23
    long utcHours = totalSeconds / 3600;
    long localHours = utcHours + offset;
    long wrapped = localHours % 24;
    long positive = wrapped + 24;
    long hour24 = positive % 24;
    // 4. 12-hour display: show 12 instead of 0
    long hour12 = hour24 % 12;
    if (hour12 == 0)
    {
        hour12 = 12;
    }
    // 5. display
    cout << "second=" << second << "\nminute=" << minute << "\nhour24=" << hour24 << "\nhour12=" << hour12 << endl;
    cout << "time=" << hour12 << ":" << minute << ":" << second << " ";
    if (hour24 < 12)
    {
        cout << "AM" << endl;
    }
    else
    {
        cout << "PM" << endl;
    }
    return 0;
}
