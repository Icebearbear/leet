# FAST BUT SOME LOGIC IS WRONG. PASSED 157/172
# class Solution(object):
#     def jump(self, nums):
#         if len(nums) <= 1:
#             return True
#         if nums[0] == 0 and len(nums) > 1:
#             print(f"edge case {nums}")

#             return False

#         else:
#             print(f"recurse case {nums}")
#             print(nums[0])
#             curr = nums[0]
#             nums = nums[curr:]
#             print(f"next nums {nums}")
#             return self.jump(nums)
        
#     def canJump(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         if len(nums) <= 1 :
#             return True
#         return self.jump(nums)

# CAN SOLVE THE EDGE CASES BUT SLOW. PASSED 147/172
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reachable = 0
        for i in range(len(nums)):
            print("max reachable read",max_reachable)

            if i > max_reachable:
                print("f")
                return False
            max_reachable = max(max_reachable, i + nums[i])
            print("max reachable set",max_reachable)
        return True
    
s =Solution()
nums = [2,1,0,0]
r = s.canJump(nums)
print(r)