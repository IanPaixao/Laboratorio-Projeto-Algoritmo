/*
 * Festival
 */

#include <iostream>
#include <vector>
using namespace std;

//Struct: Festival
typedef struct {
    int qt_blocos{};
    int comprimento{};
    vector<int> blocos;
} Festival;

Festival festival;

//Preenche Festival
void preencheFestival() {
    cin >> festival.qt_blocos >> festival.comprimento;
    int bloco;
    
    for(int i=0; i<festival.qt_blocos; i++){
        cin >> bloco;
        festival.blocos.push_back(bloco);
    }
}

//Limpa Festival
void limpaFestival() {
    festival.blocos.clear();
}

//Minimiza a quantidade de blocos
int minimizarBlocos(){
    int matriz[100][1000] = {0};

    for(int j=0; j<=festival.comprimento; j++){
        matriz[0][j] = j;
    }

    for(int i=1; i<festival.qt_blocos; i++) {
        for(int j=0; j<=festival.comprimento; j++){
            if(festival.blocos[i] > j){
                matriz[i][j] = matriz[i-1][j];
            } else if(matriz[i-1][j] > matriz[i][j-festival.blocos[i]] + 1){
                matriz[i][j] = matriz[i][j-festival.blocos[i]] + 1;
            } else {
                matriz[i][j] = matriz[i-1][j];
            }
        }
    }

    return matriz[festival.qt_blocos-1][festival.comprimento];
}

//Funcao Principal
int main() {
    int instancia;
    cin >> instancia;

    for(int i=0; i<instancia; i++){
        preencheFestival();
        cout << minimizarBlocos() << endl;
        limpaFestival();
    }

    return 0;
}