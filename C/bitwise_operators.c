#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
//Complete the following function.


void calculate_the_maximum(int n, int k) {
  //Write your code here.
  int and[2]={0},or[2]={0},xor[2]={0};
  
  for(int i=1;i<=k;i++)
  {
      for(int j=i+1;j<=n;j++)
      {
          if((i&j)<k){
              and[1] = i&j;
              if(and[0]<and[1])
                and[0]=and[1];  
          }
          if((i|j)<k){
              or[1] = i|j;
              if(or[0]<or[1])
                or[0]=or[1]; 
          } 
          if((i^j)<k){
              xor[1] = i^j;
              if(xor[0]<xor[1])
                xor[0]=xor[1]; 
              
          }  
      }
  }
  printf("%d\n",and[0]);
  printf("%d\n",or[0]);
  printf("%d",xor[0]);
  
}

int main() {
    int n, k;
  
    scanf("%d %d", &n, &k);
    calculate_the_maximum(n, k);
 
    return 0;
}