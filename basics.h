#ifndef EMPLOYEE_H
#define EMPLOYEE_H
#include <string>
using namespace std;

class Employee
{
	private:
		string name;
		char gender;
		short age;
		float salary;
		
	public:
		void setname(string name);
		void setage(short age);
		void setgender(char gender);
		void setsalary(float salary);
		string getname();
	    char getgender();
	    short getage();
	    float getsalary();
};

#endif