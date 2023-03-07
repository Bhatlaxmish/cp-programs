
""" 
date and time


"""



import tkinter
import pytz
import datetime
from time import time as myclock
import time
import webbrowser
import random
import shelve
print(dir(shelve))  # it provides what are in shelve dir is a function
for of in dir(shelve.Shelf):
    print(of)


help(shelve)
help(random)

# webbrowser.open("https://www.python.org")#it opens the link in browser
#date and time
print(time.localtime())  # it prints current date
print(time.time())
print(time.gmtime(0))
time_now = time.localtime()
print("year:-", time_now[0], time_now.tm_year)  # you can print either one way
print("month:-", time_now[1])
print("day:-", time_now[2])
print("hour:-", time_now[3])
print("min:-", time_now[4])
print("second:-", time_now[5])
print()

# from time import perf_counter as myclock

# input("click start to start")
timeelapsed = random.randint(2, 8)
# time.sleep(timeelapsed)
start_time = myclock()
# input("press stop to stop")
end_time = myclock()
print("starting at "+time.strftime("%x", time.localtime(start_time)))
print("ending at"+time.strftime("%x", time.localtime(end_time)))
print("time lapse{}".format(end_time-start_time))

print("the epoth "+time.strftime('%c', time.gmtime(0)))
# %c is used as it is the syntax
print("current time is ", time.tzname, time.timezone)
print(datetime.datetime.today())
print(datetime.datetime.now())
# prints current date and time
print(datetime.datetime.utcnow())
# help(pytz)
country = "Indian/Chagos"
txz = pytz.timezone(country)
ls = datetime.datetime.now(txz)

print("the time in moscow is ".format(ls))

# for x in pytz.all_timezones:
#     print(x)#it gives all timezones
locazl = datetime.datetime.now()
print(pytz.utc.localize(locazl))
print(pytz.utc.localize(datetime.datetime.utcnow()))

# {
# try:
#     import tkinter
# except ImportError:  # python2
#     import TKinter as tkinter
# help(tkinter)
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
# # # tkinter._test()#another window will pop up press quit to exit
# mainWindow = tkinter.Tk()  # it also opens up a window
# mainWindow.title("not perfect")
# mainWindow.geometry('440x388+8+400')
#
# label = tkinter.Label(mainWindow, text="Hello, World")
# label.pack(side='top')
# canvas = tkinter.Canvas(mainWindow, relief='raised', borderwidth=1)
# canvas.pack(side='top', fill=tkinter.Y, expand=True)
# button1 = tkinter.Button(mainWindow, text='button1')
# button2 = tkinter.Button(mainWindow, text='button1')
# button3 = tkinter.Button(mainWindow, text='button1')
# button1.pack(side='left', anchor='n')
# mainWindow.columnconfigure(0, weight=0)
# mainWindow.mainloop()
# }
# ctrl+keyword gives sourcecode
with open("output.txt", mode='w')as centerd_file:
    centerd_file.write("sd" * (80-len("sslfjweff")))


def drawaxes(canvas):
    canvas.update()
    xorigin = canvas.winfo_width()/2
    yorigin = canvas.winfo_width()/2
    # canvas.configure(scrollregion={-xorigin,-yorigin,xorigin,yorigin})
    canvas.create_line(-xorigin, 0, xorigin, 0, fill='green')
    canvas.create_line(-yorigin, 0, yorigin, 0, fill='pink')


mainWindow = tkinter.Tk()
mainWindow.title("patabolw")
mainWindow.geometry("640x480")
canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)
drawaxes(canvas)
mainWindow.mainloop()

print(__name__)
