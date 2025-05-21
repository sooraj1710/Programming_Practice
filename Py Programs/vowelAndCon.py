s="Hello world "
s=s.lower()
print(s)
vowel=0
con=0
for i in range(len(s)):
    if(s[i]=='a' or s[i]=='e' or s[i]=='i' or s[i]=='o' or s[i]=='u'):
        vowel=vowel+1
    elif(s[i]!=" "):
        con=con+1

print(vowel, con)