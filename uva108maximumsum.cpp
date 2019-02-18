#include <iostream>
#include <vector>
using namespace std;
int largesum(vector<int> , int size);
int main() {
  //cout << "Hello World!\n";
  int size;
  int aux;
  cin >> size;
  int array[size][size];
  vector<int> subarray;
  vector<int> subarray2;
  vector<int> subarray3;
  vector<int> subarray4;
  for(int i=0;i < size ;i++){
      for(int j=0;j < size; j++){
        cin >> aux;
        if(aux != ' ') array[i][j] = aux;
      }//end for
  }//end for
  
for(int i=0;i < size ;i++){
      for(int j=0;j <size/2; j++){
             subarray.push_back(array[i][j]);
             //cout << array[i][j]<<endl; 
          
      }//end for
  }//end for
  
  for(int i=0;i < size ;i++){
      for(int j=size/2;j < size; j++){
             subarray2.push_back(array[i][j]);
             //cout << array[i][j]<<endl; 
          
      }//end for
  }//end for

  for(int i=0;i < size/2 ;i++){
      for(int j=0;j <size; j++){
             subarray3.push_back(array[i][j]);
             //cout << array[i][j]<<endl; 
          
      }//end for
  }//end for

  for(int i=size/2;i < size ;i++){
      for(int j=0;j <size; j++){
             subarray4.push_back(array[i][j]);
             //cout << array[i][j]<<endl; 
          
      }//end for
  }//end for
  
  int ans1=largesum(subarray, subarray.size());
  int ans2=largesum(subarray2,subarray2.size());
  int ans3=largesum(subarray3, subarray3.size());
  int ans4=largesum(subarray4,subarray4.size());

  if((ans1>ans2)&&(ans1>ans3)&&(ans1>ans4))cout << ans1<< endl;
  if((ans2>ans1)&&(ans2>ans3)&&(ans2>ans4))cout << ans2<< endl;
  if((ans3>ans2)&&(ans3>ans1)&&(ans3>ans4))cout << ans3<< endl;
  if((ans4>ans2)&&(ans4>ans3)&&(ans4>ans1))cout << ans4<< endl;

}//end main


int largesum(vector<int> a, int size){
    int max=0;
    int sum=0;
    for(int i=0;i<size;i++){
    max+= a[i];
    if(sum < max)sum=max;
    if(max<0)max=0;
    }// end for
    return max;
}//end largesum