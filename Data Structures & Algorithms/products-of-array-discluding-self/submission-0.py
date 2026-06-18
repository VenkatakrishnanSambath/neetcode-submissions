class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_num = 1
        r_num = 1
        l_arr = [0] * len(nums)
        r_arr = [0] * len(nums)
        res = []
        for i in range(len(nums)):
            j = -i-1
            l_arr[i] = l_num
            r_arr[j] = r_num
            l_num *= nums[i]
            r_num *= nums[j]
        for k in range(len(nums)):
            res.append(l_arr[k] * r_arr[k])
        return res

soln = Solution()
nums = [1,2,4,6]
soln.productExceptSelf(nums)