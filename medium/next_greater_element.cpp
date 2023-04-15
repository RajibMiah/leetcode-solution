#include<bits/stdc++.h>
using namespace std;
#define PI 3.14159265358979323846264338327951
const int INF = 1e9;
const int MAX_N = 1e5 + 5;
const int MOD = 1e9 + 7;
const double EPS = 1e-9;

bool cmp(pair <int , int> a , pair < int ,int> b){
    if(a.first != b.second) return a.first < b.second;
    return a.first > b.second;
}
// Time limit	Operations (approximate)
// 1 second     	10^7
// 10 seconds	    10^8
// 1 minute	        10^9
// 1 hour	        10^11

vector <int> NGE(vector<int> v){
    vector<int> ans(v.size());
    stack<int> st;
    for(int i = 0 ; i < v.size(); i++){
            while(!st.empty() and  v[st.top()] < v[i] ){
                ans[st.top()] = i;
                st.pop();
            }
            st.push(i);
    }
    while(!st.empty()){
        ans[st.top()] = -1;
        st.pop();
    }
    
    return ans;
}
int main(){
    int ttt ; cin >> ttt;
    vector <int> v;
    for(int i = 0; i< ttt ; i++){
            int n;
            cin >> n;
            v.push_back(n);;
    }
    auto result = NGE(v);
    for(int i= 0 ; i< result.size() ; i++){
        cout << v[i] << " " <<(result[i] == - 1 ? -1 : v[result[i]]) << endl; 
    }
}