#include <stdio.h>

typedef struct {
    int x;
    int y;
} point;

int inside(point p, point poly[], int n) {
    //if p inside poly return 1, else return 0
    return 0;
}

int verify(point p, point a, point b){
    //p: pontp; a e b representam as extremidades de uma aresta
    //if p in aresta return 2; else if um raio soltado por p
    //para a direita cruza a aresta; else caso contrário

    double m = (b.y - a.y)/(b.x - a.x);
    double n = a.y - m*a.x;

    int maior, menor;
    if (a.y > b.y) {
        maior = a.y;
        menor = b.y;
    } else {
        maior = b.y;
        menor = a.y;
    }

    if (menor < p.y && p.y < maior) {
        double x = (p.y - n)/m;
        if (x > p.x) {
            return 1;
        } else if (abs(x) == abs(p.x)) {
            return 2;
        }
        return 0;
    }
    
    return 0;
}

int main() {


    return 0;
}