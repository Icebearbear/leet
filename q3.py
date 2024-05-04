# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         prev = nums[0]
#         dup_count = 1
#         k = 1
#         for i in range(1,len(nums)):
#             print( nums[i] , nums[i-1])

#             if nums[i] == nums[i-1]:
#                 dup_count +=1
#                 if(dup_count <= 2):
#                     nums[k] = nums[i]
#                     k +=1
#                     dup_count +=1

#                 print("i", nums)
#             else:
#                 dup_count = 1
#                 nums[k] = nums[i]
#                 k +=1
#                 print("j", nums)

#             print(k)

#         print(nums)
#         print(k)
#         return k
    
#BETTER SOLUTION
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 1
        for i in range(1,len(nums)):
            print(i)
            print(nums[i], nums[k-2])

            if k == 1 or nums[i] != nums[k-2]:
                print("add" , nums[i])
                nums[k] = nums[i]
                k +=1
            print("k",k)
        print(nums)
        print(k)
        return k
    
s= Solution()
l = [1,1,1,2,2,3]
s.removeDuplicates(l)

