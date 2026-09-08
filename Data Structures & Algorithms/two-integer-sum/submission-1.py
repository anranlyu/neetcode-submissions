class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a , b = 0 , 1
        while a < len(nums) - 1:
            while b < len(nums):
                if nums[a] + nums[b] == target:
                    return [a,b]
                b +=1
            a+=1
            b = a + 1




        