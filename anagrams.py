class Solution:
    def anagrams(self, data):
        temp={}
        for index,val in enumerate(data):
                   y=''.join(sorted(val))
                   if y not in temp:
                       temp[y]=[index+1]
                   else:
                       temp[y]+=[index+1]
        return list(temp.values())
