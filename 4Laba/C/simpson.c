#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float FX(float K){


//return 0.5*(sin(((3.0+K)*(3+K))/2.0))*log(K+2.0);
return K*K;
}

int main(){
	printf("Метод Симпсона = \n");
int N ;

printf("введите N: \n");
    if(scanf("%d", &N)!=1){
        printf("ERROR");
        exit(EXIT_FAILURE);

	}
	float A;
	printf("Input A: \n");

		        if(scanf("%f", &A)!=1){
               printf("ERROR");
               exit(EXIT_FAILURE);
	}

	float B;
	printf("Input B: \n");
		        if(scanf("%f", &B)!=1){
               printf("ERROR");
               exit(EXIT_FAILURE);
	}

float E;
	printf("Input E: \n");
		        if(scanf("%f", &E)!=1){
               printf("ERROR");
               exit(EXIT_FAILURE);
	}



float H;
H = (B-A)/N;
float X[100000];
float Y[100000];
float Ipr, Q , W;
Q = 0.0;
W = 0.0;


float Ipr1;
Ipr = 0.0;
Ipr1 = 1.0;
while( fabsf( Ipr - Ipr1)  > E){

Ipr = Ipr1;
H = H/2.0;
N =2*N;
Ipr1= 0.0;
Q = 0.0;
W = 0.0;
printf("%d \n",N);
for(int i = 0 ; i <= N ; i++){
	X[i]= A + i*H;
	Y[i]= FX(X[i]);

}
for(int i = 1 ; i <= N/2.0 ; i++){
	X[i]= A + i*H;
	Q += FX(X[2*i-1]);

}



for(int i = 1 ; i <= (N - 1)/2 ; i++){
	X[i]= A + i*H;
	W += FX(X[2*i]);

}

Ipr1 =(1.0/3.0)*H*(Y[0]+ 4.0*Q + 2.0*W + Y[N]);
}




printf("%.7f", Ipr);


}




