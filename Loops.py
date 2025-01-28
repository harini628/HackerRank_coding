class Solution(object):
    def sq(self , n):
        
        for i in range(n):
            x = i*i
            print(x)
        
n = int(input())
obj = Solution()
obj.sq(n)
