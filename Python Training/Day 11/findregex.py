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

# 
# Str = "Sat, hat, mat,pat"
# # 
# # allstr = re.findall("[shmp]at",Str)
# # for i in allstr:
# #     print(i)
# 
# allstr = re.findall("[h-m]at",Str)
# for i in allstr:
#      print(i)


# Food= 'hat mat rat pat'
# regex = re.compile("[r]at")
# Food = regex.sub("food",Food)
# print(Food)

# randStr = '12345'
# print("Matches:",len(re.findall("\d{5}",randStr)))

# str="""
# hello my name 
# is khan 
# and 
# i am not 
# a terrorist!
# """
# print(str)
# regex = re.compile("\n")
# Str = regex.sub("",str)
# print(Str)


str2='here is \\bpit'
print(str2)
print(re.search(r'\\bpit',str2))