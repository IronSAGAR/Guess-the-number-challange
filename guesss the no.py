
import tkinter
import random
from tkinter.font import BOLD


def start():
    def guess(*args):
        nonlocal attempts
        attempts -= 1

        if attempts <= 0:
            text1.set("You Lost.")
            text2.set("Number was %i" % (N))
            user_entry.pack_forget()
            guess_bt.pack_forget()
            call_restart()

        elif N == int(user_input.get()):
            text1.set("Congratulations! ")
            text2.set("YOU WIN !!")
            user_entry.pack_forget()
            guess_bt.pack_forget()
            call_restart()

        elif N < int(user_input.get()):
            text1.set("incorrect.")
            text2.set("try smaller")
        elif N > int(user_input.get()):
            text1.set("incorrect.")
            text2.set("try higher")

        user_input.set("")
        text3.set("attempts left - %i" % (attempts))

    start_bt.pack_forget()
    title.pack_forget()

    N = random.randint(1,99)
    
    text1 = tkinter.StringVar()
    text1.set("Can you guess the number correctly?")
    label1 = tkinter.Label(textvariable=text1,font=("Helvetica",14))
    label1.pack(pady=10)

    text2 = tkinter.StringVar()
    text2.set("HINT - its between 1 to 99")
    label2 = tkinter.Label(textvariable=text2,font=("Helvetica",14))
    label2.pack(pady=10)

    user_input = tkinter.StringVar()
    user_input.set("")
    user_entry = tkinter.Entry(textvariable = user_input, font=("Helvetica",14),width=10)
    user_entry.pack(pady=10)
    user_entry.bind("<Return>",guess)

    guess_bt = tkinter.Button(text="GUESS",font=("Helvetica",16),command=lambda:guess())
    guess_bt.pack(pady=10)

    attempts = 10

    text3 = tkinter.StringVar()
    text3.set("attempts left - %i"%(attempts))
    label3 = tkinter.Label(textvariable=text3,font=("Helvetica",14))
    label3.pack(pady=10)


    def call_restart():
            retry = tkinter.Button(text="PLAY AGAIN",font=("Helvetica",16),command=lambda:restart())
            retry.pack(pady=10)
            QUIT = tkinter.Button(text="QUIT",font=("Helvetica",16),command=lambda:window.destroy())
            QUIT.pack(pady=10)

            def restart():
                retry.destroy()
                QUIT.destroy()
                label1.destroy()
                label2.destroy()
                label3.destroy()
                user_entry.destroy()
                start()


        
window = tkinter.Tk()
window.title('Guess the Number')
window.geometry('400x400')
window.resizable(False,False)

title = tkinter.Label(text = "GUESS THE NUMBER",font=('MS Serif',18,'bold'))
title.pack(pady=100)
start_bt = tkinter.Button(text= "START",font=("Helvetica",16),command=lambda:start())
start_bt.pack(pady=5)


window.mainloop()