#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>

using namespace std;

struct Student{
	string ID;
	string index;
	string LName;
	string FName;
	float midsem;
	float finalmark;
	float totalmark; 
};
 void Reader(Student temp);
 
int main(){
	Student pupil;
	cout<<"Starting program..."<<endl;
	Reader(pupil);
	
	return 0;
}


void Reader(Student Temp){
	string header;
	ifstream infile("Data file.txt");
	ofstream outfile("Processed data.txt");
	
	outfile<<"INDEX NUMBER"<<"\t LAST NAME"<<"\tTOTAL MARK"<<endl;
	outfile<<"---------------------------------------------------------------------------------------------------------------------"<<endl;
	
if(infile.is_open()){
	getline(infile, header);
	while(!infile.eof()){
	infile>>Temp.ID>>Temp.index>>Temp.LName>>Temp.FName>>Temp.midsem>>Temp.finalmark;
	Temp.totalmark = Temp.midsem + Temp.finalmark;
	outfile<<Temp.index<<setw(18)<<Temp.LName<<setw(15)<<Temp.totalmark<<endl;
		}
		
	cout<<" Run sucessfully.."<<endl;	
	}
	else cout<<"File not found";
	
	infile.close();
	outfile.close();
}
