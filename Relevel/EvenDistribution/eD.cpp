    #include <iostream>
    using namespace std;

    int main(){
        int t;
        cin>>t;
        while(t--){
            int n,m,i,e = 0;
            cin>>n;
            m = 2*n;
            long long int a[m];
            for(i=0;i<m;i++){
                cin>> a[i];
                if(a[i]%2 !=0)
                e++;
            }
            if(e%2 == 0){
                cout<<"YES";
            }else{
                cout<<"NO";
            }
            
        }
        return 0;
    }