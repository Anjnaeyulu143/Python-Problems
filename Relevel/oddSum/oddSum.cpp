#include <iostream>
using namespace std;

int main() {
    // Number of elements in the array
    int n;
    cin>>n;
    int oddCount = 0; // Stores number of odd valued elements
    int arr[n];
    for(int i = 0; i < n; i++) {
        cin>>arr[i];
        // Checking for odd valued element
        if(arr[i] % 2 == 1)
            oddCount++;
    }
    if(oddCount > 0) {
        // If we have odd number of odd values, the resulting sum will be odd. Hence no operations are required
        if(oddCount % 2 == 1)
            cout<<"0";
        // Otherwise we have even number of odd numbers, removing one odd number will provide us with odd sum of array
        else
            cout<<"1";
    }
    else {
        int minMoves = 1000;
        for(int i = 0; i < n; i++) {
            int num = 0;
            while(arr[i] % 2 != 1) {
                num++;
                arr[i] /= 2;
            }
            minMoves = min(minMoves, num);
        }
        int cnt = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < minMoves; j++)
                arr[i] /= 2;
            if(arr[i] % 2 == 1)
                cnt++;
        }
        if(cnt % 2 == 1) 
            cout<<minMoves;
        else
            cout<<minMoves + 1;
    }
    return 0;
}