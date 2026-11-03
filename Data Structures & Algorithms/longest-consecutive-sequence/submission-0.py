class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result=0

        if nums is None:
            return result
        numset=set(nums)
        for num in nums:
            res=1
            while (num-1) in nums:
                res+=1
                num-=1
            
            result=max(result,res)
        return result
