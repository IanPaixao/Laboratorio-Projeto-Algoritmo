cases = int(input())
 
for i in range(cases):
 n, m = list(map(int,input().split()))
 Sum = 0
 counter = 0
 array = []
 array=list(map(int,input().split()))
 
 while m > Sum:
  highest = max(array)
  Sum += highest
  counter += 1
   
 while m != Sum:
     lowest = min(array)
     Sum -= lowest
     counter +=1
 print(counter)
 print(Sum)
