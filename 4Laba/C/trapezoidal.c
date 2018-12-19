#include<stdio.h>
#include<stdlib.h>
#include<math.h>

float FX(float K){


//return 0.5*(sin(((3+K)*(3+K))/2.0))*log(K+2.0);
return K*K;
}

int main(){
	printf("Метод трапеций = \n");
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
float Ipr, Q , Ipr1;
Q = 0.0;
Ipr = 0.0;
Ipr1 = 1.0;


int l = 1;
while( fabsf( Ipr - Ipr1)  > E){

Ipr = Ipr1;
H = H/2.0;
N =2*N;
Ipr1= 0.0;
Q = 0.0;
printf("%d \n",l++);
for(int i = 0 ; i <= N ; i++){
	X[i]= A + i*H;
	Y[i]= FX(X[i]);

}

for(int i= 1; i <= N-1; i++ ) {
X[i]= A + i*H;
Q += FX(X[i]);;              }

Ipr1 = H*(((Y[0]+Y[N])/2.0)+Q);
}


printf("%.7f", Ipr);
return 0;
}




