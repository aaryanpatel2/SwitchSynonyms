from tkinter import *
from collections import defaultdict
import webbrowser
from bs4 import BeautifulSoup
import requests

window = Tk()
window.geometry("300x300")
window.state('zoomed')
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
        Label(text="Enter your file below (Click File Creation Again When Done)").pack()
        global file_enter
        file_enter = Text(window, height=25, width=100, wrap=WORD, bg="black",)
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
    global words
    global words_list
    file_create = open("synonymswitch.txt", 'r')
    words = file_create.read()
    words_list = words.split(" ")
    words_list = [words.lower() for words in words_list]


    danger_words = ["the", "a", "an", "what"]

    for word in list(words_list):
        if word in danger_words:
            words_list.remove(word)

    for word in list(words_list):
        if "!" in word:
            new_word = word.replace("!", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "@" in word:
            new_word = word.replace("@", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "?" in word:
            new_word = word.replace("?", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "." in word:
            new_word = word.replace(".", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if ";'" in word:
            new_word = word.replace(";", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "," in word:
            new_word = word.replace(",", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if ":" in word:
            new_word = word.replace(":", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "\"" in word:
            new_word = word.replace("\"", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "'" in word:
            new_word = word.replace("'", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "$" in word:
            new_word = word.replace("$", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "%" in word:
            new_word = word.replace("%", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "&" in word:
            new_word = word.replace("&", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "(" in word:
            new_word = word.replace("(", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if ")" in word:
            new_word = word.replace(")", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "{" in word:
            new_word = word.replace("{", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "}" in word:
            new_word = word.replace("}", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "]" in word:
            new_word = word.replace("]", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "[" in word:
            new_word = word.replace("[", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "\\" in word:
            new_word = word.replace("\\", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "/" in word:
            new_word = word.replace("/", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "`" in word:
            new_word = word.replace("`", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "~" in word:
            new_word = word.replace("~", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "*" in word:
            new_word = word.replace("*", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "_" in word:
            new_word = word.replace("_", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "_" in word:
            new_word = word.replace("-", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if "<" in word:
            new_word = word.replace("<", "")
            words_list.append(new_word)
            words_list.remove(word)

    for word in list(words_list):
        if ">" in word:
            new_word = word.replace(">", "")
            words_list.append(new_word)
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
    syn_frame = Frame(syn_window).pack()
    Label(syn_window, syn_frame, text = "• " + most_used_word).pack()
    Label(syn_window, syn_frame, text="").pack()
    thesaurus_button = Button(syn_window, text= "Open Thesaurus.com", command=lambda: open_thesaurus())
    thesaurus_button.place(x = 670, y = 730)



def open_new_window():
    global syn_window
    syn_window = Toplevel(window)
    syn_window.title("SynonymSwitch")
    syn_window.geometry("300x300")
    Button(syn_window, text="Find Synonym", command=lambda: [find_syn(), webscrape()]).pack(pady=20)

def open_thesaurus():
    global thesaurus_win
    thesaurus_win = Toplevel(syn_window)
    thesaurus_win.geometry("800x450")
    url = 'https://www.thesaurus.com/browse/' + most_used_word
    webbrowser.open(url)

def webscrape():
    url = 'https://www.thesaurus.com/browse/' + most_used_word
    result = requests.get(url)
    file = BeautifulSoup(result.text, "html.parser")
    synonyms = file.find_all('li')
    syn_list = []
    for tag in synonyms:
        syn_list.append(tag.get_text())

    account_index = syn_list.index("Account")
    hash_index = syn_list.index("#")

    new_list = syn_list[account_index + 1: hash_index]

    Label(syn_window, text="Try These Synonyms from Thesaurus.com").pack()

    list_display = Text(syn_window, height=25, width=50, bg="black")
    list_display.pack(pady=10)

    for syn in new_list:
        list_display.insert(END, syn + "\n")

    global syn_replace_text
    Label(syn_window, text="Choose a synonym to replace and type below").pack()
    syn_replace_text = Text(syn_window, height=5, width=10, bg="black")
    syn_replace_text.pack()
    Button(syn_window, text="Submit Change", command=lambda: replace()).pack(pady=20)
def replace():
    syn_replace = syn_replace_text.get("1.0", "end-1c")
    if syn_replace == "":
        Label(syn_window, text="No synonym chosen, text remains same")
    else:
        replace_window = Toplevel(syn_window)
        replace_window.title("SynonymSwitch")
        replace_window.geometry("300x300")

        Label(replace_window, text="New Text with Synonyms").pack()

        replace_display = Text(replace_window, height=25, width=50, wrap=WORD, bg="black")
        replace_display.pack(pady=10)

        new_list = [word if word != most_used_word else syn_replace for word in words_list]

        for word in new_list:
            replace_display.insert(END, word + " ")


mainloop()



