from tkinter import *
import random

# File paths for different difficulty levels
easy_words = "easy.txt"
normal_words = "normal.txt"
hard_words = "hard.txt"

word_letters = []
trys = 0
word = ''
difficulty = 0

logs = Tk()
logs.geometry("1000x860")
logs.title("Karātavas")
logs.configure(bg='gray')

start_frame = Frame(logs, bg='gray')
game_frame = Frame(logs, bg='white')
difficulty_select_frame = Frame(logs, bg='white')
win_frame = Frame(game_frame, bg='white')

# Canvas for hangman
a = Canvas(game_frame, width=600, height=350, bg='white')
a.pack()

def draw_base():
    a.create_line(400, 100, 400, 400, fill="black", width=5)
    a.create_line(400, 100, 275, 100, fill="black", width=5)
    a.create_line(275, 100, 275, 150, fill="black", width=5)


hangman_parts = [
    lambda: a.create_oval(260, 160, 290, 185, fill="black", outline="black", width=20),
    lambda: a.create_line(275, 185, 275, 225, fill="black", width=5),  
    lambda: a.create_line(275, 225, 245, 250, fill="black", width=5),  
    lambda: a.create_line(275, 225, 300, 250, fill="black", width=5),   
    lambda: a.create_line(275, 225, 275, 275, fill="black", width=5),  
    lambda: a.create_line(275, 275, 300, 300, fill="black", width=5),  
    lambda: a.create_line(275, 275, 250, 300, fill="black", width=5)   
]

def draw_next_part():
    global trys
    if trys < len(hangman_parts):
        hangman_parts[trys]()
        trys += 1
    if trys == len(hangman_parts):
        lose_screen()

def difficulty_select(x):
    global difficulty
    difficulty = x
    switch_game_screen()

def read_words():
    file_path = {1: easy_words, 2: normal_words, 3: hard_words}.get(difficulty, easy_words)
    with open(file_path, 'r') as file:
        return file.read().split(',')

def create_lines():
    global word, word_letters, Lines
    word = random.choice(read_words())
    word_letters = ['_'] * len(word)
    Lines = Label(game_frame, text=" ".join(word_letters), font=("Arial", 35, 'bold'), fg='red', bg="white")
    Lines.pack(pady=20)

def switch_game_screen():
    global trys
    trys = 0
    a.delete("all")
    draw_base()
    create_lines()
    difficulty_select_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    create_keyboard(keyboard_frame)

def switch_difficulty_screen():
    start_frame.pack_forget()
    difficulty_select_frame.pack(fill="both", expand=True)

def win_screen():
    keyboard_frame.pack_forget()
    win_frame.pack()
    Label(win_frame, text="You win!", bg='white', font=("Arial", 35, 'bold')).pack()
    Button(win_frame, text="Exit", command=logs.quit).pack()
    Button(win_frame, text="Play Again", command=play_again).pack(pady=10)

def lose_screen():
    keyboard_frame.pack_forget()
    Label(game_frame, text="Game Over!", font=("Arial", 35, "bold"), bg="white", fg="red").pack()
    

def play_again():
    Lines.pack_forget()
    game_frame.pack_forget()
    switch_difficulty_screen()
    win_frame.destroy()

def letter_pressed(letter, button):
    button.config(state=DISABLED)
    global word_letters, word, Lines
    letter = letter.lower()
    if letter in word:
        for idx, char in enumerate(word):
            if char == letter:
                word_letters[idx] = letter
        Lines.config(text=" ".join(word_letters))
        if "".join(word_letters) == word:
            win_screen()
    else:
        draw_next_part()

def create_keyboard(frame):
    keys = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    for row_index, row in enumerate(keys):
        for col_index, letter in enumerate(row):
            btn = Button(frame, text=letter, font=("Arial", 14, "bold"), width=4, height=2,
                         bg="black", fg="white", activebackground="gray", activeforeground="white")
            btn.config(command=lambda l=letter, b=btn: letter_pressed(l, b))
            btn.grid(row=row_index, column=col_index, padx=3, pady=5)

#Start screen widgets
Stat_Label = Label(start_frame, text="★ Karātavas ★", font=("Times New Roman", 50, "bold italic"), fg='gold', bg='black')
Stat_Label.place(x=500, y=50, anchor='center')
Button(start_frame, text="⚡ START ⚡", font=("Impact", 30), fg='cyan', bg='black', command=switch_difficulty_screen).place(x=500, y=200, anchor='center')

# Difficulty Selection
Label(difficulty_select_frame, text="Izvēlies grūtības līmeni", font=("Arial", 24, "bold"), fg='white', bg='darkblue').grid(row=0, column=1, pady=30)
Button(difficulty_select_frame, text="Viegls", font=("Arial", 22), fg='white', bg='#4CAF50', command=lambda: difficulty_select(1)).grid(row=1, column=0, padx=20)
Button(difficulty_select_frame, text="Normāls", font=("Arial", 22), fg='white', bg='#FF9800', command=lambda: difficulty_select(2)).grid(row=1, column=1, padx=20)
Button(difficulty_select_frame, text="Grūts", font=("Arial", 22), fg='white', bg='#F44336', command=lambda: difficulty_select(3)).grid(row=1, column=2, padx=20)

start_frame.pack(fill="both", expand=True)
keyboard_frame = Frame(game_frame, bg="white")
keyboard_frame.pack(pady=100, side='bottom')

logs.mainloop()