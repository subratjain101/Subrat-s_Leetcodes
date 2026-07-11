class Solution(object):
    def lengthOfLongestSubstring(self, s):
        st=set()
        l=0
        max_len=0

        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[l])
                l+=1
            st.add(s[i])
            max_len=max(max_len,i-l+1)
    
        return max_len 