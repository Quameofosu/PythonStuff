#include "Employee.h"

void Employee::setage(short age){
	this->age = age;
}

void Employee::setname(string name){
	this->name = name;
}

void Employee::setgender(char gender){
	this->gender = gender;
}

void Employee::setsalary(float salary){
	this->salary = salary;
}

string Employee::getname(){
	return name;
}

short Employee::getage(){
	return age;
}

char Employee::getgender(){
	return gender;
}
