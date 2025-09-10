lis=[13,6,32,7,2,66,44,55]



def secon_large(lis):
    fir=sec=float('-inf')
    for i in lis:
        if i > fir:
            fir,sec = i,fir
            
        elif i < fir and i > sec:
            sec=i
    return sec
    
print(secon_large(lis))    
        
        