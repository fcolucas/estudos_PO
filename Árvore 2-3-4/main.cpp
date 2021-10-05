#include <iostream>
#include "tree.cpp"
#include <stdlib.h>
#include <stdio.h>

using namespace std;

int main() {

	//Isso é uma Instancia da classe
	Arvore234 arvore234 = Arvore234();

    char op;
    int num, i, j;

    while(1){
        cout << "\n********************************\n" << endl;
        cout << "*        ARVORE 2-3-4          *\n" << endl;
        cout << "********************************\n" << endl;

    	op = menu_principal();
    	cout << "\n\n" << endl;

        if(op == '0') {
            break;
        }

        switch(op)
        {
            case '1':

                cout << "  Digite a quantidade de numeros: ";
                scanf("%d",&j);
                fflush(stdin);

                for(i = 0; i < j; i++){

                    cout << "  Digite um numero: ";
                    scanf("%d",&num);
                    fflush(stdin);

                    cout << "\n  Numero " << num << " inserido na arvore\n" << endl;
                    arvore234.inserir(num);
                }

                break;

            case '2':
                cout << "  Digite um numero: ";
                scanf("%d",&num);
                fflush(stdin);

				cout << "\n  Numero " << num << " excluido da arvore\n" << endl;
		        arvore234.remover(num);
                break;

            case '3':

                cout << "  Digite um numero: ";
                scanf("%d",&num);
                fflush(stdin);

                if(arvore234.buscaValor(num))
                    cout << "  Numero encontrado na arvore" << endl;
                else
                    cout << "  Numero nao pertence a arvore" << endl;
                break;

            case '4':

                arvore234.imprime();
                fflush(stdin);
                break;

            default:
                cout <<"\n  Opcao Invalida\n" << endl;
                break;
        }
    }

	return 0;
}
