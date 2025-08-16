def maximum69Number (self, num: int) -> int:
        '''
        num_str = list(str(num))

        for i in range(len(num_str)):
            if num_str[i] == '6':
                num_str[i] = '9'
                break

        
        return int(''.join(num_str))

        '''

        # Using .replace(old, new, count)

        return int(str(num).replace('6','9',1))
    
'''
    Java Code 
    
    class Solution {
    public int maximum69Number (int num) {
        String s = String.valueOf(num);
        String res = s.replaceFirst("6","9");
        return Integer.parseInt(res);
        
    }
}
    
    
'''