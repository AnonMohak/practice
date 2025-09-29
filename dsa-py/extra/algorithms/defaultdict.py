### lets say we wanna group anagrams together
## and return a list back 
##Input: strs = ["eat","tea","tan","ate","nat","bat"]
##Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnn(strs):
    sol=defaultdict(list)   #makes a dict with list as values and if element not exists default value=0

    for s in strs:
        count=[0]*26   #make an array of 26 0's 
        for c in s:
            count[ord(c)-ord("a")]+=1   #ord("a") converts a-> ASCII value, soo when c=0, a-a=0 -> count[0]
        sol[tuple(count)].append(s)

    return list(sol.values())


ga=groupAnn(strs)

print(ga)
