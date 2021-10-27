from tkinter import *
from PIL import ImageTk, Image
root=Tk()
root.title("ENDLESS DICE GAME")
root.geometry("600x400")
root.configure(background="#fa98d8")

img=ImageTk.PhotoImage(Image.open ("dice1.4.jpg"))


player_1 = Label(root, text="Player 1", bg="purple", fg="white")
player_1.place(relx=0.1, rely=0.3, anchor=CENTER)

player_2 = Label(root, text="Player 2", bg="purple", fg="white")
player_2.place(relx=0.9, rely=0.3, anchor=CENTER)

player_1_score = Label(root, bg="purple", fg="white")
player_1_score.place(relx=0.1, rely=0.4, anchor=CENTER)

player_2_score = Label(root, bg="purple", fg="white")
player_2_score.place(relx=0.9, rely=0.4, anchor=CENTER)

random_dice_label = Label(root, bg="purple", fg="white")
random_dice_label.place(relx=0.5, rely=0.5, anchor=CENTER)

player1_score = 0
def player1():
    global player1_score
    random_no = random.randint(1,6)
    random_dice_label["text"]="PLAYER 1 DICE RANDOM NUMBER :"+str(random_no)
    player1_score = player1_score+random_no
    player_1_score["text"]+str(player1_score)
    
    player_1btn=Button(root, image = img, command = player1)
    player_1btn.place(relx=0.1, rely=0.6, anchor=CENTER)
    
    player2_score = 0
def player2():
    global player2_score
    random_no2 = random.randint(1,6)
    random_dice_label["text"]="PLAYER 2 DICE RANDOM NUMBER :"+str(random_no2)
    player2_score = player2_score+random_no2
    player_2_score["text"]+str(player2_score)
    
    player_2btn=Button(root, image = img, command = player2)
    player_2btn.place(relx=0.9, rely=0.6, anchor=CENTER)
    
root.mainloop()