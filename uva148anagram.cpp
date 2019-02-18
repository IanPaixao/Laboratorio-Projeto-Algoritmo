#include <iostream>
#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
using namespace std;
const vector<string> explode(const string& s, const char& c);
string split(string word);
bool contains(string primeira, string segunda);
string stringremove(string primeira, string segunda);
string concat(vector<string> teste);
void anagram_checker(string phrase, vector<string> dictphrase);
vector<string> removeword(vector<string> wordss2, vector<string> substrings);

int main(){
  string read;
  string phrase;
  vector<string> dict;
  vector<string> phrases;

  while (cin >> read, read != "#"){
    dict.push_back(read);
  }//end while
  cin.ignore();
  
  while (getline(cin,phrase), phrase != "#"){
    phrases.push_back(phrase);
  }//end while
  for(int index = 0; index < phrases.size(); index ++){
    vector<string> dictphrase;
    string resposta = phrases[index];
    string aux = split(resposta); 
    sort(aux.begin(),aux.end()); 
    for(int i = 0; i < dict.size(); i++){
      if(contains(dict[i],aux)){ 
        dictphrase.push_back(dict[i]);
      }//end if
    }//end for
    vector<string> str = explode(phrases[index],' ');
    anagram_checker(phrases[index],removeword(str,dictphrase));
  }//end for
  return 0;
}//end main

/*
From a string to a vector
*/
const vector<string> explode(const string& s, const char& c){
  string buff = "";
  vector<string> v;
  for(auto n:s){
    if(n != c) buff+=n; else
    if(n == c && buff != "") { v.push_back(buff); buff = ""; }//end if
  }//end for
  if(buff != "") v.push_back(buff);
  return v;
}//end explode
/*
Erase blank spaces from a string.
*/
string split(string word){
  word.erase(remove(word.begin(), word.end(), ' ' ),word.end());
  return word;
}// end split

/*
Checks if a string is whitin a another
*/
bool contains(string first, string second){
  string a = first; 
  string b = second; 
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  bool aux = false;
  string intersection;
  set_intersection(a.begin(), a.end(),b.begin(),b.end(), back_inserter(intersection));
  if(intersection.length() == a.length()){
    aux = true;
  }//end if
  return aux;
}//end contains
/*
Erase a string whitin a another.
*/
string stringremove(string first, string second){
  string a = first; 
  string b = second; 
  sort(a.begin(), a.end());
  sort(b.begin(), b.end());
  string symmetricdifference;
  set_symmetric_difference(a.begin(), a.end(),b.begin(),b.end(), back_inserter(symmetricdifference));
  return symmetricdifference;
}//end stringremove
/*
Concatenate a vector to form a string
*/
string concat(vector<string> teste){
  string c = "";
  for(int i = 0; i < teste.size(); i++){
    c += teste[i];
  }//end for
  return c;
}//end concat
/*
The Anagram Checker Method.
*/
void anagram_checker(string phrase, vector<string> dictphrase){
  vector<string> dictAux = dictphrase; 
  vector<string> anagrams;
  while(dictAux.size() > 0 && phrase.length() < concat(dictAux).length()){
    int i = 0;
    string copy = phrase; 
    copy = split(copy); 
    sort(copy.begin(),copy.end()); 
    vector<string> candidate;
    vector<int> array;
    do{
      if(contains(dictAux[i],copy)){
        copy = stringremove(copy, dictAux[i]);
        array.push_back(i);
         candidate.push_back(dictAux[i]);
      }//end if
       
      if(copy.length() == 0){
        bool is = false;
        string a = concat( candidate);
        for (int j = 0; j < anagrams.size(); j++){
          if(anagrams[j] == a){
            is = true;
          }//end if
        }//end for
        if(is == false){
          cout << phrase << " = ";
          for (int j = 0; j < candidate.size(); j++){
            cout << candidate[j] << " ";
          }//end for
          cout << endl;
          anagrams.push_back(a);
        }// end if
      }//end if
      // if(!anagram) continue
      if( i == dictAux.size() - 1){
        if(array.at(array.size() - 1) != dictAux.size() - 1){
          i = array.at(array.size() - 1) + 1;
          array.pop_back();
          copy += candidate.at(candidate.size() - 1);
          candidate.pop_back();
        }//end if 
        else {
         array.pop_back();
          i = array.at(array.size() - 1) + 1;
          array.pop_back();
          copy += candidate.at(candidate.size() - 1) + candidate.at(candidate.size() - 2);
          candidate.pop_back();
          candidate.pop_back();
        }//end else
      }//end if
      else{
        i++;
      }//end else
    }while(!array.empty());//end do
    dictAux.erase(dictAux.begin());
  }//end while
}//end anagram_checker
/*
Erase equals words from the second vector
*/
vector<string> removeword(vector<string> words2, vector<string> substrings){
  for(int i = 0; i < words2.size();i++){
    for(int j = 0; j < substrings.size();j++){
      if(words2[i] == substrings[j])substrings.erase(substrings.begin() + j);
    }//end for
  }// end for
  return substrings;
}//end