class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)
        n2=len(word2)
        if n1<n2:
            n=n1
        else:
            n=n2
        print(n)
        a=""

        for i in range(0,n):
            a=a+word1[i]+word2[i]
            
            c=i+1
        a=a+word1[c:]+word2[c:] 
        return a


# Best method 

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = ""
        i = 0
        while i < len(word1) and i < len(word2):
            merged += word1[i] + word2[i]
            i += 1
        merged += word1[i:] + word2[i:]
        return merged

# # Example usage:
# solution = Solution()
# word1 = "abc"
# word2 = "pqr"
# print(solution.mergeAlternately(word1, word2))  # Output: "apbqcr"

# word1 = "ab"
# word2 = "pqrs"
# print(solution.mergeAlternately(word1, word2))  # Output: "apbqrs"

# word1 = "abcd"
# word2 = "pq"
# print(solution.mergeAlternately(word1, word2))  # Output: "apbqcd"
