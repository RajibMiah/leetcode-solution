#include<bits/stdc++.h>
using namespace std;
#define PI 3.14159265358979323846264338327951
const int INF = 1e9;
const int MAX_N = 1e5 + 5;
const int MOD = 1e9 + 7; 
const double EPS = 1e-9;

// Time limit	Operations (approximate)
// 1 second     	10^7
// 10 seconds	    10^8
// 1 minute	        10^9
// 1 hour	        10^11


unordered_map <char , int > symbols = {{'[' ,-1} , {'(' , -2} ,{'{' , -3} , {']' , 1} , {')' , 2} ,{'}' , 3}};

string isBalanced(string s){
    stack <char > st;
    for( char bracket : s){
        if(symbols[bracket] < 0 ){
            st.push(bracket);
        }else{
            if(st.empty()){
                return "NO";
            }
            char top = st.top();
            st.pop();
            if(symbols[top] + symbols[bracket] != 0){
                return "NO";
            }


 
        }

    }
    return "YES";
}

int main(){
    int n;
    cin >> n;
    while(n--){
        string s;
        cin >> s;
        cout << isBalanced(s) << endl;
    }

}