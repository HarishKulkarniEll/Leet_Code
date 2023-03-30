s= "aab"
p = "c*a*b"
def isMatch(s: str, p: str) -> bool:
    if s == p:
        return True
    else:
        # if '.' not in p and '*' not in p:
        #     return False
        # else:
        #     for i in s:
        #         for j in p:
        #             if i != j and j != '.' and j != '*':
        #                 return False
        #             else:
        #                 return True
        if '.' in p and len(s)==len(p):
            print(p)

ans = isMatch(s, p)
print(ans)