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

Button(window, text="Welcome/Quit", command=lambda: welcome_greeting()).pack(pady=20)

def welcome_greeting():
    global greeting
    if greeting_answer.get("1.0", "end-1c") == "c" or greeting_answer.get("1.0", "end-1c") == "C":
        Button(window, text="File Creation", command=lambda: create_file()).pack(pady=20)
        Label(text="Enter your file below (Click File Creation to confirm selection)").pack()
        global file_enter
        file_enter = Text(window, height=25, width=50, bg="black",)
        new_window_button = Button(window, text="Open Synonym Window", command=lambda: open_new_window()).pack(side=BOTTOM, padx=20, pady=20)
    elif greeting_answer.get("1.0", "end-1c") == "q" or greeting_answer.get("1.0", "end-1c") == "Q":
        quit()
    else:
        error_message = Label(text="Please enter a valid input (c or q)")
        error_message.pack()


#Creates a user dialog box where users can type in their document and
# it will create a text file with the contents in the dialog box
#file_enter = Text(window, height=25, width=50, bg="black", pady=20)

def create_file():
    file_enter.pack()
    global file_create
    file_create = open("synonymswitch.txt", 'w')
    file_enter_string = file_enter.get("1.0", "end-1c")
    file_create.write(file_enter_string)
    file_create.close()

#Parses the text file and finds the most used word
# (add to list and increment count)
def find_syn():
    file_create = open("synonymswitch.txt", 'r')
    words = file_create.read()
    #print(words)
    words_list = words.split(" ")
    #print(words_list)
    word_frame = Frame(syn_window).pack(pady=20)

    for word in words_list:
        Label(syn_window, word_frame, text = "● " + word).pack()

    syn_list = []

    danger_words = ["the", "a", "an"]

    for word in list(words_list):
        if word in danger_words:
            words_list.remove(word)

    print(words_list)

    for i in range(len(words_list)):
        if words_list[i] == words_list[i-1]:
            syn_list.append(words_list[i])

    print(syn_list)

    Label(syn_window, text = "Here are your most used words").pack(pady=40)
    syn_frame = Frame(syn_window).pack(pady=20)
    for synonym in syn_list:
        Label(syn_window, syn_frame, text = "● " + synonym).pack()



def open_new_window():
    global syn_window
    syn_window = Toplevel(window)
    syn_window.title("SynonymSwitch")
    syn_window.geometry("300x300")
    Button(syn_window, text="Find Synonym", command=lambda: find_syn()).pack(pady=20)


mainloop()



