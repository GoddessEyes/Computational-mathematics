#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float FX(float K){


//return 0.5*(sin(((3+K)*(3+K))/2.0))*log(K+2.0);
return K*K;
}

int main(){
	printf("Метод прямоугольников : \n");
int N ;
float SX = 0.0;
float SX1 = 1.0;
printf("введите N: \n");
    if(scanf("%d", &N)!=1){
        printf("ERROR");
        exit(EXIT_FAILURE);

	}
	float A;
	printf("введите A: \n");

		        if(scanf("%f", &A)!=1){
               printf("ERROR");
               exit(EXIT_FAILURE);
	}

	float B;
	printf("введите B: \n");
		        if(scanf("%f", &B)!=1){
               printf("ERROR");
               exit(EXIT_FAILURE);
	}

float E;
	printf("введите E: \n");
		        if(scanf("%f", &E)!=1){
               printf("ERROR");
               exit(EXIT_FAILURE);
	}



float H;
H = (B-A)/N;
float X[100000];


int l= 1;

while( fabsf( SX - SX1)  > E){

SX = SX1;
H = H/2.0;
N =2*N;
SX1= 0.0;
printf("%d \n",l++);

for(int i= 1; i <= N; i++ ) {
X[i]= A + i*H;
SX1 += FX(X[i]);              }

SX1 = SX1*H;
}

printf("%.7f/n", SX);



return 0;
}
