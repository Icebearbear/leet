class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if len(citations) <= 1:
            return min(1, citations[0])
        
        n = len(citations)
        
        for i in range(1,n):
            temp = i
            while temp > 0 and citations[temp] < citations[temp-1]:
                t = citations[temp]
                citations[temp] = citations[temp-1]
                citations[temp-1] = t
                temp -=1
        print(citations)
        max_h = 0
        for i in range(len(citations)-1,0, -1):
            curr = citations[i]
            counter_h = 0
            print(citations[:i]) 
            for num in citations[:i]:
                if num >= curr:
                    counter_h +=1

            print(len(citations) - i + 1)
            print(counter_h , len(citations) - i + 1)
            counter_h = counter_h + len(citations) - i + 1
            print(f'counter_h {counter_h} and curr_h  {curr}')

            if counter_h >= curr and curr > max_h:
                max_h = curr
        return max_h    

s= Solution()
l = [3,0,6,1,5]
l= [1,3,1]
l = [1,2]
r = s.hIndex(l)
print(r)