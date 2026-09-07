class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        result = False
        for i in range(len(nums)):
            if map.get(nums[i]) == None:
                map[nums[i]] =1
            else:
                map[nums[i]] +=1
                if map.get(nums[i]) > 1:
                    result = True
            
        return result
                
            


        