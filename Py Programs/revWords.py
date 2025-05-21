def rev(s):
    words=s.split()
    for i in range(len(words)):
        words[i]=words[i][::-1]
    return words

s="hello world"
print(rev(s))
