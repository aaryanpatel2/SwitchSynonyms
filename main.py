from tkinter import *
from collections import defaultdict
import webbrowser

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
        Label(text="Enter your file below (Click file creation twice to confirm selection)").pack()
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
    words_list = words.split(" ")

    danger_words = ["the", "a", "an"]

    for word in list(words_list):
        if word in danger_words:
            words_list.remove(word)


    global syn_list
    temp = defaultdict(int)

    for words in words_list:
        for word in words.split():
            temp[word] += 1

    global most_used_word
    most_used_word = max(temp, key=temp.get)

    if words_list.count(most_used_word) == 1:
        most_used_word = "Every word appears once :)"
        syn_window.after(3000, lambda:syn_window.destroy())

    file_create.close()


    Label(syn_window, text = "Here is your most used word").pack(pady=30)
    syn_frame = Frame(syn_window).pack(pady=20)
    Label(syn_window, syn_frame, text = "• " + most_used_word).pack()
    Button(syn_window, text= "Open Thesaurus.com", command=lambda: open_thesarus()).pack(pady=60)



def open_new_window():
    global syn_window
    syn_window = Toplevel(window)
    syn_window.title("SynonymSwitch")
    syn_window.geometry("300x300")
    Button(syn_window, text="Find Synonym", command=lambda: find_syn()).pack(pady=20)

def open_thesarus():
    global thesaurus_win
    thesaurus_win = Toplevel(syn_window)
    thesaurus_win.geometry("800x450")
    url = 'https://www.thesaurus.com/browse/' + most_used_word
    webbrowser.open(url)




mainloop()



