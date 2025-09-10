def is_palindrome(s):
    if  len(s) <=1:
        return False
        
    l=0
    r=len(s)-1
    
    while l < r:
        if s[l] != s[r]:
            return False
        l+=1
        r-=1
        
    return True 
    
    
print(is_palindrome('dad'))    