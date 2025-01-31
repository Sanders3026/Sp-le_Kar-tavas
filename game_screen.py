from tkinter import *
import random
import sys
# File paths
easy_words = "easy.txt"
normal_words = "normal.txt"
hard_words = "hard.txt"
# Globālās mainīgās
word_letters = []
trys = 0
word = ''
difficulty = 0
keys = ["QWERTYUIOP", "ASDFGHJKL", "ZXCVBNM"]
garie = False
pressed_keys = set()
# Krāsu shēma
COLORS = {
    "background": "#2E294E",
    "accent": "#EED5C7",
    "primary": "#D72638",
    "secondary": "#3F88C5",
    "text": "#FFFFFF",
    "disabled": "#6C757D"
}
# Loga inicializācija
logs = Tk()
screen_width = logs.winfo_screenwidth()
screen_height = logs.winfo_screenheight()
if sys.platform == "darwin":  # macOS
    logs.geometry("1000x800")
elif sys.platform == "win32":  # Windows
    logs.geometry(f"{int(screen_width * 0.6)}x{int(screen_height * 0.8)}")
logs.title("Karātavas")
logs.configure(bg=COLORS["background"])
# Frames
start_frame = Frame(logs, bg=COLORS["background"])
game_frame = Frame(logs, bg=COLORS["background"])
difficulty_select_frame = Frame(logs, bg=COLORS["background"])
win_frame = Frame(game_frame, bg=COLORS["background"])
lose_frame = Frame(game_frame, bg=COLORS["background"])
# Canvas for hangman
a = Canvas(game_frame, width=600, height=350, bg=COLORS["background"], highlightthickness=0)
a.pack(pady=20)
def draw_base():
    a.create_line(400, 100, 400, 400, fill=COLORS["accent"], width=5)
    a.create_line(400, 100, 275, 100, fill=COLORS["accent"], width=5)
