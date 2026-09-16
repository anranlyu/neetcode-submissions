class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        output = []
        
        if len(nums) == 3:
            if nums[0] + nums[1] + nums[2] == 0:
                output.append([nums[0], nums[1] , nums[2]])
            return output

        for x in range(len(nums)-2):
            if x > 0 and nums[x] == nums[x - 1]:
                continue
            i , j = x+1, len(nums) -1
            while i<j:
                sum = nums[i] + nums[j] + nums[x]
                if sum == 0:
                    output.append([nums[x], nums[i] , nums[j]])
                    i+=1
                    j-=1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                elif sum > 0:
                    j-=1
                else:
                    i+=1
        return output
        