class Solution:
    def myAtoi(self, s: str) -> int:
        if s == "": return 0
        sta = 0
        flag = 1
        answer = ["0"]
        mx = 2**31-1
        mn = -2**31
        while sta < len(s) and s[sta] ==" ":
            sta += 1
        if sta == len(s): return 0
        if s[sta] =="+":
            sta +=1
        elif s[sta] =='-':
            sta+=1
            flag = -1
        while sta < len(s) and s[sta].isnumeric():
            answer.append(s[sta])
            sta+=1
        answer = flag*int("".join(answer))
        answer = mx if answer > mx else answer
        answer = mn if answer < mn else answer
        return answer
        
        # ord(s[sta]) >= ord('0') and ord(s[sta]) <= ord('9'):
        #     num = ord(s[sta]) - ord('0')
        #     answer = answer*10+num
        #     sta += 1
        #     if flag*answer > mx: return mx
        #     if flag*answer <mn: return mn
        # return flag*answer
