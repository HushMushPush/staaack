class Solution:
    def isValid(self, str_): # str -> bool
        stack = []

        for elem in str_:
            print(elem, stack)
            if len(stack) == 0 and (elem == ')' or elem == ']' or elem == '}'):
                return False
            
            if elem == '(' or elem == '[' or elem == '{':
                stack.append(elem)
            elif stack[-1] == '(' and elem == ')':
                stack.pop()
            elif stack[-1] == '[' and elem == ']':
                stack.pop()
            elif stack[-1] == '{' and elem == '}':
                stack.pop()
            else:
                return False

        if stack:
            return False
        else:
            return True


s = '(])'
abs = Solution()

print(abs.isValid(s))