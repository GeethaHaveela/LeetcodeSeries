class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        max_reach = 0
        for i,jump in enumerate(nums):
            if i>max_reach:  
                return False
            max_reach=max(max_reach,i+jump) 
            if max_reach>=len(nums)-1:  
                return True
        return False
s1=Solution()
print(s1.canJump([2,3,1,1,4]))