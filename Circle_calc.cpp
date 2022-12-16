#include <iostream>

using namespace std;
class circle{
	private:
		float area, circu, radius;
	    const float pi=3.14;
	    
	    public:
	    	float areacalc(float a){
	    		radius = a;
	    		area = pi * a*a;
	    		return area;
			}
			
			float circucalc(float b){
	    		radius = b;
	    		area = pi *b;
	    		return circu;
			}
			void printcircu(){
			cout<<"the circumference of circle:"<<circu<<endl;
		}
		
			void printarea(){
			cout<<"the area of circle:"<<area<<endl;
		}
		
	
	
};

int main(){
	circle obj;
	float n;
	cout<<"Hello There"<<endl;
	cout<<"enter the radius:"<<endl;
	cin>>n;
	
	obj.areacalc(n);
	obj.circucalc(n);
	obj.printarea();
	obj.printcircu();
	
	
	
	
	return 0;
}