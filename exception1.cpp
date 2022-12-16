#include<iostream>


using namespace std;


int main(){
	
	int age =0;
	
	cout<<"Enter Age";
	cin>>age;
	
	
	
	try{
		if(age >=18){
			cout <<"Access granted you are old enough"<<endl;
		}//end of if block
		
		else{
			cout<<"Access denied";
		}
		throw age;
		
		
		
		
		
	}//end of try block
	
	
	catch (int e){
		
		cout<<"Access denied-You must be 18 years old"
			<<"You are only "<<e<<" years old.";
	}//end of catch
	
	return 0;
}