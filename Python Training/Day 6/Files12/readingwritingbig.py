# def main():
#     buffersize = 50000 #assumed buffer size
#     infile = open('bigfile.txt','r')
#     outfile = open('new.txt','w')
#     buffer = infile.read(buffersize)
#     while len(buffer):
#         outfile.write(buffer)
#         print('.',end = '')
#         buffer = infile.read(buffersize)
#         print()
#     print('done...')
# main()

# list of text file with file name of 5 people
# make a new file with people not in the list

def main():
    buffersize = 50000 #assumed buffer size
    infile = open('olives.jpg','rb')
    outfile = open('new.txt','wb')
    buffer = infile.read(buffersize)
    while len(buffer):
        outfile.write(buffer)
        print('.',end = '')
        buffer = infile.read(buffersize)
        print()
    print('done...')
if __name__ =="__main__":
    main()