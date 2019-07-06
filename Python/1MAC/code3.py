# Credit goes to Websten from forums
#
# Program defensively:
#
# What do you do if your input is invalid? For example what should
# happen when date 1 is not before date 2?
#
# Add an assertion to the code for daysBetweenDates to give
# an assertion failure when the inputs are invalid. This should
# occur when the first date is not before the second date.
#  

def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1
def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False        

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    assert dateIsBefore(year1, month1, day1, year2, month2, day2)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

def test():
    test_cases = [((2012,9,30,2012,10,30),30), 
                  ((2012,1,1,2013,1,1),360),
                  ((2012,9,1,2012,9,4),3),
                  ((2013,1,1,1999,12,31), "AssertionError")]
    
    for (args, answer) in test_cases:
        try:
            result = daysBetweenDates(*args)
            if result != answer:
                print "Test with data:", args, "failed"
            else:
                print "Test case passed!"
        except AssertionError:
            if answer == "AssertionError":
                print "Nice job! Test case {0} correctly raises AssertionError!\n".format(args)
            else:
                print "Check your work! Test case {0} should not raise AssertionError!\n".format(args)            
test()

# ---------------------------------------
# Here's another chance to practice your for loop skills. Write code for the 
# function word_in_pos (meaning word in parts_of_speech), which takes in a string 
# word and a list parts_of_speech as inputs. If there is a word in parts_of_speech
# that is a substring of the variable word, then return that word in parts_of_speech, 
# else return None.
import re
test_cases = ["NOUN", "FALSE", "<<@PERSON><", "PLURALNOUN"]
parts_of_speech = ["PERSON", "PLURALNOUN", "NOUN"]
def word_in_pos(word, parts_of_speech):
    i = 0
    word_str = re.sub(r"[^A-Za-z]+", '', word) # this word string after filtered 
    while i < len(word):
        j = 0
        while j < len(parts_of_speech):
            if (word_str == parts_of_speech[j]):
                return parts_of_speech[j]
            j += 1
        i += 1    
    

print word_in_pos(test_cases[0], parts_of_speech)
print word_in_pos(test_cases[1], parts_of_speech)
print word_in_pos(test_cases[2], parts_of_speech)
print word_in_pos(test_cases[3], parts_of_speech)
# another code 
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
	    if pos in word:
		return pos
	return "None"	
# -------------------------------------------------------
# ------ this is another code challenge that's is difficult 
# Write code for the function play_game, which takes in as inputs parts_of_speech
# (a list of acceptable replacement words) and ml_string (a string that
# can contain replacement words that are found in parts_of_speech). Your play_game
# function should return the joined list replaced, which will have the same structure
# as ml_string, only that replacement words are swapped out with "corgi", since this
# program cannot replace those words with user input.

parts_of_speech  = ["PLACE", "PERSON", "PLURALNOUN", "NOUN"]

test_string = """This is PLACE, no NOUN named PERSON, We have so many PLURALNOUN around here."""

def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

def play_game(ml_string, parts_of_speech):
    replaced = []
    ml_string = ml_string.split()
    for word in ml_string:
       replacement = word_in_pos(word, parts_of_speech)
       if replacement != None:
          word = word.replace(replacement, "corgi")
          replaced.append(word)
       else:
          replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

print play_game(test_string, parts_of_speech)
#------------------------------------------
#for Graphics making
import turtle

def draw_r (turtle, size, small_angle):
    for i in range(2):
        turtle.forward(size)
        turtle.right(small_angle)
        turtle.forward(size)
        turtle.right((360-2 * small_angle)//2)

def draw_flower(turtle, size, angle):
    for i in range (360// angle):
        draw_r(turtle, size, 60)
        turtle.right(angle)
    turtle.right(90)
    turtle.forward(size * 3)

canvas = turtle.Screen()
canvas.colormode(255)
canvas.bgcolor("red")

bruce = turtle.Turtle("turtle")
bruce.color("green")
bruce.speed(4)

draw_flower(bruce, 100, 15)
#-------------------------------