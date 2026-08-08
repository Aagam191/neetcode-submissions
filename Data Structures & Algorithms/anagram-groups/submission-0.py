
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sorted_list={}
        final_arr=[]
        for i in strs :
            sorted_i = sorted(i)
            str_i="".join(sorted_i)
            if str_i not in sorted_list:
                sorted_list[str_i]=[i]
            else:
                sorted_list[str_i].append(i) 
        return list(sorted_list.values())