hangman_parts = [
    lambda: a.create_line(275, 100, 275, 150, fill=COLORS["primary"], width=5),
    lambda: a.create_oval(260, 160, 290, 185, fill=COLORS["primary"], outline=COLORS["primary"], width=20),
    lambda: a.create_line(275, 185, 275, 225, fill=COLORS["primary"], width=5),
    lambda: a.create_line(275, 225, 245, 250, fill=COLORS["primary"], width=5),
    lambda: a.create_line(275, 225, 300, 250, fill=COLORS["primary"], width=5),
    lambda: a.create_line(275, 225, 275, 275, fill=COLORS["primary"], width=5),
    lambda: a.create_line(275, 275, 300, 300, fill=COLORS["primary"], width=5),
    lambda: a.create_line(275, 275, 250, 300, fill=COLORS["primary"], width=5)
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
    Lines = Label(game_frame, text=" ".join(word_letters), font=("Arial", 35, 'bold'), fg=COLORS["primary"], bg=COLORS["background"])
    Lines.pack(pady=20)
def switch_game_screen():
    global trys
    trys = 0
    a.delete("all")
    draw_base()
    difficulty_select_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    create_keyboard(keyboard_frame)
    create_lines()
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
    Lines.configure(text=word, font=("Arial", 35, 'bold'), fg=COLORS["primary"], bg=COLORS["background"])
    Label(win_frame, text="🏆 Uzvarēji! 🏆", font=("Arial", 35, "bold"), bg=COLORS["background"], fg=COLORS["secondary"]).pack(pady=20)
    Button(win_frame, text="Iziet", font=("Arial", 18), bg=COLORS["secondary"], fg=COLORS["text"], command=logs.quit).pack(side='left', padx=20)
    Button(win_frame, text="Spēlēt Atkal", font=("Arial", 18), bg=COLORS["primary"], fg=COLORS["text"], command=play_again).pack(side='right', padx=20)
def lose_screen():
    keyboard_frame.pack_forget()
    lose_frame.pack()
    Lines.configure(text=word, font=("Arial", 35, 'bold'), fg=COLORS["primary"], bg=COLORS["background"])
    Label(lose_frame, text="💀 Zaudēji! 💀", font=("Arial", 35, "bold"), bg=COLORS["background"], fg=COLORS["secondary"]).pack(pady=20)
    Button(lose_frame, text="Iziet", font=("Arial", 18), bg=COLORS["secondary"], fg=COLORS["text"], command=logs.quit).pack(side='left', padx=20)
    Button(lose_frame, text="Spēlēt Atkal", font=("Arial", 18), bg=COLORS["primary"], fg=COLORS["text"], command=play_again).pack(side='right', padx=20)
def play_again():
    global word_letters, word, trys, pressed_keys, keyboard_frame
    word_letters = []
    word = ''
    trys = 0
    a.delete("all")
    pressed_keys = set()
    win_frame.pack_forget()
    lose_frame.pack_forget()
    game_frame.pack_forget()
    Lines.destroy()
    # Atkārtoti izveidojam klaviatūru
    keyboard_frame = Frame(game_frame, bg=COLORS["background"])
    keyboard_frame.pack(pady=20, side='bottom')
    # Pārslēdzamies uz sākuma ekrānu
    switch_difficulty_screen()
def letter_pressed(letter, button):
    button.config(state=DISABLED)
    pressed_keys.add(letter.lower())
    global word_letters
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
        row_frame = Frame(frame, bg=COLORS["background"])
        row_frame.pack(fill='x', expand=True, pady=2)
        inner_frame = Frame(row_frame, bg=COLORS["background"])
        inner_frame.pack(expand=True)
        for letter in row:
            btn = Button(inner_frame, text=letter, font=("Arial", 14, "bold"), width=4, height=2,
                         bg=COLORS["secondary"], fg=COLORS["text"], activebackground=COLORS["primary"], activeforeground=COLORS["text"])
            btn.config(command=lambda l=letter, b=btn: letter_pressed(l, b))
            if letter.lower() in pressed_keys:
                btn.config(state=DISABLED)
            btn.pack(side='left', padx=3)
    row_frame = Frame(frame, bg=COLORS["background"])
    row_frame.pack(fill='x', expand=True, pady=2)
    inner_frame = Frame(row_frame, bg=COLORS["background"])
    inner_frame.pack(expand=True)
    Button(inner_frame, text="Garie Burti", font=("Arial", 14, "bold"), width=8, height=2, bg=COLORS["primary"], fg=COLORS["text"], command=garie_burti).pack(side='left', padx=3)
# Start screen widgets
Stat_Label = Label(start_frame, text="★ Karātavas ★", font=("Times New Roman", 50, "bold italic"), fg=COLORS["accent"], bg=COLORS["background"])
Stat_Label.place(relx=0.5, rely=0.3, anchor='center')
Button(start_frame, text="⚡ Spēlēt ⚡", font=("Impact", 30), fg=COLORS["text"], bg=COLORS["primary"], command=switch_difficulty_screen).place(relx=0.5, rely=0.5, anchor='center')
# Difficulty Selection screen widgets
Label(difficulty_select_frame, text="Izvēlies grūtības līmeni", font=("Arial", 28, "bold"), fg=COLORS["text"], bg=COLORS["background"], pady=20, padx=40).place(relx=0.5, rely=0.2, anchor='center')
Button(difficulty_select_frame, text="Viegls", font=("Arial", 22), bg="#4CAF50", fg=COLORS["text"], command=lambda: difficulty_select(1)).place(relx=0.5, rely=0.4, anchor='center')
Button(difficulty_select_frame, text="Normāls", font=("Arial", 22), bg="#FF9800", fg=COLORS["text"], command=lambda: difficulty_select(2)).place(relx=0.5, rely=0.5, anchor='center')
Button(difficulty_select_frame, text="Grūts", font=("Arial", 22), bg="#F44336", fg=COLORS["text"], command=lambda: difficulty_select(3)).place(relx=0.5, rely=0.6, anchor='center')
start_frame.pack(fill="both", expand=True)
keyboard_frame = Frame(game_frame, bg=COLORS["background"])
keyboard_frame.pack(pady=20, side='bottom')
logs.mainloop()