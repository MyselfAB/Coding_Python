class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        a=abs(nums[0])
        n=len(nums)
        print(n)
        c=0
        for i in range(0,n):
    
            b=abs(nums[i])
    
            if b<a:
                a=b
                c=i
       
            elif b==a:
                if nums[i]>=nums[c]:
                    c=i
        return nums[c]        
        
