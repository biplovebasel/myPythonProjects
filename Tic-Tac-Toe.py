def delay():
    a = 0
    for i in range (10000000):
        a = a + 1
    return


def win():
    # Xs

    if BUT1A["text"] == " X " and BUT1B["text"] == " X " and BUT1C["text"] == " X ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

        # game_reset2(label)

    if BUT2A["text"] == " X " and BUT2B["text"] == " X " and BUT2C["text"] == " X ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT3A["text"] == " X " and BUT3B["text"] == " X " and BUT3C["text"] == " X ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT1A["text"] == " X " and BUT2A["text"] == " X " and BUT3A["text"] == " X ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT1B["text"] == " X " and BUT2B["text"] == " X " and BUT3B["text"] == " X ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT1C["text"] == " X " and BUT2C["text"] == " X " and BUT3C["text"] == " X ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT1A["text"] == " X " and BUT2B["text"] == " X " and BUT3C["text"] == " X ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT3A["text"] == " X " and BUT2B["text"] == " X " and BUT1C["text"] == " X ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    # Os
    if BUT1A["text"] == " O " and BUT1B["text"] == " O " and BUT1C["text"] == " O ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT2A["text"] == " O " and BUT2B["text"] == " O " and BUT2C["text"] == " O ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT3A["text"] == " O " and BUT3B["text"] == " O " and BUT3C["text"] == " O ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT1A["text"] == " O " and BUT2A["text"] == " O " and BUT3A["text"] == " O ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT1B["text"] == " O " and BUT2B["text"] == " O " and BUT3B["text"] == " O ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT1C["text"] == " O " and BUT2C["text"] == " O " and BUT3C["text"] == " O ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT1A["text"] == " O " and BUT2B["text"] == " O " and BUT3C["text"] == " O ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)

    if BUT1C["text"] == " O " and BUT2B["text"] == " O " and BUT3A["text"] == " O ":
        print ('win')
        label = Label (frame3, text='WIN!!!')
        label.grid (row=1, columnspan=3)
        frame3.pack ()
        BUT_reset.bind ("<Button-1>", game_reset2)


def game_reset2(event):
    # delay()
    BUT1A["text"] = "     "
    BUT1B["text"] = "     "
    BUT1C["text"] = "     "
    BUT2A["text"] = "     "
    BUT2B["text"] = "     "
    BUT2C["text"] = "     "
    BUT3A["text"] = "     "
    BUT3B["text"] = "     "
    BUT3C["text"] = "     "
    global counter
    counter = 0


def game_reset(event):
    BUT1A["text"] = "     "
    BUT1B["text"] = "     "
    BUT1C["text"] = "     "
    BUT2A["text"] = "     "
    BUT2B["text"] = "     "
    BUT2C["text"] = "     "
    BUT3A["text"] = "     "
    BUT3B["text"] = "     "
    BUT3C["text"] = "     "
    global counter
    counter = 0


def xo1a():
    global counter
    counter = counter + 1
    print (counter)
    if BUT1A["text"] == "     ":
        if counter % 2 == 0:
            # switch to Goodbye
            BUT1A["text"] = " X "
        else:
            BUT1A["text"] = " O "
    win ()


def xo1b():
    global counter
    counter = counter + 1
    print (counter)
    if BUT1B["text"] == "     ":
        if counter % 2 == 0:
            # switch to Goodbye
            BUT1B["text"] = " X "
        else:
            BUT1B["text"] = " O "
    win ()


def xo1c():
    global counter
    counter = counter + 1
    print (counter)
    if BUT1C["text"] == "     ":
        if counter % 2 == 0:
            # switch to Goodbye
            BUT1C["text"] = " X "
        else:
            BUT1C["text"] = " O "
    win ()


def xo2a():
    global counter
    counter = counter + 1
    print (counter)
    if BUT2A["text"] == "     ":
        if counter % 2 == 0:
            # switch to Goodbye
            BUT2A["text"] = " X "
        else:
            BUT2A["text"] = " O "
    win ()


def xo2b():
    global counter
    counter = counter + 1
    print (counter)
    if BUT2B["text"] == "     ":
        if counter % 2 == 0:
            # switch to Goodbye
            BUT2B["text"] = " X "
        else:
            BUT2B["text"] = " O "
    win ()


def xo2c():
    global counter
    counter = counter + 1
    print (counter)
    if BUT2C["text"] == "     ":
        if counter % 2 == 0:
            # switch to Goodbye
            BUT2C["text"] = " X "
        else:
            BUT2C["text"] = " O "
    win ()


def xo3a():
    global counter
    counter = counter + 1
    print (counter)
    if BUT3A["text"] == "     ":
        if counter % 2 == 0:
            # switch to Goodbye
            BUT3A["text"] = " X "
        else:
            BUT3A["text"] = " O "
    win ()


def xo3b():
    global counter
    counter = counter + 1
    print (counter)
    if BUT3B["text"] == "     ":
        if counter % 2 == 0:
            # switch to Goodbye
            BUT3B["text"] = " X "
        else:
            BUT3B["text"] = " O "
    win ()


def xo3c():
    global counter
    counter = counter + 1
    print (counter)
    if BUT3C["text"] == "     ":
        if counter % 2 == 0:
            # switch to Goodbye
            BUT3C["text"] = " X "
        else:
            BUT3C["text"] = " O "
    win ()

def game():
    print("apples")

from tkinter import *

game.__init__
counter = 0
root = Tk ()
frame1 = Frame (root)
frame2 = Frame (root)
frame3 = Frame (root)

BUT1A = Button (frame1, text='     ', command=xo1a)
BUT1B = Button (frame1, text='     ', command=xo1b)
BUT1C = Button (frame1, text='     ', command=xo1c)
BUT2A = Button (frame1, text='     ', command=xo2a)
BUT2B = Button (frame1, text='     ', command=xo2b)
BUT2C = Button (frame1, text='     ', command=xo2c)
BUT3A = Button (frame1, text='     ', command=xo3a)
BUT3B = Button (frame1, text='     ', command=xo3b)
BUT3C = Button (frame1, text='     ', command=xo3c)

BUT_reset = Button (frame2, text='RESET', width=10)

# Packing

BUT1A.grid (row=2, column=1)
BUT1B.grid (row=2, column=2)
BUT1C.grid (row=2, column=3)
BUT2A.grid (row=3, column=1)
BUT2B.grid (row=3, column=2)
BUT2C.grid (row=3, column=3)
BUT3A.grid (row=4, column=1)
BUT3B.grid (row=4, column=2)
BUT3C.grid (row=4, column=3)

BUT_reset.grid (row=5, columnspan=3)
BUT_reset.bind ("<Button-1>", game_reset)
frame1.pack ()
frame2.pack (side=BOTTOM)
root.mainloop ()






