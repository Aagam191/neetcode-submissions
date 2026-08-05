class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        final=[]
        for i in range(len(nums)):
            product=1
            for j in range(len(nums)):
                if i!=j:
                    product *= (nums[j])
            final.append(product)
        return final