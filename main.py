from tkinter import *

window = Tk()
window.geometry("300x300")
#TODO ADD AT END: window.attributes('-fullscreen', True)
window.title(" SwitchSynonyms ")


greeting = Label(text="Welcome to SwitchSynonyms! "
                      "Replace the most commonly used word in your file! "
                      "Type 'c' to create a text file or 'q' to quit: ")
greeting.pack()
greeting_answer = Text(window, height=5, width=25, bg="black")
greeting_answer.pack()



def welcome_greeting():
    global greeting
    if greeting_answer.get("1.0", "end-1c") == "c" or greeting_answer.get("1.0", "end-1c") == "C":
        Button(window, text="File Creation", command=lambda: create_file()).pack(pady=20)
        Label(text="Enter your file below (Click File Creation").pack()
    elif greeting_answer.get("1.0", "end-1c") == "q" or greeting_answer.get("1.0", "end-1c") == "Q":
        quit()
    else:
        error_message = Label(text="Please enter a valid input (c or q)")
        error_message.pack()


#Creates a user dialog box where users can type in their document and
# it will create a text file with the contents in the dialog box
def create_file():
    file_create = open("synonymswitch.txt", 'w')
    file_enter_string = ""
    file_enter = Text(window, height=25, width=25, bg="black")
    file_enter.pack()

    #TODO: "fix command or move button" Button(window,text="Submit File", command=lambda: create_file()).pack(pady=20)

    file_enter = file_enter_string
    file_create.write(file_enter_string)

#Parses the text file and finds the most used word
# (add to list and increment count)
#def find_syn():

    #TODO: create a user dialog box where user can type in their document and it will create a text file off that



Button(window, text="Welcome/Quit", command=lambda: welcome_greeting()).pack(pady=20)


window.mainloop()