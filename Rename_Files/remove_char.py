import os, sys
import re
from os.path import isfile
def remove_char_from_list():
 list_names = os.listdir(r".")

 for n in list_names:
   # print(nn)
   match_ = re.match("\s?[0-9]+,?\s?[0-9]+\s?X,\s?[0-9]+\s?[{0-9a-zA-Z}]+?\s?\s?",n)
   # s = re.findall("[0-9]+\s[{0-9a-zA-Z}]+\s",n)
   # s = re.finditer("[0-9]+",n)
   if match_:
    s = str(match_.group(0))
    replace_=n.replace(s," ")
    try:
     os.rename(os.path.join(r".",""+n),(os.path.join(r".\replaced_algorithm","Like_"+replace_)))
    except WindowsError:
     exist = os.path.isfile(".\replaced_algorithm\\" +replace_)
     if exist:
      os.remove(os.path.join(r".\replaced_algorithm",replace_))
      os.rename(os.path.join(r".",""+n),(os.path.join(r".\replaced_algorithm",replace_)))
remove_char_from_list()
