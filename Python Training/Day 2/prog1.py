# #conditions max value range is 45 if> 43 print large
#  ''' if >35 and <=43 medium
#  >25 and <=35 small
#  <= 25 not eligible
#  the value is small/medium /large '''
 
import random as r
b=r.randint(0,45)
if (b>43):
     print('The value gien is Large', b)
elif (b>35 and b<=43):
    print('The given value is medium', b)
elif (b>25 and b<=25):
    print('The given value is small', b)
else:
    print('The Given value is not Eligible',b)
