#--------this is code for remove string from string-------
def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    length = len(sub)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return part_before + part_after

# 
# Don't change these test cases!
print remove('audacity', 'a')
print remove('pythonic', 'ic')
print remove('substring institution', 'string in')
print remove('ding', 'do')  # "do" isn't in "ding"; should print "ding"
print remove('doomy', 'dooming')  # and this should print "doomy"


#----------------------------------
# this code for extract median number 

def bigger(a,b):
    if a > b:
        return a
    else:
        return b

def biggest(a,b,c):
    return bigger(a,bigger(b,c))

def median(a, b, c):
    big = biggest(a, b, c);
    if ( big == a):
        return bigger(c, b);
    if ( big == b):
        return bigger(a, c);
    if (big == c):
        return bigger(a, b);
 # --------------------------------------
   # this code  for putting word replace another word in python 
    def process_madlib(madlib):
	 processed = ""
	idnex = 0                          
	box_length = 4
	while index < len(madlib):
	 frame = madlib[index:index+box_length]
	 to_add = word_transformer(frame)
	 processed += to_add
	if len(to_add) == 1 :
	 index += 1
	 else:
	 index += 4
	return processed 
	'''
	 this code  must focus and focus at it
	'''
 #----------------------------------------
# Let's put it all together. Write code for the function process_madlib, which takes in 
# a string "madlib" and returns the string "processed", where each instance of
# "NOUN" is replaced with a random noun and each instance of "VERB" is 
# replaced with a random verb. You're free to change what the random functions
# return as verbs or nouns for your own fun, but for submissions keep the code the way it is!

# this code such as previous code and same code for performance
from random import randint

def random_verb():
    random_num = randint(0, 1)
    if random_num == 0:
        return "run"
    else:
        return "kayak"
        
def random_noun():
    random_num = randint(0,1)
    if random_num == 0:
        return "sofa"
    else:
        return "llama"

def word_transformer(word):
    if word == "NOUN":
        return random_noun()
    elif word == "VERB":
        return random_verb()
    else:
        return word[0]
        
def process_madlib(mad_lib):
    if(mad_lib.find("NOUN") != -1 and mad_lib.find("VERB") != -1):
     processed  = mad_lib.replace("NOUN", word_transformer("NOUN"))
     return processed.replace("VERB", word_transformer("VERB"))
    
      
    # your code here
    # you may find the built-in len function useful for this quiz
    # documentation: https://docs.python.org/2/library/functions.html#len
    
test_string_1 = "This is a good NOUN to use when you VERB your food"
test_string_2 = "I'm going to VERB to the store and pick up a NOUN or two."
print process_madlib(test_string_1)
print process_madlib(test_string_2)
#------------------------------------------------- 


def sum_list(element_number): # this parameter pass as element list number this trick 
    sum = 0
    for element in element_number:
     sum += element
    return sum
print sum_list([1, 7, 4])
#>>> 12

print sum_list([9, 4, 10])
#>>> 23

print sum_list([44, 14, 76])
#>>> 134
# ----------------------------------------- 
name = ['Dave','Sebastian','Katy']
i = 0
while i < len(name):
    y = 0
    while y < len(name[i]):
        print name[i][y]
        y = y + 1
    print "-------------------"
    i = i + 1
 #-----------------------------------
 
def find_element(p, t):
    i = 0
    for e in p:
        if (e == t):
            return i
        i = i + 1
    return -1
print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
#------------------------------------------------
p = [1,2,3,4,5]
print p.index(1)
print "======"
print 2 in p # this is check value ,if it's found return true otherwise return false
print 2 not in p 

#--------------------------------]
# Define a procedure, find_element,
# using index that takes as its
# inputs a list and a value of any
# type, and returns the index of
# the first element in the input
# list that matches the value.

# If there is no matching element,
# return -1.

def find_element(a, b):
    i = 0
    while i < len(a):
        if (a[i] == b):
            return a.index(a[i])
        i += 1
    else:
        return -1

print find_element([1,2,3],3)
#>>> 2

print find_element(['alpha','beta'],'gamma')
#>>> -1
#----------------------------------------------
# --- isleapyear---------
# Given your birthday and the current date, calculate your age 
# in days. Compensate for leap days. Assume that the birthday 
# and current date are correct dates (and no time travel). 
# Simply put, if you were born 1 Jan 2012 and todays date is 
# 2 Jan 2012 you are 1 day old.

# IMPORTANT: You don't need to solve the problem yet! 
# Just brainstorm ways you might approach it!

daysOfMonths = [ 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
current_day = 9754;
st_birthday = 1991;
def isLeapYear(year):
   if (year % 400 == 0):
       return True;
   if (year % 100 == 0):
       return True;
   if (year % 4 == 0):
        return True;
   else:
        return False;
        
    ##
    # Your code here. Return True or False
    # Pseudo code for this algorithm is found at
    # http://en.wikipedia.org/wiki/Leap_year#Algorithm
    ##

     
print isLeapYear(644)
print "-------------"
print daysBetweenDates(1,3,3,2,3,4);
#--------------------------------------------
###
### Define a simple nextDay procedure, that assumes
### every month has 30 days.
###
### For example:
###    nextDay(1999, 12, 30) => (2000, 1, 1)
###    nextDay(2013, 1, 30) => (2013, 2, 1)
###    nextDay(2012, 12, 30) => (2013, 1, 1)  (even though December really has 31 days)
###

def nextDay(year, month, day):
    days_month = 30 # the days in one month and it's fixed is 30 day
    i = 0
    day += 1
    if day >= days_month:
        day = 1
        month += 1
        if (month > 12):
            month = 1
            year += 1
    print (str(year) + ","+str(month)+","+str(day))
    return

nextDay(1991,12,30)
# -----------------------------
# another algorithm for procedure nextDay
if (day < 30):
    return year , month , day + 1
	else:
	    if ( month < 12):
	     return year  ,month + 1, 1
        else:
	    return year + 1, 1, 1