class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        num1=int(num1)
        num2=int(num2)
        res=num1*num2
        return str(res)
s1=Solution()
print(s1.multiply("2","3"))