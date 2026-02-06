fp = open("text.txt")
print(fp.read()) #reads the content of the file
fp.close()

print("or in another way:")
with open("text.txt") as fp:
    print(fp.read())

#read line by line and can also process it:
with open("text.txt") as fp:
    for line in fp:
        print(line.capitalize(), end = "")
        #print(line.capitalize().rstrip())
