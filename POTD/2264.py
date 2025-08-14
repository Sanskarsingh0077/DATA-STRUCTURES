def largestGoodInteger(self, num: str) -> str:
        maxstr = ' '
        for i in range(2,len(num)):
            if num[i] == num[i-1] and num[i] == num[i-2]:
                maxstr = max(maxstr, num[i])
                

        if maxstr == ' ':
            return ""

        return maxstr * 3
        
'''
Java Code:

class Solution {
    public String largestGoodInteger(String num) {
        char maxstr = 0;

        for(int i = 2; i < num.length(); i++){
            if(num.charAt(i) == num.charAt(i-1) && num.charAt(i)==num.charAt(i-2)){
                maxstr = (char) Math.max(maxstr, num.charAt(i));
            }

        }
        if(maxstr == 0) return "";

        return String.valueOf(maxstr).repeat(3);

    }
}

'''