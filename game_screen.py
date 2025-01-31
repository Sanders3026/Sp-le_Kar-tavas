from tkinter import *
import random
import sys

# File paths
easy_words = "easy.txt"
normal_words = "normal.txt"
hard_words = "hard.txt"

word_letters = []
trys = 0
word = ''
difficulty = 0
keys = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
garie = False
pressed_keys = set()

logs = Tk()
screen_width = logs.winfo_screenwidth()
screen_height = logs.winfo_screenheight()

if sys.platform == "darwin":  # macOS
    logs.geometry("1000x800")
elif sys.platform == "win32":  # Windows
    logs.geometry(f"{int(screen_width * 0.6)}x{int(screen_height * 0.8)}")
logs.title("Karātavas")
logs.configure(bg='gray')

start_frame = Frame(logs, bg='gray')
game_frame = Frame(logs, bg='white')
difficulty_select_frame = Frame(logs, bg='white')
win_frame = Frame(game_frame, bg='white')
lose_frame = Frame(game_frame, bg='white')

# Canvas for hangman
a = Canvas(game_frame, width=600, height=350, bg='white')
a.pack()

def draw_base():
    a.create_line(400, 100, 400, 400, fill="black", width=5)
    a.create_line(400, 100, 275, 100, fill="black", width=5)

hangman_parts = [
    lambda:  a.create_line(275, 100, 275, 150, fill="black", width=5),
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
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read().split(',')

def create_lines():
    global word, word_letters, Lines
    word = random.choice(read_words())
    word_letters = ['_'] * len(word)
    Lines = Label(game_frame, text=" ".join(word_letters), font=("Arial", 35, 'bold'), fg='red', bg="white")

def switch_game_screen():
    global trys
    trys = 0
    draw_base()
    difficulty_select_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    create_keyboard(keyboard_frame)
    create_lines()
    Lines.pack()

def switch_difficulty_screen():
    for widget in win_frame.winfo_children():
        widget.destroy()
    for widget in lose_frame.winfo_children():
        widget.destroy()

    start_frame.pack_forget()
    difficulty_select_frame.pack(fill="both", expand=True)

def win_screen():
    keyboard_frame.pack_forget()
    win_frame.pack()
    Lines.configure(text=word, font=("Arial", 35, 'bold'), fg='red', bg="white")
    Label(win_frame, text="Winnēji!", font=("Arial", 35, "bold"), bg="white", fg="red").pack(pady=20)
    Button(win_frame, text="Iziet", command=logs.quit).pack()
    Button(win_frame, text="Spēlēt Atkal", command=play_again).pack(pady=10)

def lose_screen():
    keyboard_frame.pack_forget()
    lose_frame.pack()
    Lines.configure(text=word, font=("Arial", 35, 'bold'), fg='red', bg="white")
    Label(lose_frame, text="Zaudēji!", font=("Arial", 35, "bold"), bg="white", fg="red").pack(pady=20)
    Button(lose_frame, text="Iziet", command=logs.quit).pack()
    Button(lose_frame, text="Spēlēt Atkal", command=play_again).pack(pady=10)

def play_again():
    global word_letters, word, trys, pressed_keys
    word_letters = []
    word = ''
    trys = 0
    a.delete("all")
    pressed_keys = set() 
    win_frame.pack_forget()
    lose_frame.pack_forget()
    game_frame.pack_forget()
    Lines.destroy()
    keyboard_frame.pack_forget()  
    create_keyboard(keyboard_frame)  
    keyboard_frame.pack(pady=100, side='bottom')
    difficulty_select_frame.pack_forget()
    switch_difficulty_screen()

def letter_pressed(letter, button):
    button.config(state=DISABLED)
    pressed_keys.add(letter.lower())
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

def garie_burti():
    global keys, garie, pressed_keys
    if not garie:
        keys = ["QWĒRTYŪĪOP", "ĀŠDFĢHJĶĻ", "ŽXČVBŅM"]
    else:
        keys = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
    garie = not garie
    for widget in keyboard_frame.winfo_children():
        widget.destroy()
    create_keyboard(keyboard_frame)

def create_keyboard(frame):
    global keys
    for row in keys:
        row_frame = Frame(frame, bg='white')
        row_frame.pack(fill='x', expand=True, pady=2)
        inner_frame = Frame(row_frame, bg='white')
        inner_frame.pack(expand=True)
        for letter in row:
            btn = Button(inner_frame, text=letter, font=("Arial", 14, "bold"), width=4, height=2,
                         bg="white", fg="black", activebackground="gray", activeforeground="white")
            btn.config(command=lambda l=letter, b=btn: letter_pressed(l, b))
            if letter.lower() in pressed_keys:
                btn.config(state=DISABLED)
            btn.pack(side='left', padx=3)
    row_frame = Frame(frame, bg='white')
    row_frame.pack(fill='x', expand=True, pady=2)
    inner_frame = Frame(row_frame, bg='white')
    inner_frame.pack(expand=True)
    Button(inner_frame, text="Garie Burti", font=("Arial", 14, "bold"), width=8, height=2, command=garie_burti).pack(side='left', padx=3)

# Start screen widgets
Stat_Label = Label(start_frame, text="★ Karātavas ★", font=("Times New Roman", 50, "bold italic"), fg='gold', bg='black')
Stat_Label.place(relx=0.5, rely=0.3, anchor='center')  # Adjusted to make it more centered
Button(start_frame, text="⚡ Spēlēt ⚡", font=("Impact", 30), fg='cyan', bg='black', command=switch_difficulty_screen).place(relx=0.5, rely=0.5, anchor='center')  # Adjusted to be centered

# Difficulty Selection screen widgets
Label(difficulty_select_frame, text="Izvēlies grūtības līmeni", font=("Arial", 28, "bold"), fg='white', bg='darkblue', pady=20, padx=40, relief=RIDGE, bd=5).place(relx=0.5, rely=0.2, anchor='center')  # Centered the label

Button(difficulty_select_frame, text="Viegls", font=("Arial", 22), bg='#4CAF50', command=lambda: difficulty_select(1)).place(relx=0.5, rely=0.4, anchor='center')  # Centered the button
Button(difficulty_select_frame, text="Normāls", font=("Arial", 22), bg='#FF9800', command=lambda: difficulty_select(2)).place(relx=0.5, rely=0.5, anchor='center')  # Centered the button
Button(difficulty_select_frame, text="Grūts", font=("Arial", 22), bg='#F44336', command=lambda: difficulty_select(3)).place(relx=0.5, rely=0.6, anchor='center')  # Centered the button

start_frame.pack(fill="both", expand=True)
keyboard_frame = Frame(game_frame, bg="white")
keyboard_frame.pack(pady=100, side='bottom')

logs.mainloop()