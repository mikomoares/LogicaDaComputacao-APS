/*Teste de função recursiva*/

int soma(int x, int y) {
    int a;
    a = x + y;
    printy(a);
    ret a;
}

int fatorial(int n){
    si(n == 0){
        ret 1;
    }

    ret n*fatorial(n-1);
}

int main() {
    int a;
    int b;
    int x;
    a = 3;
    x = 4;
    b = soma(a, 4);
    x = fatorial(x);
    printy(x);
    printy(a);
    printy(b);
}