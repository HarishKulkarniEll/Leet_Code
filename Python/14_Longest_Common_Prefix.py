# def longestCommonPrefix(strs):
#     if len(strs) >= 1 and len(strs) <= 200:
#         short_string = min(strs, key=len)
#         flag = True
#         return_string = ""
#         for string in strs:
#             if flag == True:
#                 return_string = ""
#                 if string == short_string: 
#                     flag = True
#                     return_string += string
#                 else:
#                     for i in range(len(string)):
#                         if flag == True:
#                             if i < len(short_string):
#                                 print(string, string[i], '==', short_string[i])
#                                 if string[i] == short_string[i]:
#                                     return_string += string[i]
#                                     flag = True 
#                                 else:
#                                     flag = False
#                             else:
#                                 flag = False
#         return return_string
            
def longestCommonPrefix(strs):
    if not strs:
        return ""
    strs.sort()
    first=strs[0]
    last=strs[-1]
    i=0
    while i<len(first)  and first[i]==last[i]:
        i+=1
    return first[:i]
# returnString = longestCommonPrefix(["a"])
# returnString = longestCommonPrefix(["flower","flow","flight"])
# returnString = longestCommonPrefix(["dog","racecar","car"])
# returnString = longestCommonPrefix(["cir","car"])
returnString = longestCommonPrefix(["abca","aba","aaab"])
print("Output is",returnString)