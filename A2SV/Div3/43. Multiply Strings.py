class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        total=0

        for i, n1 in enumerate(reversed(num1)):
            n1=ord(n1)-ord('0')
            for j,n2 in enumerate(reversed(num2)):
                n2=ord(n2)-ord('0')
                total+=(n1*n2*10**(i+j))
        return str(total)
