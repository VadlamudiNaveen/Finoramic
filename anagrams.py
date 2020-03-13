# algorithm
# anagrams are those which are formed by having same letters but having a different order in every word.
# so to find the like wise anagrams sort every string in the list and map them to a dictionary.
# time complexity O(n)
# space complexity size of dictionary. O(m).. {where m is number of keys}

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
