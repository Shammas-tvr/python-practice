def longest_wrd(word):
    w=word.split()
    longest=""
    for i in word:
        if len(i) < len(longest):
            longest=i
    return longest
    
    
print(longest_wrd(" remove whitespace from start and end "))    