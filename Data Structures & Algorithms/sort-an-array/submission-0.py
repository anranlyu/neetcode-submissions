class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            return merge(left,right)
        
        def merge(a,b):
            res = []
            i = j = 0
            while i < len(a) and j < len(b):
                if a[i] <= b[j]:
                    res.append(a[i])
                    i+=1
                else:
                    res.append(b[j])
                    j+=1
            res.extend(a[i:])
            res.extend(b[j:])
            return res
        return merge_sort(nums)