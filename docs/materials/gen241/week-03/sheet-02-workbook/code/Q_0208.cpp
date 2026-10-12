// GEN 241 - Sheet 2 - Q8
// Worked learning example. Read the source note in the workbook.
// PLAN
//   WANT  trip cost in pounds
//   HAVE  distance km; consumption L/100km; price pounds/L
//   CONVERT  distance to 100km blocks, then litres
//   RELATE  cost=(distance/100.0)*consumption*price
//   CHECK  lower consumption must lower cost
#include <iostream>
#include <cmath>
#include <ctime>
using namespace std;

int main()
{
    double km,consumption,price; cin >> km >> consumption >> price;
    double blocks=km/100.0;
    double litres=blocks*consumption;
    double cost=litres*price;
    cout << "blocks=" << blocks << "\nlitres=" << litres << "\ncost=" << cost << endl;
    return 0;
}
