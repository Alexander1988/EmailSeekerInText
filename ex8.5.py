fname = input("Enter file name: ")#prompt the filename
#if len(fname) < 1 : fname = "mbox-short.txt"
fh = open(fname)
count = 0 #counter for lines coutining added
for line in fh:
    line = line.rstrip()#delete all spaces at the right end of the line
    if not line.startswith('From '): continue
    #if there is not FRom in this line go to begining
    words=line.split()#else split line onto the words
    count=count+1#increment counter
    print(words[1])#print emails
#finally we re printing out the number of all liines start with FROM word
print("There were", count, "lines in the file with From as the first word")
