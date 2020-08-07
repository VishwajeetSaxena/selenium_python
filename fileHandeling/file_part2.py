#Read file
samplefile = open('file1.txt', 'r')
print(samplefile.read())
samplefile.close()

print('*'*20)
#Read file line by line
samplefile2 = open('file1.txt', 'r')
while True:
    line = samplefile2.readline()
    if line:
        print(line)
    else:
        break


samplefile2.close()
