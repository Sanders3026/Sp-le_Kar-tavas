from tkinter import *
import random

easy_words = "easy.txt"
normal_words = "normal.txt"
hards_words = "hard.txt"

word_letters=[]
Lines = None
trys = 0
word = ''
difficulty = 0
logs = Tk()
logs.resizable(False, False)
logs.geometry("1000x860")
logs.title("Karātavas")
logs.configure(bg='gray')

start_frame = Frame(logs, bg='gray')
game_frame = Frame(logs, bg='white')
difficulty_select_frame = Frame(logs, bg='white')

def draw_hangman():
    a.create_line(400, 100, 400, 400, fill="black", width=5)
    a.create_line(400, 100, 275, 100, fill="black", width=5)
    a.create_line(275, 100, 275, 150, fill="black", width=5)
    a.create_oval(260, 160, 290, 185, fill="black", outline="black", width=20)
    a.create_line(275, 185, 275, 225, fill="black", width=5)
    a.create_line(275, 225, 245, 250, fill="black", width=5)
    a.create_line(275, 225, 300, 250, fill="black", width=5)
    a.create_line(275, 225, 275, 275, fill="black", width=5)
    a.create_line(275, 275, 300, 300, fill="black", width=5)
    a.create_line(275, 275, 250, 300, fill="black", width=5)

def difficulty_select(x):
    global difficulty
    difficulty = x
    switch_game_screen()

def read_words():
    file_path = ''
    if difficulty == 1:
        file_path = easy_words
    elif difficulty == 2:
        file_path = normal_words
    else:
        file_path = hards_words
    with open(file_path, 'r') as file:
        return file.read().split(',')

def create_lines():
    global word
    global word_letters
    global Lines
    word = random.choice(read_words())
    word_letters = ['_'] * len(word)
    Lines = Label(game_frame, text=" ".join(word_letters), font=("Arial", 35,'bold'), fg='red', bg="white")
    Lines.pack(pady=20)

def start_screen():
    start_frame.pack(fill="both", expand=True)

def switch_game_screen():
    create_lines()
    draw_hangman()
    difficulty_select_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    create_keyboard(keyboard_frame)

def switch_difficulty_screen():
    start_frame.pack_forget()
    difficulty_select_frame.pack(fill="both", expand=True)


def letter_pressed(letter):
    global word_letters
    global word
    global Lines
    letter=letter.lower()
    
    if letter.lower() in word:
        for idx, char in enumerate(word):
            if char == letter.lower():
                word_letters[idx] = letter
                Lines.config(text=" ".join(word_letters))
    if ''.join(word_letters).lower() == word:
        print('you win')

def create_keyboard(frame):
    keys = [
        "QWERTYUIOP",
        "ASDFGHJKL",
        "ZXCVBNM"
    ]
    for row_index, row in enumerate(keys):
        for col_index, letter in enumerate(row):
            btn = Button(frame, text=letter, font=("Arial", 14, "bold"), width=4, height=2,
                         bg="black", fg="white", activebackground="gray", activeforeground="white",
                         command=lambda l=letter: letter_pressed(l))
            btn.grid(row=row_index, column=col_index, padx=3, pady=5)


    long_letters_btn = Button(frame, text="GARIE BURTI", font=("Arial", 14, "bold"), width=10, height=2,
                              bg="darkred", fg="white",
                              command=lambda: print("nav pabeigts"))
    long_letters_btn.grid(row=2, column=len(keys[2]), padx=10,columnspan=2)

# Start screen widgets
Stat_Label = Label(start_frame, text="★ Karātavas ★", font=("Times New Roman", 50, "bold italic"), 
                   fg='gold', bg='black', bd=8, relief="ridge")
Stat_Label.place(x=500, y=50, anchor='center')

start_button = Button(start_frame, text="⚡ START ⚡", font=("Impact", 30), 
                      fg='cyan', bg='black', activebackground='darkcyan', 
                      activeforeground='white', bd=8, relief="ridge", width=14, height=2, 
                      command=switch_difficulty_screen)
start_button.place(x=500, y=200, anchor='center')

# Difficulty selection screen widgets
difficulty_label = Label(difficulty_select_frame, text="Izvēlies grūtības līmeni", 
                         font=("Arial", 24, "bold"), fg='white', bg='darkblue', 
                         bd=5, relief="ridge", padx=10, pady=5)
difficulty_label.grid(row=0, column=1, columnspan=3, pady=30)

btn_viegls = Button(difficulty_select_frame, text="Viegls", font=("Arial", 22, "bold"), 
                    fg='white', bg='#4CAF50', activebackground='#388E3C', 
                    activeforeground='white', bd=6, relief="raised", width=10, height=2,
                    command=lambda: difficulty_select(1))  
btn_viegls.grid(row=1, column=0, padx=20, pady=10)

btn_Normāls = Button(difficulty_select_frame, text="Normāls", font=("Arial", 22, "bold"), 
                     fg='white', bg='#FF9800', activebackground='#F57C00', 
                     activeforeground='white', bd=6, relief="raised", width=10, height=2,
                     command=lambda: difficulty_select(2)) 
btn_Normāls.grid(row=1, column=1, padx=20, pady=10)

btn_Grūts = Button(difficulty_select_frame, text="Grūts", font=("Arial", 22, "bold"), 
                   fg='white', bg='#F44336', activebackground='#D32F2F', 
                   activeforeground='white', bd=6, relief="raised", width=10, height=2,
                   command=lambda: difficulty_select(3))  
btn_Grūts.grid(row=1, column=2, padx=20, pady=10)

# Game screen widgets
a = Canvas(game_frame, width=600, height=350, bg='white')
a.pack()

start_screen()

keyboard_frame = Frame(game_frame, bg="white")
keyboard_frame.pack(pady=100,side='bottom')

logs.mainloop()
