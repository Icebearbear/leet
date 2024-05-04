# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         k = 0
#         for i in range(1,len(nums)):
#             temp = nums[:i]
#             if nums[i] in temp:
#                 k+=1
#                 nums[i] = None
#         print(nums)
        
#         t = 0
#         for i in range(len(nums)):
#             if t >= len(nums)-k:
#                 return len(nums)-k
#             else:
#                 if nums[i] != None:
#                     nums[t] = nums[i]
#                     t +=1
#         print(len(nums)-k )
#         print(nums)

#         return len(nums)-k 
    
#BETTER SOLUTION
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k = 1
        t = 0
        for i in range(1,len(nums)):
            temp = nums[:k]
            if nums[i] not in temp:
                nums[k] = nums[i]
                k+=1
        return k
    
s= Solution()
l = [1,2]
s.removeDuplicates(l)
