#include <iostream>
#include <string>
#include <cmath>
#include <cstdlib>
#include <iomanip>
#include <fstream>

using namespace std;

struct LabReading
{
	float AlphaEnergies;
	int Total_Impulses;
};

void Standard_Deviation(LabReading);

int main()
{
	LabReading Temp;
	
	cout<<endl;
	cout<<endl;
	Standard_Deviation(Temp);
	
	ifstream readdata ("Data9.txt");
	string header;
	
	cout<<endl;
	cout<<endl;
	cout<<endl;
	 
	 cout<<"Displaying Experimental Results In A Tabular Form"<<endl;
	 cout<<endl;
	
	cout<<"Alpha Energies Readings (E/KeV)"
	    <<setw(25)<<"Impulse Reading"<<endl;
	
	if(readdata.is_open())
	{
		getline(readdata,header);
		
		while(!readdata.eof())
		{
			readdata>>Temp.AlphaEnergies
			        >>Temp.Total_Impulses;
			  
		
		    cout<<fixed<<showpoint<<setprecision(1)<<Temp.AlphaEnergies<<setw(45)
		        <<Temp.Total_Impulses<<endl;
		     
		
		}
		     
	readdata.close();	
		
	}else cout<<"ERROR......Input File Not Found\nPlease Try again"<<endl;
	
	
	cout<<endl;
	cout<<endl;
	
	system ("pause");
	return 0;
}

void Standard_Deviation(LabReading temp)
{   
	ifstream readfile ("Data9.txt");
	
	string line;
	int total,sum;
	float mean, variance, stdDeviation;
	
	if(readfile.is_open())
	{
		getline(readfile,line);
		
		while(!readfile.eof())
		{
			readfile>>temp.AlphaEnergies
			        >>temp.Total_Impulses;;
			
			sum+= temp.AlphaEnergies;
		
		   total += temp.Total_Impulses;
		} 
		   
			mean = sum/9;
			 variance += pow(temp.AlphaEnergies - mean, 2);
			  variance = variance/9;
			  stdDeviation = sqrt(variance);
			    
		    cout<<"The standard deviation of the Alpha"
		        <<" Energy Readings are: "
				<<stdDeviation<<endl;
		
		  
	     cout<<"The sum total of the impulses"
		     <<" recorded in the experiment  are: "<<total<<endl;
		     
	
		
		     
	readfile.close();	
		
	}else cout<<"ERROR......Input File Not Found\nPlease Try again"<<endl;
	
	
}
