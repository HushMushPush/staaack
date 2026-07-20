class Solution:
    def evalRPN(self, tokens): # List[str] -> int
        st = []
        for i in tokens:
            if i == '+':
                st.append(st.pop(-2) + st.pop())
                
            elif i == '-':
                st.append(st.pop(-2) - st.pop())

            elif i == '*':
                st.append(st.pop(-2) * st.pop())
            
            elif i == '/':
                st.append(int(st.pop(-2) / st.pop()))

            else:
                st.append(int(i))

        return int(st[0])
    

a = ["1","2","+","3","*","4","-"] # input().split()
abs = Solution()

print(abs.evalRPN(a))