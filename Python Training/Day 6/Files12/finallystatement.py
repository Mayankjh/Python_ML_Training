# finally statement executed
try:
    fh = open('lines.txt')
    a= 1/0;
except IOError as e:
    print("file does not exist.......!!",e)
finally:
    print('Finally block')
    fh.close()