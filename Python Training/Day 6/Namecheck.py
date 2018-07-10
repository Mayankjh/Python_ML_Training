def main():
    try:
        name = ['Mayank','Karan','Kritarth','Geetansh','Piyush']
#         for line in readfile('lines.txt'):
#             print(line.strip())
        if 'Mayank' in open('names.txt').read():
           print()
        else:
            print('False')
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