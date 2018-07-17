## Day 11 

## RegEx (regular Expression)

* syntax

    import re
	NameAge = "Janice is 22 and Theon is 33 Gabriel is 44 and Joey is 21"
	ages = re.findall(r'\d{1,3}',NameAge)
	names = re.findall(r'[A-Z][a-z]*',NameAge)
	ageDict={}
	x=0
	for eachname in names:
	    ageDict[eachname] = ages[x]
	    x +=1
	print(ageDict)
## FindAll() key word

 import re

# allinform = re.findall("inform","we need to inform him with the latest information")
# 
# for i in allinform:
#     print(i)

# str ="we need to inform him the latest information"
# 
# for i in re.finditer("inform",str):
#     locTuple = i.span()
#     print(locTuple)


Str = "Sat, hat, mat,pat"
# 
# allstr = re.findall("[shmp]at",Str)
# for i in allstr:
#     print(i)


## Removing Blank spaces
str="""
hello my name 
is khan 
and 
i am not 
a terrorist!
"""
print(str)
regex = re.compile("\n")
Str = regex.sub("",str)
print(Str)
allstr = re.findall("[h-m]at",Str)
for i in allstr:
     print(i)

## Replacing Text through Regex

Food= 'hat mat rat pat'
regex = re.compile("[r]at")
Food = regex.sub("food",Food)
print(Food)

## Matching a single string

randStr = '12345'
print("Matches:",len(re.findall("\d{5}",randStr)))
