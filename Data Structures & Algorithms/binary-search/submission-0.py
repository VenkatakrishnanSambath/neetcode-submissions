class Solution:
    def search(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] == target:
                return i
        if target not in nums:
            return -1