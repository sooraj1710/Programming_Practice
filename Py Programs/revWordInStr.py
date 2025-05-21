# def rev(s):
#     n=len(s)
#     t=''
#     for i in range(n-1,-1,-1):
#         t+=s[i]
#     return t

s="hello my name is jaroos"
word=s.split() #word=[hello, my, name, is, jaroos]
print(word)
rev_word=[]
for i in range (0,len(word)):
    rev_word.append(word[i][::-1])
print(rev_word)
for i in range(len(rev_word)):
    print(rev_word[i], end=" ")