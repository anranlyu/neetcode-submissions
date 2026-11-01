class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        def mergeSort(arr):
            if len(arr) <=1:
                return arr
            mid = len(arr)//2
            left = mergeSort(arr[:mid])
            right = mergeSort(arr[mid:])
            return mergeHelper(left,right)
        
        def mergeHelper(a,b):
            i ,j = 0,0
            res = []
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
        merged = mergeSort((nums1[:m] + nums2))
        nums1[:] = merged

