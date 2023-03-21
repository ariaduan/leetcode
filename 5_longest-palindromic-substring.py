class Solution:
    def longestPalindrome(self, s: str) -> str:
        
        def getmax(s, left, right):
            while left-1 >= 0 and right+1 <len(s) and s[left-1]==s[right+1]:
                left -=1
                right +=1
            return (left,right)

        answer = (0,0)
        for mid in range(len(s)):
            comp1 = getmax(s,mid,mid)
            answer = answer if answer[1]-answer[0] >= comp1[1]-comp1[0] else comp1
            if mid+1 < len(s) and s[mid] == s[mid+1]:
                comp2 = getmax(s,mid,mid+1)
                answer = answer if answer[1]-answer[0] >= comp2[1]-comp2[0] else comp2
        return s[answer[0]:answer[1]+1]
