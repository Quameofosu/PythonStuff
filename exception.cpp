#include<iostream>


using namespace std;


int main()
{
	int donut, icycup;
	double dpi;
	
	
	
	cout<<"Enter number of donuts bought by customer";
	cin>>donut;
	cout<<"Enter number of cups of icycups bought by customer";
	cin>>icycup;
	cout<<endl;
	
	
	
	
	try{
	
	  	if(icycup<=0)
	  		throw donut;
	  	dpi= donut/static_cast<double>(icycup);
	  	
	  	
	  	
	cout<< donut<<"donuts.\n"
		<<icycup<<"cups of icycups.\n"
		<<dpi <<" is the ratio of donuts to icycup bought by customer";
	}//try block
	
	
	catch (int x){
		cout<<x<<" donuts have been bought and no cups of IcyCups "<<endl
			<<"Please buy some ICYCUPS!!!\n";
			
			
	}//end of catch
	
	
	
	
	
	
	
	return 0;
}//end of main