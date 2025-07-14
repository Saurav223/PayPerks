import customtkinter as ctk
from tkinter import messagebox
from PIL import ImageTk, Image
from itertools import cycle


def run_auth_gui():
    ctk.set_appearance_mode("light")
    ctk.set_default_color_theme("blue")

    # Window setup
    window = ctk.CTk(fg_color="white")
    window.title('PayPerks Auth')
    window.geometry('925x500')
    window.resizable(False, False)
    def raise_frame(frame):
        frame.tkraise()

    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()
        if username == '' or password == '' or confirm_password == '':
            messagebox.showerror("Error", "All fields are required")
        elif password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
        else:
            messagebox.showinfo("Success", "Sign Up Successful")

    def signin():
        username = user_signin.get()
        password = code_signin.get()
        if username == '' or password == '':
            messagebox.showerror("Error", "All fields are required")
        else:
            messagebox.showinfo("Success", f"Welcome back, {username}!")
    # Loading images
    img = Image.open('img/PAYPERKS2.png').resize((250, 250))
    payperks_img = ImageTk.PhotoImage(img)
    ctk.CTkLabel(window, image=payperks_img, text="", bg_color='white').place(x=500, y=-40)

    bg_label = ctk.CTkLabel(window, text="", bg_color='white')
    bg_label.place(x=20, y=50)

    bg_images = ['img/bg.png', 'img/bg3.png']
    bg_index = [0]

    def load_bg(index):
        bg_img = Image.open(bg_images[index]).resize((400, 400))
        tk_img = ImageTk.PhotoImage(bg_img)
        bg_label.configure(image=tk_img)
        bg_label.image = tk_img

    load_bg(bg_index[0])
    # Typing effect
    typing_label = ctk.CTkLabel(window, text='', text_color='black', font=ctk.CTkFont("Segoe UI", 16, "bold"))
    typing_label.place(x=90, y=390)

    text_to_type = "Welcome to PayPerks!"
    def type_text(index=0):
        if index < len(text_to_type):
            typing_label.configure(text=typing_label.cget("text") + text_to_type[index])
            window.after(100, type_text, index + 1)
    type_text()

    words = cycle(["Secure. Simple. Smart Wallet.", "Your money, your control.", "Fast, safe & easy transactions."])
    is_animating = [False]

    def erase_text():
        is_animating[0] = True
        current = typing_label.cget("text")
        if current:
            typing_label.configure(text=current[:-1])
            window.after(50, erase_text)
        else:
            show_next_word()

    def show_next_word():
        word = next(words)
        typing_label.configure(text="")
        type_word(word)

    def type_word(word, index=0):
        if index < len(word):
            typing_label.configure(text=typing_label.cget("text") + word[index])
            window.after(150, type_word, word, index + 1)
        else:
            window.after(1200, erase_text)
    # Background sliding effect
    def slide_bg_out(x=10):
        if x > -400:
            bg_label.place(x=x, y=50)
            window.after(5, slide_bg_out, x - 10)
        else:
            swap_bg_image()

    def slide_bg_in(x=-400):
        if x < 10:
            bg_label.place(x=x, y=50)
            window.after(5, slide_bg_in, x + 10)
        else:
            window.after(100, lambda: is_animating.__setitem__(0, False))

    def swap_bg_image():
        bg_index[0] = (bg_index[0] + 1) % len(bg_images)
        load_bg(bg_index[0])
        slide_bg_in()
        erase_text()

    def swap_bg_and_animate():
        if not is_animating[0]:
            slide_bg_out()
            is_animating[0] = True
        window.after(5000, swap_bg_and_animate)

    window.after(5000, swap_bg_and_animate)
    # Frames for Sign Up and Sign In
    signup_frame = ctk.CTkFrame(window, width=450, height=360, fg_color='white')
    signin_frame = ctk.CTkFrame(window, width=450, height=360, fg_color='white')
    for frame in (signup_frame, signin_frame):
        frame.place(x=400, y=110)

    # --- Sign Up Form ---
    ctk.CTkLabel(signup_frame, text='Sign Up', text_color='#57a1f8', font=ctk.CTkFont(size=23, weight="bold")).place(x=25, y=10)

    name = ctk.CTkEntry(signup_frame, width=300, placeholder_text="Full Name")
    name.place(x=30, y=50)

    user = ctk.CTkEntry(signup_frame, width=300, placeholder_text="Username")
    user.place(x=30, y=90)

    code = ctk.CTkEntry(signup_frame, width=300, placeholder_text="Password", show="*")
    code.place(x=30, y=130)

    confirm_code = ctk.CTkEntry(signup_frame, width=300, placeholder_text="Confirm Password", show="*")
    confirm_code.place(x=30, y=170)

    email = ctk.CTkEntry(signup_frame, width=300, placeholder_text="Email")
    email.place(x=30, y=210)

    signup_btn = ctk.CTkButton(signup_frame, text="Sign Up", width=300, fg_color="#57a1f8", hover_color="#0052cc", command=signup)
    signup_btn.place(x=30, y=250)

    ctk.CTkLabel(signup_frame, text="I have an account?", text_color="black", font=ctk.CTkFont(size=11)).place(x=30, y=280)
    ctk.CTkButton(signup_frame,width=50, text="Sign In", fg_color="transparent", text_color="#57a1f8", hover=False, command=lambda: raise_frame(signin_frame)).place(x=130, y=280)

    # --- Sign In Form ---
    ctk.CTkLabel(signin_frame, text='Sign In', text_color='#57a1f8', font=ctk.CTkFont(size=23, weight="bold")).place(x=25, y=10)

    user_signin = ctk.CTkEntry(signin_frame, width=300, placeholder_text="Username")
    user_signin.place(x=30, y=60)

    code_signin = ctk.CTkEntry(signin_frame, width=300, placeholder_text="Password", show="*")
    code_signin.place(x=30, y=120)

    signin_btn = ctk.CTkButton(signin_frame, text="Sign In", width=300, fg_color="#57a1f8", hover_color="#0052cc", command=signin)
    signin_btn.place(x=30, y=180)

    ctk.CTkLabel(signin_frame, text="Don't have an account?", text_color="black", font=ctk.CTkFont(size=11)).place(x=30, y=230)
    ctk.CTkButton(signin_frame,width=50, text="Sign Up", fg_color="transparent", text_color="#57a1f8", hover=False, command=lambda: raise_frame(signup_frame)).place(x=145, y=230)

    raise_frame(signup_frame)
    window.mainloop()


if __name__ == '__main__':
    run_auth_gui()
