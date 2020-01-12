# load a Tkinter listbox with data lines from a file,
# sort data lines, select a data line, display the data line,
# edit the data line, update listbox with the edited data line
# add/delete a data line, save the updated listbox to a data file
# used a more modern import to give Tkinter items a namespace
# tested with Python24       vegaseat       16nov2006

import tkinter as tk  # gives tk namespace

def add_item():
    """
    add the text in the Entry widget to the end of the listbox
    """
    listbox1.insert(tk.END, enter1.get())


def delete_item():
    """
    delete a selected line from the listbox
    """
    try:
        # get selected line index
        index = listbox1.curselection()[0]
        listbox1.delete(index)
    except IndexError:
        pass


def get_list(event):
    """
    function to read the listbox selection
    and put the result in an entry widget
    """
    # get selected line index
    index = listbox1.curselection()[0]
    # get the line's text
    seltext = listbox1.get(index)
    # delete previous text in enter1
    enter1.delete(0, 50)
    # now display the selected text
    enter1.insert(0, seltext)


def set_list(event):
    """
    insert an edited line from the entry widget
    back into the listbox
    """
    try:
        index = listbox1.curselection()[0]
        # delete old listbox line
        listbox1.delete(index)
    except IndexError:
        index = tk.END
    # insert edited item back into listbox1 at index
    listbox1.insert(index, enter1.get())


def sort_list():
    """
    function to sort listbox items case insensitive
    """
    temp_list = list(listbox1.get(0, tk.END))
    temp_list.sort(key=str.lower)
    # delete contents of present listbox
    listbox1.delete(0, tk.END)
    # load listbox with sorted data
    for item in temp_list:
        listbox1.insert(tk.END, item)


def save_list_jente():
    """
    save the current listbox contents to a file
    """
    # get a list of listbox lines
    temp_list = list(listbox1.get(0, tk.END))
    # add a trailing newline char to each line
    temp_list = [chem + '\n' for chem in temp_list]
    # give the file a different name
    print("jente")
    fout = open("jenter.txt", "w")
    fout.writelines(temp_list)
    fout.close()

def save_list_gutter():
    """
    save the current listbox contents to a file
    """
    # get a list of listbox lines
    temp_list = list(listbox1.get(0, tk.END))
    # add a trailing newline char to each line
    temp_list = [chem + '\n' for chem in temp_list]
    # give the file a different name
    print("gutt")
    fout = open("gutter.txt", "w")
    fout.writelines(temp_list)
    fout.close()


def main_kjønn(kjønn):
    # create the sample data file

    if kjønn == "gutter":
        str1 = open("gutter.txt", "r").read()
        fout = open("gutter.txt", "w")
    else:
        str1 = open("jenter.txt", "r").read()
        fout = open("jenter.txt", "w")

    fout.write(str1)
    fout.close()
    # read the data file into a list
    if kjønn == "gutter":
        fin = open("gutter.txt", "r")
    else:
        fin = open("jenter.txt", "r")
    chem_list = fin.readlines()
    fin.close()
    # strip the trailing newline char
    chem_list = [chem.rstrip() for chem in chem_list]

    root = tk.Tk()
    root.title("Listbox Operations")
    # create the listbox (note that size is in characters)
    globals()["listbox1"] = tk.Listbox(root, width=50, height=6)
    listbox1.grid(row=0, column=0)

    # create a vertical scrollbar to the right of the listbox
    yscroll = tk.Scrollbar(root, command=listbox1.yview, orient=tk.VERTICAL)
    yscroll.grid(row=0, column=1, sticky=tk.N + tk.S)
    listbox1.configure(yscrollcommand=yscroll.set)

    # use entry widget to display/edit selection
    globals()["enter1"] = tk.Entry(root, width=50, bg='yellow')
    enter1.insert(0, 'Click on an item in the listbox')
    enter1.grid(row=1, column=0)
    # pressing the return key will update edited line
    enter1.bind('<Return>', set_list)
    # or double click left mouse button to update line
    enter1.bind('<Double-1>', set_list)
    # button to sort listbox
    button1 = tk.Button(root, text='Sorter', command=sort_list, width=20)
    button1.grid(row=2, column=0, sticky=tk.W)
    # button to save the listbox's data lines to a file
    if kjønn == "gutter":
        button2 = tk.Button(root, text = "Lagre", command=save_list_gutter, width=20)
    else:
        button2 = tk.Button(root, text='Lagre', command=save_list_jente, width=20)
    button2.grid(row=3, column=0, sticky=tk.W)
    # button to add a line to the listbox
    button3 = tk.Button(root, text='Legg til teksten i listen', command=add_item, width=20)
    button3.grid(row=2, column=0, sticky=tk.E)
    # button to delete a line from listbox
    button4 = tk.Button(root, text='Fjern valgte linje    ', command=delete_item, width=20)
    button4.grid(row=3, column=0, sticky=tk.E)

    label1 = tk.Label(root, text="Du må trykke lagre og restarte programmet for å lagre endringer")
    label1.grid(row=4, column=0, sticky=tk.E)
    # load the listbox with data
    for item in chem_list:
        listbox1.insert(tk.END, item)

    # left mouse click on a list item to display selection
    listbox1.bind('<ButtonRelease-1>', get_list)
    root.mainloop()
def main_gutter():
    main_kjønn("gutter")
def main_jenter():
    main_kjønn("jenter")
def close():
    #TODO
    global listbox1
    try:
        return
    except NameError:
        return