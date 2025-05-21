fp=open("temp.txt", "w")
    fp.write("Hello world, I'm Chandraj")
    fp.close
fp.open("temp.txt", 'r')
    content=fp.read()
    print(content)
    fp.close
