def main():
    try:
        name = ['Mayank','Karan','Kritarth','Geetansh','Piyush']
#         for line in readfile('lines.txt'):
#             print(line.strip())
        for names in readfile('names.txt'):
           outfile = open('new.txt','w')
           data = names.strip()
           if data not in name:
               outfile.write(data +"\n")
               print("done...")
           else:
              pass

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

file = open('new.txt', 'r') 
print(file.read())