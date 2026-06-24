class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        r = len(numbers)-1
        l = 0
        while l < r:
            sui = numbers[l] + numbers[r]
            if sui == target:
                return [l+1, r+1]
            elif sui < target:
                l +=1
            else:
                r-=1