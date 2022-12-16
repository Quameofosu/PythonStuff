#include<iostream>


using namespace std;


int main(){
	int choice;
	
	
	try{
		
		cout<<"Enter any integer:>>";
		cin>>choice;
		
		
		if (choice==0) cout<<"hello world";
		else if (choice ==1) throw (100); //throw integer value
		else if (choice ==2) throw ('A'); //throw character value
		else if (choice ==3) throw (1.2f); //throw float value
		else cout<<"Bye Bye"<<endl;
		
	}//try block
	
	catch(int a){
		cout<<"Integer value exception block is: "<<a<<endl;
	}
	
		catch(char b){
		cout<<"character value exception block is: "<<b<<endl;
	}
	
		catch(float c){
		cout<<"floating point value exception block is: "<<c<<endl;
	}//end of catch block
	
	return 0;
}