// Q1 MODULATING THE ARRAY

// Problem Statement
// Amy has an array A, of N integers. She also has an integer K, such that 0<=K<=MIN(A1, A2,..., A (N) ) 
// Here MIN denotes the Minimum of the array.

// She wants to "modulate" the array with positive integer M. 
// "Modulating an array with M, for each i between 1 to N, she converts Ai=(Ai - K)%M 

// For example, if N=3, K = 1 and A = [2, 5, 3] then after
// modulating the array with M = 2 it becomes A = [1, 0, 0]
// She was given Q queries. In each query she has index of the array A, X and Y ( 1 <= X, Y <= N, X may be equal to Y) 
// and is ask to find how many positive values of M exists such that after modulating the array with M, Ax becomes equal to Ay.
// If infinite such values of M exists print -1. Since she is busy in her job interview, she asks you to help her answer the queries.

#include<bits/stdc++.h>
using namespace std;

int main(){
    int n,k,q;
    cin>>n>>k>>q;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    int x,y;
    while(q--){
        cin>>x>>y;
        if(a[x-1]==a[y-1]){
            cout<<"-1\n";
            continue;
        }
        // int count=1;
        // int limit=max(a[x-1],a[y-1]);
        a[x-1]-=k;
        a[y-1]-=k;
        int factor=abs(a[x-1]-a[y-1]);
        int count_of_factors=0;
        for(int i=1;i*i<=factor;i++){
            if(factor%i==0){
                if(factor/i==i){
                    count_of_factors++;
                }
                else{
                    count_of_factors+=2;
                }
            }
        }
        cout<<count_of_factors<<endl;

        // for(int i=2;i<=limit;i++){
        //     if((a[x-1]-k)%i==(a[y-1]-k)%i){
        //         count++;
        //     }
        // }
        // for(int i=limit;i>=2;i-=min(a[x-1],a[y-1])){
        //     if((a[x-1]-k)%i==(a[y-1]-k)%i){
        //         count++;
        //     }
        // }
        // cout<<count<<endl;
    }
    return 0;
}