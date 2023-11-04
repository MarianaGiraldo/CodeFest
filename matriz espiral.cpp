#include <bits/stdc++.h>
#include <iostream>
#include <cmath>
#include <math.h>
#include <vector>
#include <string>
#include <map>

typedef long long ll;
#define fastInp cin.tie(0); cout.tie(0); ios_base::sync_with_stdio(0);
 
using namespace std;

ll** espiral(ll n){
    ll repeticiones,i,j,k;
    ll** matriz = new ll*[n];
    // rellenar matriz con ceros
    for (i=0; i<n; i++) {
        matriz[i] = new ll[n];
        for (j=0; j<n; j++) {
            matriz[i][j] = 0;
        }
    }
    // establecer limites
    if (n%2!=0){
        repeticiones=floor(n/2);
    }
    if (n%2==0){
        repeticiones=floor(n/2)-1;
    }
    for (j=0;j<repeticiones+1;j++){
        // esquina superior izquierda
        if (j==0){
            matriz[j][j]=1;
        }else{
            matriz[j][j]=matriz[j][j-1]+1;
        }
        // fila arriba
        for (i=j+1;i<n-j;i++){
            matriz[j][i]=matriz[j][i-1]+1;
        }
        // columna derecha
        for (i=j+1;i<n-j;i++){
            for (k=n-j-1;k<n-j;k++){
                matriz[i][k]=matriz[i-1][k]+1;
            }
        }
        // fila abajo
        for (i=0;i<n-2*j-1;i++){
            matriz[n-j-1][n-i-j-2]=matriz[n-j-1][n-i-j-1]+1;
        }
        // columna izquierda
        for (i=0;i<n-2-2*j;i++){
            for (k=0;k<j+1;k++){
                matriz[n-i-j-2][k]=matriz[n-i-k-1][k]+1;
            }
        }
    }
    return matriz;
}

int main(){
    fastInp;
    ll n,i,j;
    cin >> n;
    ll** matriz=espiral(n);
    // imprimir matriz
    for (i=0;i<n;i++){
        for(j=0;j<n;j++){
            cout << matriz[i][j] << " ";
        }
        cout << endl;
    }
}