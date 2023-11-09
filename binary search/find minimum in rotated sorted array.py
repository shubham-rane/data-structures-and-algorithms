class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        conditions:
        minimum is at the beginning of the array
        minimum is at the end of the array
        minimum is between the array:
            left is greater than target & right is greater than target
            left is smaller than target and right is greater than target
            left is smaller than target and right is smaller than target - return right
        """
        i = 0 
        j = len(nums)-1
        #if nums is rotated
        while (i < j):
            target = int((i + j)/2)
            print(i,j,target)
            if nums[target] > nums[target-1] and nums[target] > nums[target+1]:
                return nums[target+1]
            if nums[target] < nums[target-1] and nums[target] < nums[target+1]:
                return nums[target]
            else:
                print(target, j)
                if nums[target] < nums[j]:
                    j = target
                else:
                    i = target

        #if nums size is 1
        return nums[i]