#include <stdio.h>
#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
string left_trim( string s );
string right_trim( string s );
string trim( string s );
string remove_spaces( string s );

int main() {
     
    //cout << "Hello there";
    short n;

    while( cin >> n && n != 0 ) {
        string *threads = new string[ n ];
        cin.ignore();
        int max = 0;
         
        for( short i = 0; i < n; i++ ) {
            getline( cin, threads [ i ] );
            threads [ i ] = remove_spaces( trim( threads [ i ] ) );
             
            if( threads [ i ].size() > max ) {
                max = threads [ i ].size();
            }//end if
        }//end for
         
        for( short i = 0; i < n; i++ ) {
            cout << setw( max ) << threads [ i ] << endl;
        }//end for
        cout << endl;
    }// end while
     
    return 0;
}//end main

string trim (string s){
   s.substr( s.find_first_not_of( " " ) );
   s.substr( 0, s.find_last_not_of( " " ) + 1 );
   return s;
}//end trim
 
string remove_spaces( string s ) {
    string r = "";
    string::iterator it;
    int spaces = 0;
     
    for( it = s.begin(); it != s.end(); it++ ) {
        if( *it != ' ' ) {
             
            if( spaces > 0 ) {
                r += " ";
                spaces = 0;
            }//end if
             
            r += *it;
        }// end if
        else {
            spaces += 1;
        }// end else
    }//end for
     
    return r;
}// end remove
 
