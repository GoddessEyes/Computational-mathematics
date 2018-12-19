#include <iostream>

float f (float x)
{
    return (sin(((x/2) + 2)^2))^2- x/5;
}
float pf(float x)
{
    return 0.5*(x+4)*sin(((x^2)/2) + 4*x + 8) - 0.2;
}
float pf2(float x)
{
    return cos((2 + x/2)^2)*sin((2 + x/2)^2) + 0.5*(4.0 + x)^2*cos((2 + x/2)^2)^2 - 0.5*(4.0 + x)^2*sin((2 + x/2)^2)^2;
}
int main() {
    float a,b,c,d,e, x_pr
    float a_i, b_i;

    int n = 0;

    cout <<"a="; cin >> a_i;
    cout <<"b="; cin >> b_i;
    cout <<"e="; cin >> e;

    //метод половинного деления

    a = a_i;
    b = b_i;
    while (b-a > e)
    {
        n++;
        c = (a+b)/2;
        if (f(a)*f(c) < 0) b = c;
        else a = c;
    }

    x_pr = (a+b)/2;
    cout << "x_pr=" << x_pr << " " << f(x_pr)<< "n=" << n << endl;

    //метод хорд и касательных

    a = a_i;
    b = b_i;
    n = 0;

    while (b-a > e)
    {
        n++;
        c = a -f(a)/(f(b) - f(a));
        d = a - f(a)/pf(a);
        b=c;
        a=d;
    }

    x_pr = (a+b)/2;
    cout << "x_pr=" << x_pr << " " << f(x_pr)<< "n=" << n << endl;

    // метод итераций

    double lambda = 0.1;

    double x_pred, x_sled;
    x_sled = a;
    x_pred = b;

    while (fabs (x_pred - x_sled)>e)
    {
        x_pred = x_sled;
        x_sled = x_pred-lambda*f(x_pred);
    }

    x_pr = x_sled;
    cout << "x_pr=" << x_pr << " " <<f(x_pr) << "n=" << n << endl;
    return 0;
}