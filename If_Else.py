class Solution(object):
  def oddeven(self,n):
    if(n%2 == 0):
        if ( n > 20 ):
            print("Not Weird")
        elif(1 < n < 6):
            print("Not Weird")
        else:
            print("Weird")
    
    else:
       print("Weird")
       
n = int(input())
obj = Solution()
obj.oddeven(n)

