/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main(int argc, char* argv[])
{
    char arr[50];
    int arr_[50];
    
    cin.getline(arr,50);
    char separator = ' ';
    int i = 0;
    
    string s;
    string n;
    while (arr[i] != '\0'){
        if(arr[i] != separator){
            s+=arr[i];
        }else{
            n = s;
            s.clear();
        }
        i++;
    }
    
    int intN = stoi(n);
    int intS = stoi(s);
    cout << stoi(n) << endl; 
    cout << stoi(s) << endl; 
    
    cin.getline(arr,50);
    char separator = ' ';
    int i = 0;
    
    string s;
    string n;
    while (arr[i] != '\0'){
        if(arr[i] != separator){
            
        }else{
            s.clear();
        }
        i++;
    }
}
