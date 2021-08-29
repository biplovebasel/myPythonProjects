from tkinter import *

def do_nothing():
    print("Nothing")
def open():
    root2=Tk()
    root2.title("Biploves Notepad")
    menu = Menu(root2)
    root2.config(menu=menu)

    # menu items in the menu bar
    filemenu = Menu(menu)
    editmenu = Menu(menu)
    formatmenu = Menu(menu)
    viewmenu = Menu(menu)
    helpmenu = Menu(menu)

    menu.add_cascade(label="File", menu=filemenu)
    menu.add_cascade(label="Edit", menu=editmenu)
    menu.add_cascade(label="Format", menu=formatmenu)
    menu.add_cascade(label="View", menu=viewmenu)
    menu.add_cascade(label="Help", menu=helpmenu)

    # submenu for file
    filemenu.add_command(label="New", command=open)
    filemenu.add_command(label="Open..", command=do_nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Save", command=do_nothing)
    filemenu.add_command(label="SaveAs", command=do_nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Print Setup", command=do_nothing)
    filemenu.add_command(label="Print", command=do_nothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=do_nothing)

    # submenu for Edit
    editmenu.add_command(label="Undo", command=do_nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", command=do_nothing)
    editmenu.add_command(label="Copy", command=do_nothing)
    editmenu.add_command(label="Paste", command=do_nothing)
    editmenu.add_command(label="Delete", command=do_nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Find", command=do_nothing)
    editmenu.add_command(label="Find Next", command=do_nothing)
    editmenu.add_command(label="Replace", command=do_nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Goto To", command=do_nothing)
    editmenu.add_command(label="Select All", command=do_nothing)
    editmenu.add_separator()
    editmenu.add_command(label="Date/Time", command=do_nothing)

    # submenu for Format
    formatmenu.add_command(label="Word Wrap", command=do_nothing)
    formatmenu.add_command(label="Font", command=do_nothing)

    # submenu for View
    viewmenu.add_command(label="Status Bar", command=do_nothing)

    # submenu for Help
    helpmenu.add_command(label="View Help", command=do_nothing)
    helpmenu.add_command(label="About Notepad", command=do_nothing)
    # Text area of the Text editor
    # Begins

    textarea = Frame(root2)
    entry2 = Text(textarea)
    entry2.grid()
    textarea.grid()

    root2.mainloop()


root=Tk()
root.title("Biploves Notepad")
menu=Menu(root)
root.config(menu=menu)

#menu items in the menu bar
filemenu=Menu(menu)
editmenu=Menu(menu)
formatmenu=Menu(menu)
viewmenu=Menu(menu)
helpmenu=Menu(menu)


menu.add_cascade(label="File",menu=filemenu)
menu.add_cascade(label="Edit",menu=editmenu)
menu.add_cascade(label="Format",menu=formatmenu)
menu.add_cascade(label="View",menu=viewmenu)
menu.add_cascade(label="Help",menu=helpmenu)


#submenu for file
filemenu.add_command(label="New",command=open)
filemenu.add_command(label="Open..",command=do_nothing)
filemenu.add_separator()
filemenu.add_command(label="Save",command=do_nothing)
filemenu.add_command(label="SaveAs",command=do_nothing)
filemenu.add_separator()
filemenu.add_command(label="Print Setup",command=do_nothing)
filemenu.add_command(label="Print",command=do_nothing)
filemenu.add_separator()
filemenu.add_command(label="Exit",command=do_nothing)

#submenu for Edit
editmenu.add_command(label="Undo",command=do_nothing)
editmenu.add_separator()
editmenu.add_command(label="Cut",command=do_nothing)
editmenu.add_command(label="Copy",command=do_nothing)
editmenu.add_command(label="Paste",command=do_nothing)
editmenu.add_command(label="Delete",command=do_nothing)
editmenu.add_separator()
editmenu.add_command(label="Find",command=do_nothing)
editmenu.add_command(label="Find Next",command=do_nothing)
editmenu.add_command(label="Replace",command=do_nothing)
editmenu.add_separator()
editmenu.add_command(label="Goto To",command=do_nothing)
editmenu.add_command(label="Select All",command=do_nothing)
editmenu.add_separator()
editmenu.add_command(label="Date/Time",command=do_nothing)

#submenu for Format
formatmenu.add_command(label="Word Wrap",command=do_nothing)
formatmenu.add_command(label="Font",command=do_nothing)

#submenu for View
viewmenu.add_command(label="Status Bar",command=do_nothing)

#submenu for Help
helpmenu.add_command(label="View Help",command=do_nothing)
helpmenu.add_command(label="About Notepad",command=do_nothing)



#Text area of the Text editor
#Begins

textarea=Frame(root,width=169,height=43)
entry2=Text(textarea,width=169,height=43)
entry2.grid()
textarea.grid()

#print(entry2)








root.mainloop()
