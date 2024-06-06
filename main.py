import random
from tkinter import Tk, Button, Frame, Label

def new_game():
    
    global current_player

    current_player = random.choice(players)

    label.config(text=current_player + " turn")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text=" ", bg="SystemButtonFace")


def check_winner():
    
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] == "X":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
        
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] == "X":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
        
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] == "X":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] == "X":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True

    return False

def next_turn(row, column):
    
    global current_player
    global prev_button 

    if buttons[row][column]['text'] != "X" and check_winner() is False:

        if current_player == players[0]:
            
            if buttons[row][column]['text'] == " " and prev_button != buttons[row][column]:

                buttons[row][column]['text'] = current_player
                prev_button = buttons[row][column]

                if check_winner() is False:
                    current_player = players[1]
                    label.config(text=current_player+ " turn")
                elif check_winner() is True:
                    label.config(text=current_player + " wins")
                
            if buttons[row][column]['text'] == "|" and prev_button != buttons[row][column]:

                buttons[row][column]['text'] = "X"
                prev_button = buttons[row][column]

                if check_winner() is False:
                    current_player = players[1]
                    label.config(text=current_player+ " turn")
                elif check_winner() is True:
                    label.config(text=current_player + " wins")
                
        
        else:
            if buttons[row][column]['text'] == " " and prev_button != buttons[row][column]:

                buttons[row][column]['text'] = current_player
                prev_button = buttons[row][column]

                if check_winner() is False:
                    current_player = players[0]
                    label.config(text=current_player+ " turn")
                elif check_winner() is True:
                    label.config(text=current_player + " wins")
                
            if buttons[row][column]['text'] == "-" and prev_button != buttons[row][column]:

                buttons[row][column]['text'] = "X"
                prev_button = buttons[row][column]

                if check_winner() is False:
                    current_player = players[0]
                    label.config(text=current_player+ " turn")
                elif check_winner() is True:
                    label.config(text=current_player + " wins")


# Create the main window
window = Tk()
window.title("Tic Tac Toe")

players = ['-', '|']
current_player = random.choice(players)

buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]
prev_button = None

label = Label(text= current_player + " turn", font=('Arial', 40)) 
label.pack(side="top")

reset_button = Button(window, text="Reset", font=('Arial', 40), command=new_game)
reset_button.pack(side="top")

frame = Frame(window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(frame, text=" ", font=('Arial', 40), width=5, height=2, 
                                      command=lambda row=row, column=column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

# Start the main loop
window.mainloop()