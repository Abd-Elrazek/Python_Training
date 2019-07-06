'''
--I told my friend about the idea of this program and liked the idea but preferred to be the period every five hours or more
--- instead of two hours I said you can modify it and customize it for any time time you want to ask me to send him the link of --- the program and told him that it is still an idea and a program under construction, The language of Python and the method of--- programming by which we talked about the procedures and how it can run the program said I liked it I look for a copy of this
application if possible.
'''
'''
The program has two main steps:

Prolonged for two hours
Open and play YouTube link with your favorite music
It repeats it three times
To perform step 1, we use the sleep () function and provide it with the number of seconds required to multiply. But this function can not be used directly because it is defined in another file in Python's main library called Python Standard Library
Therefore, you must call the required file called time within the program file using the word import and then put the desired filename
import time

To execute step 2 we use the open () function and this function opens the given link in the default browser on the machine.
This function is defined inside a file called webbrowser in the Python main library so we are also calling this file
import webbrowser

To repeat, we know two variables, break_times to determine the number of alarms, and count is incremented by 1 each time within the while clause to obtain the desired number of repetitions

In order to calculate the number of seconds in two hours, we multiplied by 2 (two hours) at 60 (sixty minutes per hour) at 60 (sixty seconds per minute)

sleep (2 * 60 * 60)
'''
# author "Abdelrazek"
import time
import webbrowser  
number_breaks= 3
count = 0
while (count < number_breaks):
     time.sleep(60) # in actually we multiplied 2 hours >> (2 * 60 * 60)
     if (number_breaks == 0):
	      webbrowser.open("https://www.youtube.com/watch?v=FkWHg3lvZXw")
     if (number_breaks == 1):
	      webbrowser.open("https://www.youtube.com/watch?v=1ZYbU82GVz4")
     if (number_breaks == 2):
	      webbrowser.open("https://www.youtube.com/watch?v=lFcSrYw-ARY")
     if (number_breaks == 3):
	      webbrowser.open("https://www.youtube.com/watch?v=CcsUYu0PVxY")
     count +=  1