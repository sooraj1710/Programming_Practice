def capt(s):
    word=s.split()
    
    for i in range(len(word)):
        n=len(word[i])
        word[i]=word[i][0].upper() + word[i][1:n-1] + word[i][n-1].upper()
    return word

s = "hello world sooraj"
#word = s.split()

print(capt(s))  


# for i in range(len(word)):
    
    # word[i] = word[i][0].upper() + word[i][1:len(word[i])-1] + word[i][len(word[i])-1].upper() 



# print(word)
