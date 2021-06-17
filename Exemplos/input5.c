int soma_inputs(){
    int a;
    int b;
    printy("digite 2 numeros a serem somados");
    a = imputi();
    b = imputi();
    ret a+b;
}

int main() {
    int a;
    a = soma_inputs();
    printy(a);
}