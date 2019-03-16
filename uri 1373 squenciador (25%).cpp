#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
using namespace std;

int max(int a, int b); 
int lcs( string X, string Y, int length, int length2 ); 

int main() {
       
    //cout << "Hello there";
    short n;
    string X = ""; 
    string Y = "";
    int length = 0;
    int length2 = 0;
    while( cin >> n && n != 0 ) {
      cout << endl;
      cin >> X;
      //cout << X << endl;
      cin >> Y;
      //cout << Y << endl;
      length = X.length(); 
      length2 = Y.length();
      //cout << length << endl; 
       //cout << length2 << endl; 
      cout << lcs( X, Y, length, length2 );
    }//end while
}//end main

/* Function to get max of 2 integers */
int max(int a, int b) { 
	return (a > b)? a : b; 
}// end max 

/* Returns length of LCS for X[0..m-1], Y[0..n-1] */
int lcs( string X, string Y, int length, int length2 ) { 
if (length == 0 || length2 == 0) 
return 0; 
if (X[length-1] == Y[length2-1])
return 1 + lcs(X, Y, length-1, length2-1); 
else 
return max(lcs(X, Y,length, length2-1), lcs(X, Y, length-1, length2)); 
}//end lcs 