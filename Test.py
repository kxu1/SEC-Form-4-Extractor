from Tkinter import *

def left_command(stringvariable):
	stringvariable.set("LEFT")

root = Tk()
mainframe = Frame(root, bg='blue', bd=10).pack()

bottomframe = Frame(mainframe, bg='red', bd=10).pack(side=BOTTOM)
bottom_button = Button(bottomframe, text="bottom").pack()

topframe = Frame(mainframe, bg='black', bd=10).pack(side=TOP)
top_button = Button(topframe, text="top").pack()

# centerframe = Frame(mainframe, bg='cyan').pack()
# quit_button = Button(mainframe, text="QUIT", command=lambda:quit()).pack()
# 
# leftframe = Frame(mainframe, bg='blue').pack(side=LEFT)
# left_button = Button(leftframe, text="left", command=lambda:left_command(quit_text)).pack()
# ticker_list = Listbox(leftframe, height=10).pack()
# 
# rightframe = Frame(mainframe, bg='green').pack(side=RIGHT)
# right_button = Button(rightframe, text="right").pack()

# quit_text = StringVar()
# quit_text.set("QUIT")
# quit_label = Label(mainframe, textvariable=quit_text).pack()

# label_uno = Label(leftframe, text="Select something here")
# label_uno.pack( side=TOP )
# 
# listboxTester = Listbox(leftframe, height=10)
# 
# # Get the company.get_reporting_information[0] list from SecFormEND, and apply them here:
# 
# listboxTester.insert(END, "Python")
# listboxTester.insert(END, "Perl")
# listboxTester.insert(END, "C")
# listboxTester.insert(END, "PHP")
# listboxTester.insert(END, "JSP")
# listboxTester.insert(END, "Ruby")
# listboxTester.insert(END, "Python")
# listboxTester.insert(END, "Perl")
# listboxTester.insert(END, "C")
# listboxTester.insert(END, "PHP")
# listboxTester.insert(END, "JSP")
# listboxTester.insert(END, "Ruby")
# listboxTester.insert(END, "Python")
# listboxTester.insert(END, "Perl")
# listboxTester.insert(END, "C")
# listboxTester.insert(END, "PHP")
# listboxTester.insert(END, "JSP")
# listboxTester.insert(END, "Ruby")
# listboxTester.insert(END, "Python")
# listboxTester.insert(END, "Perl")
# listboxTester.insert(END, "C")
# listboxTester.insert(END, "PHP")
# listboxTester.insert(END, "JSP")
# listboxTester.insert(END, "Ruby")
# 
# listboxTester.pack( side=LEFT)
# listboxTester.activate(5)
# 
# printbutton = Button(bottomframe, text="Print selection", command=lambda:doyourthing(listboxTester))
# printbutton.pack( side = BOTTOM)
# 
root.mainloop()
