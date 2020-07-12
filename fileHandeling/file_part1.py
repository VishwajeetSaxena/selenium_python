
samplelist = [1, 2, 4]
samplefile = open('file1.txt', 'w')

for item in samplelist:
    samplefile.write(str(item) + '\n')

samplefile.close()
