// Q2 MINIMAX

// Problem Statement
// You are given an array A, of N positive distinct integers. You can delete several elements of the array (possibly zero). 
// You cannot reorder the elements. Let B denote the array of size K, that we obtain after deleting several elements of array A.
// Your goal is to maximise the sum of consecutive absolute difference of elements of array B, S.
// S=|B1-B2|+|B2-B3|+......+|B(k-1)-B(k)| 
// For several such array B. find the one with the minimum value of K. 
// Print the maximum value of S and its corresponding minimum value of K. You are given T independent test cases.

#include <bits/stdc++.h>
using namespace std;

int main() {
	int t; cin >> t;
	while (t--) {

		int n; cin >> n;
		vector<int> a(n);

		int sum = 0, k = 0;

		for (int i = 0; i < n; i++) {
			cin >> a[i];
			if (i) {
				sum += abs(a[i] - a[i - 1]);
			}
		}

		for (int i = 2; i < n; i++) {

			if (a[i] >= a[i - 1] and a[i - 1] >= a[i - 2]) {
				k++;
			}
            else if (a[i] <= a[i - 1] and a[i - 1] <= a[i - 2]) {
				k++;
			}

		}
		cout << sum << ' ' << n - k << endl;
	}
	return 0;
}