class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seen = []
        
        for i in range(len(nums)):
            if nums[i] in seen:
                return nums[i]
            seen.append(nums[i])
        