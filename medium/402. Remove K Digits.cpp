class Solution {
public:
    string removeKdigits(string num, int k) {
        string s;
        for(int i=0; i <= num.size() ; i++){
            while(!s.empty() and s.back() > num[i] and k !=0){
                s.pop_back();
                k--;
            }
            if(i != num.size()){
                s.push_back(num[i]);
            }
           
            if(s.size() == 1 and num[i] == '0'){
                s.pop_back();
            }
            
        }
        
        if(s.length() == 0 || (num.length() == 1 and k == 1))
            return "0";
        return s;
    }
};
