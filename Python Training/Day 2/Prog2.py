name = 'Bluf'
guess = input("So I'am thinking of a person's name, Try to guess it :-")

pos = 0
while guess !=name and pos<len(name):
     print("Nope, that's not it! Hint: letter ", end='')
     print(pos + 1, "is", name[pos]+ ".", end='')
     guess = input("Guess Again: ")
     pos = pos + 1
if pos == len(name) and name!= guess:
    print("Too bad, You couldn't get it. The name was", name+ ".")
else:
    print("\n Great, you got it in", pos+1,"guesses!")
     