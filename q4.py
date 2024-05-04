class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import math
        indicator = math.ceil(len(nums)/2)
        dic = {}
        max_d = nums[0]
        for i in range(len(nums)):
            if nums[i] not in dic.keys():
                dic[nums[i]] = 0
            dic[nums[i]] +=1
            if dic[max_d] < dic[nums[i]] > indicator:
                max_d = nums[i]
        return max_d 
    
s = Solution()
l = [6,5,5]
s.majorityElement(l)