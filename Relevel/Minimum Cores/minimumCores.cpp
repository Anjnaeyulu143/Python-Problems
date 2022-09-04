#include<bits/stdc++.h>
using namespace std;
int main() {
    int n;
    cin >> n;
    vector<pair<int, int>>v;
    for (int i = 0; i < n; i++) {
        int a, b;
        cin >> a >> b;
        v.push_back({a, 1});
        v.push_back({b, -1});
    }
    sort(v.begin(), v.end());
    int ans = 0;
    int cumm = 0;
    for (int i = 0; i < 2 * n; i++) {
        if (v[i].second == -1) {
            cumm--;
        }
        else {
            cumm++;
        }
        ans = max(ans, cumm);
    }
    cout << ans << "\n";
    return 0;
}