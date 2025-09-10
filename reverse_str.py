def reversal(s):
    if len(s)<=1:
        return s 
    res=""    
    for i in range(len(s)):
        if s[i] =="a":
            res+="x"
        else:
            res+=s[i]
    return res
    
print(reversal("shammas"))  