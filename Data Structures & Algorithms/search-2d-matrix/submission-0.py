class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low , high = 0 , len(matrix) - 1
        while low <= high:
            mid = (low + high) //2
            
            if matrix[mid][-1] < target:
                low = mid + 1
            elif matrix[mid][-1] == target:
                return True
            else:
                if matrix[mid][0] > target:
                    high = mid -1
                else:
                    i , j = 0, len(matrix[mid])-1
                    while i <= j:
                        m = (i+j)//2
                        if matrix[mid][m] == target:
                            return True
                        elif matrix[mid][m] > target:
                            j = m -1
                        else:
                            i = m + 1
                    return False
        return False

        