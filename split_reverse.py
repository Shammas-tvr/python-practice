def split_reverser(s):
    return " ".join(map(lambda x : x[::-1],s.split()))
    
print(split_reverser("am going to vadakara "))   



def slit_reverse_join(s):
    return " ".join(x[::-1] for x in s.split())

print(slit_reverse_join("yestarday am eat the biriyani ")) 