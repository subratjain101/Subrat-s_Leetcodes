class Solution(object):
    def sortVowels(self, s):
        s=list(s)
        Vset=set("AEIOUaeiou")
        vowels=[v for v in s if v in Vset]
        vowels.sort()
        j=0
        for i in range(len(s)):
            if s[i] in Vset:
                s[i]=vowels[j]
                j+=1
        return ''.join(s)