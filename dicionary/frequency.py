def frequency_char(s,t):   
    frequency_s ={}
    frequency_t ={}
    for char in s:
        # print(char)
        if char in  frequency_s:
            frequency_s[char]+=1
        else:
            frequency_s[char]=1
    for char in t:
        if char in frequency_t:
            frequency_t[char]+=1
        else:
            frequency_t[char]=1
    if(len(frequency_s) != len(frequency_t)):
        return False
    # print(frequency_s,frequency_t)
    for key,value in frequency_s.items():
       if key not in frequency_t or value != frequency_t[key]:
           return False
    
           
    return True
        

s = "anagram"
t = "nagaram"

frequency_char(s,t)
