class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.seen = set()
        for i in nums:
            if i in self.seen:
                return True
            else:
                self.seen.add(i)
        return False

soln = Solution()
nums = [1,2,3,4]
soln.hasDuplicate(nums)
        