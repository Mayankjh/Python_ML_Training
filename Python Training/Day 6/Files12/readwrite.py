def main():
   infile = open('lines.txt','r')
   outfile = open('new.txt','w')
   for line in infile:
      print(line,file=outfile,end='')
   print('done...')
   outfile.close()
main()

file = open('new.txt', 'r') 
print(file.read()) 