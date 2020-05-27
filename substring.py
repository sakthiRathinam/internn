totalCharacters=256  
def max_distinct_char(strr, n): 
    count=[0]*totalCharacters  
    for i in range(n): 
        count[ord(strr[i])]+=1
    max_distinct = 0
    for i in range(totalCharacters): 
        if (count[i]!=0): 
            max_distinct+=1          
    return max_distinct 
def smallesteSubstr_maxDistictChar(strr): 
    n=len(strr)      
    max_distinct=max_distinct_char(strr, n) 
    minl=n    
    for i in range(n): 
        for j in range(n): 
            subs=strr[i:j] 
            subs_lenght=len(subs) 
            sub_distinct_char=max_distinct_char(subs,subs_lenght)   
            if (subs_lenght < minl and 
                max_distinct==sub_distinct_char): 
                minl=subs_lenght 
    return minl 
if __name__ == "__main__":       
    strr=input("enter the string")
    l=smallesteSubstr_maxDistictChar(strr); 
    print( "smallest substring", 
           "consisting of maximum distinct", 
           "characters :", l)  
