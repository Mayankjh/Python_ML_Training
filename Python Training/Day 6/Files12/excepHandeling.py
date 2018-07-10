#to implement try block
# try: 
#     fh = open('xlines.txt')
#     for line in fh:
#       print(line.strip())
# except IOError as e:
#     print('file does not exist.....!',e)

def main():
    try:
        for line in readfile('lines.txt'):
            print(line.strip())
    except IOError as e:
        print('cannot read file',e)
    except ValueError as e:
        print("bad file name",e)

def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError("File name must be with '.txt' extension")
main()

