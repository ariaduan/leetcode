class Solution:
    def reverse(self, x: int) -> int:
        flag = 1
        if x <0:
            flag = -1
            x *=-1
        answer = str(x)[::-1]
        for i in range(len(answer)):
            if answer[i]!="0":
                answer = answer[i:]
                break
        answer = flag*int(answer)
        return answer if answer >= -2**31 and answer <= 2**31-1 else 0
