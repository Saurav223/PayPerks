import customtkinter as ctk
from tkinter import messagebox
from PIL import ImageTk, Image
from itertools import cycle

class PayPerksAuth:
    def __init__(self):
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")

        # Window setup
        self.window = ctk.CTk(fg_color="white")
        self.window.title('PayPerks Auth')
        self.window.geometry('925x500')
        self.window.resizable(False, False)

        self.bg_index = [0]
        self.bg_images = ['img/bg.png', 'img/bg3.png','img/bg4.png']
        self.is_animating = [False]
        self.words = cycle([
            "Secure. Simple. Smart Wallet.",
            "Your money, your control.",
            "Fast, safe & easy transactions."
        ])

        self.setup_ui()
        self.window.after(5000, self.swap_bg_and_animate)
    
    def run(self):
        self.window.mainloop()
        
    def raise_frame(self, frame):
        frame.tkraise()

    def setup_ui(self):
        # Image and Label
        img = Image.open('img/PAYPERKS2.png').resize((250, 250))
        self.payperks_img = ImageTk.PhotoImage(img)
        ctk.CTkLabel(self.window, image=self.payperks_img, text="", bg_color='white').place(x=500, y=-40)

        self.bg_label = ctk.CTkLabel(self.window, text="", bg_color='white')
        self.bg_label.place(x=20, y=50)
        self.load_bg(self.bg_index[0])

        self.typing_label = ctk.CTkLabel(self.window, text='', text_color='black', font=ctk.CTkFont("Segoe UI", 16, "bold"))
        self.typing_label.place(x=90, y=390)
        self.text_to_type = "Welcome to PayPerks!"
        self.type_text()

        # Sign Up and Sign In Frames
        self.signup_frame = ctk.CTkFrame(self.window, width=450, height=360, fg_color='white')
        self.signin_frame = ctk.CTkFrame(self.window, width=450, height=360, fg_color='white')
        for frame in (self.signup_frame, self.signin_frame):
            frame.place(x=400, y=110)

        self.build_signup_form()
        self.build_signin_form()
        self.raise_frame(self.signup_frame)

    def load_bg(self, index):
        bg_img = Image.open(self.bg_images[index]).resize((400, 400))
        tk_img = ImageTk.PhotoImage(bg_img)
        self.bg_label.configure(image=tk_img)
        self.bg_label.image = tk_img

    def type_text(self, index=0):
        if index < len(self.text_to_type):
            self.typing_label.configure(text=self.typing_label.cget("text") + self.text_to_type[index])
            self.window.after(100, self.type_text, index + 1)

    def erase_text(self):
        self.is_animating[0] = True
        current = self.typing_label.cget("text")
        if current:
            self.typing_label.configure(text=current[:-1])
            self.window.after(50, self.erase_text)
        else:
            self.show_next_word()

    def show_next_word(self):
        word = next(self.words)
        self.typing_label.configure(text="")
        self.type_word(word)

    def type_word(self, word, index=0):
        if index < len(word):
            self.typing_label.configure(text=self.typing_label.cget("text") + word[index])
            self.window.after(150, self.type_word, word, index + 1)
        else:
            self.window.after(1200, self.erase_text)

    def slide_bg_out(self, x=10):
        if x > -400:
            self.bg_label.place(x=x, y=50)
            self.window.after(5, self.slide_bg_out, x - 10)
        else:
            self.swap_bg_image()

    def slide_bg_in(self, x=-400):
        if x < 10:
            self.bg_label.place(x=x, y=50)
            self.window.after(5, self.slide_bg_in, x + 10)
        else:
            self.window.after(100, lambda: self.is_animating.__setitem__(0, False))

    def swap_bg_image(self):
        self.bg_index[0] = (self.bg_index[0] + 1) % len(self.bg_images)
        self.load_bg(self.bg_index[0])
        self.slide_bg_in()
        self.erase_text()

    def swap_bg_and_animate(self):
        if not self.is_animating[0]:
            self.slide_bg_out()
            self.is_animating[0] = True
        self.window.after(5000, self.swap_bg_and_animate)

    def build_signup_form(self):
        ctk.CTkLabel(self.signup_frame, text='Sign Up', text_color='#57a1f8', font=ctk.CTkFont(size=23, weight="bold")).place(x=25, y=10)

        self.name = ctk.CTkEntry(self.signup_frame, width=300, placeholder_text="Full Name")
        self.name.place(x=30, y=50)

        self.user = ctk.CTkEntry(self.signup_frame, width=300, placeholder_text="Username")
        self.user.place(x=30, y=90)

        self.code = ctk.CTkEntry(self.signup_frame, width=300, placeholder_text="Password", show="*")
        self.code.place(x=30, y=130)

        self.confirm_code = ctk.CTkEntry(self.signup_frame, width=300, placeholder_text="Confirm Password", show="*")
        self.confirm_code.place(x=30, y=170)

        self.email = ctk.CTkEntry(self.signup_frame, width=300, placeholder_text="Email")
        self.email.place(x=30, y=210)

        signup_btn = ctk.CTkButton(self.signup_frame, text="Sign Up", width=300, fg_color="#57a1f8", hover_color="#0052cc", command=self.signup)
        signup_btn.place(x=30, y=250)

        ctk.CTkLabel(self.signup_frame, text="I have an account?", text_color="black", font=ctk.CTkFont(size=11)).place(x=30, y=280)
        ctk.CTkButton(self.signup_frame, width=50, text="Sign In", fg_color="transparent", text_color="#57a1f8", hover=False, command=lambda: self.raise_frame(self.signin_frame)).place(x=130, y=280)

    def build_signin_form(self):
        ctk.CTkLabel(self.signin_frame, text='Sign In', text_color='#57a1f8', font=ctk.CTkFont(size=23, weight="bold")).place(x=25, y=10)

        self.user_signin = ctk.CTkEntry(self.signin_frame, width=300, placeholder_text="Username")
        self.user_signin.place(x=30, y=60)

        self.code_signin = ctk.CTkEntry(self.signin_frame, width=300, placeholder_text="Password", show="*")
        self.code_signin.place(x=30, y=120)

        signin_btn = ctk.CTkButton(self.signin_frame, text="Sign In", width=300, fg_color="#57a1f8", hover_color="#0052cc", command=self.signin)
        signin_btn.place(x=30, y=180)

        ctk.CTkLabel(self.signin_frame, text="Don't have an account?", text_color="black", font=ctk.CTkFont(size=11)).place(x=30, y=230)
        ctk.CTkButton(self.signin_frame, width=50, text="Sign Up", fg_color="transparent", text_color="#57a1f8", hover=False, command=lambda: self.raise_frame(self.signup_frame)).place(x=145, y=230)

    def signup(self):
        username = self.user.get()
        password = self.code.get()
        confirm_password = self.confirm_code.get()
        if username == '' or password == '' or confirm_password == '':
            messagebox.showerror("Error", "All fields are required")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            messagebox.showinfo("Success", "Sign Up Successful")

    def signin(self):
        username = self.user_signin.get()
        password = self.code_signin.get()
        if username == '' or password == '':
            messagebox.showerror("Error", "All fields are required")
        else:
            messagebox.showinfo("Success", f"Welcome back, {username}!")

