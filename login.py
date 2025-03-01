import tkinter
import customtkinter
from PIL import ImageTk,Image
import subprocess

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  #creating cutstom tkinter window
app.geometry("600x440")
app.title('Login')

# Obtendo as dimensões da tela
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

window_width = 1280
window_height = 720

position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)

app.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

'''
def button_function():
    app.destroy()            # destroy current window and creating new one 
    w = customtkinter.CTk()  
    w.geometry("1280x720")
    w.title('Welcome')
    l1=customtkinter.CTkLabel(master=w, text="Home Page",font=('Century Gothic',60))
    l1.place(relx=0.5, rely=0.5,  anchor=tkinter.CENTER)
    w.mainloop()
'''
def button_function():
    try:
        app.destroy() 
        subprocess.run(["python", "./app_02.py"], check=True)
    except FileNotFoundError:
        print("O arquivo app_02.py não foi encontrado.")
    except subprocess.CalledProcessError as e:
        print(f"Ocorreu um erro ao executar o script: {e}")


img1=ImageTk.PhotoImage(Image.open("./assets/pattern.png")) 
l1=customtkinter.CTkLabel(master=app,image=img1)
l1.pack()

#creating custom frame
frame=customtkinter.CTkFrame(master=l1, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2=customtkinter.CTkLabel(master=frame, text="Entrar na sua conta",font=('Century Gothic',20))
l2.place(x=62, y=60)

entry1=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Nome de Usuário')
entry1.place(x=50, y=110)

entry2=customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Senha', show="*")
entry2.place(x=50, y=165)

l3=customtkinter.CTkLabel(master=frame, text="Esqueceu a senha?",font=('Century Gothic',12))
l3.place(x=155,y=195)

#Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Entrar", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

img2 = customtkinter.CTkImage(Image.open("./assets/Google__G__Logo.svg.webp").resize((20, 20), Image.Resampling.LANCZOS))
img3 = customtkinter.CTkImage(Image.open("./assets/124010.png").resize((60, 20), Image.Resampling.LANCZOS))

button2= customtkinter.CTkButton(master=frame, image=img2, text="Google", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button2.place(x=50, y=290)

button3= customtkinter.CTkButton(master=frame, image=img3, text="Facebook", width=100, height=20, compound="left", fg_color='white', text_color='black', hover_color='#AFAFAF')
button3.place(x=170, y=290)

app.mainloop()