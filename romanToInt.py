class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000, "O":0 }
        s=s+"O"
        n=len(s)  
        a=0     
        i=0
        while i<n:
            if d[s[i]]==0 or d[s[i+1]]==0  :
                a= a+d[s[i]]
                i+=1
            elif i<n-1 and d[s[i]]<d[s[i+1]]:
                a+=d[s[i+1]]-d[s[i]]
                i+=1
                
            else:
                a= a+d[s[i]]
            i+=1
        return a 


Best  Method

class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'V':5, 'X':10, 'L':50, 'C':100, 'D': 500, 'M':1000}
        summ = 0
        n = len(s)
        i = 0
        
        while i < n:
            if i < n - 1 and d[s[i]] < d[s[i+1]]:
                summ += d[s[i+1]] - d[s[i]]
                i += 2
            else:
                summ += d[s[i]]
                i += 1
        
        return summ
        # Time: O(n)
        # Space: O(1)
