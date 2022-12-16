#include <iostream>
#include "Employee.h"

using namespace std;

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main() {
	
	Employee peter;
	peter::setgender("peter agyemang oppong");
	cout<<"the name of employee is:"<<peter::getname();
	
	return 0;
}