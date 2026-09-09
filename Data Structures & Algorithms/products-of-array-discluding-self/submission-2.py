class Solution:
    def productExceptSelf(self, nums):
        zeros = nums.count(0)
        if zeros > 1:
            return [0] * len(nums)

        product = 1
        for x in nums:
            if x != 0:
                product *= x

        result = []
        for x in nums:
            if zeros == 1:
                result.append(product if x == 0 else 0)
            else:
                result.append(product // x)
        return result







