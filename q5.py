# PASSED 10/38 TEST CASES
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        t = 0        
        temp = []
        for i in range(-k, 0, 1):
            print(i)
            temp.append(nums[t])
            nums[t] = nums[i]
            t +=1
        print(nums)
        
        for i in range(0, k):
            print(i)
            print(temp,  k+i)
            last = nums[k+i]
            nums[k+i] = temp[i]
            if 2*k+i< len(nums):
                nums[2*k+i] = last

        print(nums)


# OPTIMAL SOLUTION PASSED 37/38
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        nums[:n-k] = reversed(nums[:n-k])
        print(nums)
        nums[n-k:n] = reversed(nums[n-k:n])
        print(nums)
        
        nums.reverse()
        print(nums)
        
s = Solution()
l = [1,2,3,4,5,6,7]
k = 3
s.rotate(l, k)