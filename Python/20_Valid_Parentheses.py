# class Solution:
def isValid(s):
    # if "(" in s:
    #     s.replace("(", "")
    #     if ")" in s:
    #         s.replace(")", "")
    #         flag = True
    # elif "{" in s:
    #     s.replace("{", "")
    #     if "}" in s:
    #         s.replace("}", "")
    #         flag = True
    # elif "[" in s:
    #     s.replace("[", "")
    #     if "]" in s:
    #         s.replace("]", "")
    #         flag = True
    # else:
    #     flag = False
    
    # if flag == True and len(s) == 0:
    #     print(s)
        count=[]
        check={')':'(',']':'[','}':'{'}
        for i in s:
            if i in check:
                if count and count[-1]==check[i]:
                    count.pop()
                else:
                    return False
            else:
                count.append(i) 
        return True if not count else False


# s = """()[]{}"""
s = """([)]"""
ans = isValid(s)
print(ans)
