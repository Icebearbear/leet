class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                temp = i
                while temp < len(nums)-1:
                    nums[temp] = nums[temp+1]
                    nums[temp+1] = None
                    temp +=1
                k +=1
        return len(nums)-k
