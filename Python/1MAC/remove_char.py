import os, sys
import re
from os.path import isfile
def remove_char_from_list():
 list_names = os.listdir(r"D:\Summary and Details\Python\MAC\prank")
 for n in list_names:
   s = re.findall("[0-9]+\s[{0-9a-zA-Z}]+",n)
   if n != "" :
    replace_ = n.replace(s,"")
    os.rename(os.path.join(".",str(n)),(os.path.join(".\replaced_algorithm",replace_)))
        print "success rename " + n + " to " + x
      else:
        os.rename(os.path.join(".", str(n)), (os.path.join(".\replaced_algorithm",replace_)))
        print "fail"
remove_char_from_list()

