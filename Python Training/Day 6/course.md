# Exception Handeling

An exception is an event that occurs during the exexution of a program that disrupts the noraml flow of the program

try:
Operations are performed here
except Exceptions1:
....
else:
   if no exception execute the prog

# strip() function used to print the lines.... 
code example:


try: 
    fh = open('xlines.txt')
    for line in fh:
      print(line.strip())
except IOError as e:
    print('file does not exist.....!',e)

* Google Python Built in exception eg.  https://docs.python.org/3/library/exceptions.html

# finally statement

-> this clause is executed no matter what, and is generally used to release external resources
-> it is intended to define cleanuo actions that must be executed under all circumstances.

# Python iterators

* iterators are are objectsthat can be iterated upon

=> __iter__
=> __next__
=> reversed()

# opening and closing of files

-> files open => open(FileName[access_mode])

# the close methods
-> fileObject.close()

Reading and writing files:
write:
fileObj.write(string)
def main():
   infile = open('lines.txt','r')
   outfile = open('lines.txt','w')
   for line in infile:
      print(line,file=outfile,end='')
   print('done...')
main()


#####################################################################################################################
                                         PYTHON GUI
#####################################################################################################################

Ptyhon module 'Tkinter'
