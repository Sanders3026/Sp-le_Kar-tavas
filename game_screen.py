from tkinter import *
import random
from tkinter import font


easy_words="easy.txt"
normal_words="normal.txt"
hards_words="hard.txt"
trys=0
word=''
difficulty=0
logs=Tk()
logs.geometry("600x600")
logs.title("Karātavas")
logs.configure(bg='gray')

start_frame=Frame(logs, bg='gray')
game_frame=Frame(logs, bg='white')
difficulty_select_frame=Frame(logs, bg='white')
def draw_hangman():
    a.create_line(400, 100, 400, 400,fill="black",width=5)
    a.create_line(400, 100, 275, 100,fill="black",width=5)
    a.create_line(275, 100, 275, 150, fill="black",width=5)
    a.create_oval(260, 160, 290, 185, fill="black", outline="black", width=20)
    a.create_line(275, 185, 275, 225, fill="black", width=5)
    a.create_line(275, 225, 245, 250, fill="black", width=5)
    a.create_line(275, 225, 300, 250, fill="black", width=5)
    a.create_line(275, 225, 275, 275, fill="black", width=5)
    a.create_line(275, 275, 300, 300, fill="black", width=5)
    a.create_line(275, 275, 250, 300, fill="black", width=5)
def difficulty_select(x):
    global difficulty
    difficulty=x
    switch_game_screen()
def read_words():
    file_path=''
    if difficulty==1:
        file_path=easy_words
    elif difficulty==2:
        file_path=normal_words
    else:
        file_path=hards_words
    with open(file_path, 'r') as file:
        return file.read().split(',')

def create_lines():
    global word
    word=random.choice(read_words())
    Lines=Label(game_frame, text= '_ '*len(word), font=("Arial", 20), fg='red',bg="white")
    Lines.pack(pady=20)
def start_screen():
    start_frame.pack(fill="both", expand=True)
def switch_game_screen():
    create_lines()
    draw_hangman()
    difficulty_select_frame.pack_forget()
    game_frame.pack(fill="both", expand=True)
    entry_point.pack(pady=20)
    entry_point.focus_set()
    
def switch_difficulty_screen():
    start_frame.pack_forget()
    difficulty_select_frame.pack(fill="both", expand=True)



start_screen()

#priekäs galvenās spēles loga widgets
a=Canvas(game_frame,width=600,height=350,bg='white')
a.pack()
entry_point=Entry(game_frame,bg='white', font=("Arial", 20),fg='black')
#Plus vēk funkcija create_lines()


#Priekš Start screen widgets
Stat_Label = Label(start_frame, text="★ Karātavas ★", font=("Times New Roman", 50, "bold italic"), 
                   fg='gold', bg='black', bd=8, relief="ridge")

Stat_Label.place(x=300, y=50,anchor='center')

start_button = Button(start_frame, text="⚡ START ⚡", font=("Impact", 30), 
                      fg='cyan', bg='black', activebackground='darkcyan', 
                      activeforeground='white', bd=8, relief="ridge", width=14, height=2,command=switch_difficulty_screen)
start_button.place(x=300, y=200,anchor='center')

#select difficulty screen widgets

difficulty_select_frame.grid_columnconfigure((0, 1, 2), weight=1)  # Make columns expand
difficulty_select_frame.grid_rowconfigure(0)  # Adjust row expansion

difficulty_label = Label(difficulty_select_frame, text="Izvēlies grūtības līmeni", 
                         font=("Arial", 24, "bold"), fg='white', bg='darkblue', 
                         bd=5, relief="ridge", padx=10, pady=5)
difficulty_label.grid(row=0, column=0, columnspan=3, pady=30)  # Span all columns to center

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
btn_viegls.grid(row=1, column=0, padx=20, pady=10)
btn_Normāls.grid(row=1, column=1, padx=20, pady=10)
btn_Grūts.grid(row=1, column=2, padx=20, pady=10)



logs.mainloop()