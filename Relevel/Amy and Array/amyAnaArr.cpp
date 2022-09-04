// 100%


#include<bits/stdc++.h>
using namespace std;
#define int long long
signed main() {
    int t;
    cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int arr[n];
        for (int i = 0; i < n; i++) {
            cin >> arr[i];
        }
        // int mi[n + 1];
        // mi[n] = INT_MAX;
        // for (int i = n - 1; i >= 0; i--) {
        //     mi[i] = min(mi[i + 1], arr[i]);
        // }
        int ans = 0;
        int mi = INT_MAX;
        for (int i = n - 1; i >= 0; i--) {
            if (arr[i] >= mi) {
                ans += arr[i] - mi + 1;
                arr[i] = mi - 1;
            }
            if (mi == 0) {
                ans--;
                arr[i] = 0;
            }
            mi = min(mi, arr[i]);
        }
        cout << ans << "\n";
    }
}