f = open('C:\\Users\\LENOVO\\Desktop\\foot.txt')
line = f.readline()
while line:
    print (line,end='')
    line = f.readline()
f.close()
