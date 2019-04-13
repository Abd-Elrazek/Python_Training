#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Abdelrazek
#
# Created:     12/04/2019
# Copyright:   (c) Abdelrazek 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def tri_recursion(k):

    if (k > 0):
        result = k + tri_recursion(k - 1)
        print (result)
    else:
      result = 0
    return result
print("\n\nRecurion Example Results")
tri_recursion(4)