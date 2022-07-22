def isValid(s):
        stack = []
        CTO = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in CTO:
                if stack and stack[-1] == CTO[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        if stack:
            return False
        return True
"""
def isValid(self, s: str) -> bool:
        stack = []
        CTO = { ')':'(', '}':'{', ']':'[' }
        
        for ch in s:
            if ch in CTO.values():
                stack.append(ch)
                
            elif stack and stack[-1] ==CTO[ch]:
                    stack.pop()
            else:
                return False    

        if stack:
            return False
        return True
"""

if __name__ == "__main__":
    t = int(input())
    while t:
        s = input()
        if isValid(s) == True:
            print("YES")
        else:
            print('NO')
        t -= 1
