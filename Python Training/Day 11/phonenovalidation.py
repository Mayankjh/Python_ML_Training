import re

phoneno ='441-122-1234'
# 
# val = re.findall("[1-9][1-9][1-9][-][1-9][1-9][1-9][-][1-9][1-9][1-9][1-9]",phoneno)
# print(phoneno)
# print(val)

# a= (re.search("\w{1}-\w{2}-\w{6}",phoneno))
# 
# if (re.search("\w{1}-\w{2}-\w{6}$",phoneno)):
#     print("Valid no.")
# else:
#     print("not valid")
#  

# Full Name validation   
# name="Mayank Jha"
# 
# n = re.findall("\w*\s\w",name)
# 
# if re.findall("\w*\s\w",name):
#     print("Valid no.")
# else:
#     print("not valid")

mail=["mayankjha7722@gmail.com","kv.com","123 @.com","Reyshma @ com","india@gmail.com"]

for i in mail:
    if re.findall("[\w.@%+-]{1,20}@[\w.-]{1,6}.[a-zA-Z]{2,3}$",i):
         print("Valid mail",i)
    else:
         print("not valid",i)
        
