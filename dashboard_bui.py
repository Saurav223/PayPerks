import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import random

# Window setup
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")
window = ctk.CTk(fg_color="white")
window.title('PayPerks Dashboard')
window.geometry('925x500')
window.resizable(False, False)

# Function
def show_dashboard():
    dashboard_frame.place(x=200, y=0)
    settings_frame.place_forget()

def show_transactions():
    print("Transactions shown")

def show_settings():
    settings_frame.place(x=200, y=0)
    dashboard_frame.place_forget()


# Sidebar
sidebar = ctk.CTkFrame(window, fg_color='#1375d0', width=200,corner_radius=0)
sidebar.pack(side='left', fill='y', padx=(0, 10))
sidebar.pack_propagate(False)
button_font = ctk.CTkFont(family='Segoe UI', size=18, weight='bold')
sidebar_buttons = {}
ACTIVE_COLOR = '#4899f0'
INACTIVE_COLOR = '#1375d0'

def set_active(btn_name):
    for name, btn in sidebar_buttons.items():
        if name == btn_name:
            btn.configure(fg_color=ACTIVE_COLOR)
        else:
            btn.configure(fg_color=INACTIVE_COLOR)

def dashboard_clicked():
    set_active('dashboard')
    show_dashboard()

def transactions_clicked():
    set_active('transactions')
    show_transactions()

def settings_clicked():
    set_active('settings')
    show_settings()

# Dashboard Button
dashboard_btn = ctk.CTkButton(sidebar, text='Dashboard', font=button_font,height=40, 
                              fg_color=ACTIVE_COLOR, hover_color=ACTIVE_COLOR,
                              text_color='white', corner_radius=8,
                              command=dashboard_clicked)
dashboard_btn.pack(fill='x', padx=20, pady=(20, 5))
sidebar_buttons['dashboard'] = dashboard_btn

# Transactions Button
transactions_btn = ctk.CTkButton(sidebar, text='Transactions', font=button_font,height=40,
                                 fg_color=INACTIVE_COLOR, hover_color=ACTIVE_COLOR,
                                 text_color='white', corner_radius=8,
                                 command=transactions_clicked)
transactions_btn.pack(fill='x', padx=20, pady=5)
sidebar_buttons['transactions'] = transactions_btn

# Settings Button
settings_btn = ctk.CTkButton(sidebar, text='Settings', font=button_font,height=40,
                             fg_color=INACTIVE_COLOR, hover_color=ACTIVE_COLOR,
                             text_color='white', corner_radius=8,
                             command=settings_clicked)
settings_btn.pack(fill='x', padx=20, pady=5)
sidebar_buttons['settings'] = settings_btn



# Dashboard Frame
dashboard_frame = ctk.CTkFrame(window, fg_color='white', width=725, height=500)
dashboard_frame.place(x=200, y=0)
Label = ctk.CTkLabel(dashboard_frame, text="Welcome! user name", font=ctk.CTkFont(size=20, weight="bold"))
Label.place(x=80, y=65)
# User Icon
user_img = ['img/user_icon/user1.png', 'img/user_icon/user2.png', 'img/user_icon/user3.png', 'img/user_icon/user4.png', 'img/user_icon/user5.png']
random_user_img = random.choice(user_img)
user_icon = ctk.CTkImage(light_image=Image.open(random_user_img),size=(50, 50))
user_icon_label = ctk.CTkLabel(dashboard_frame, image=user_icon, text="")
user_icon_label.place(x=20, y=50)
# PayPerks Logo
logo_img = ctk.CTkImage(light_image=Image.open('img/PAYPERKS2.png'), size=(250, 250))
logo_label = ctk.CTkLabel(dashboard_frame, image=logo_img, text="")
logo_label.place(x=400, y=-50)

# Balance Frame and Labels
balance_card = ctk.CTkFrame(dashboard_frame, width=300, height=80, fg_color='white', border_color='#e0e1e2', border_width=2, corner_radius=10)
balance_card.place(x=360, y=150)
balance_text_label = ctk.CTkLabel(balance_card, text="Balance", font=ctk.CTkFont(size=15, weight="bold"), text_color='#1375d0', bg_color='transparent')
balance_text_label.place(x=20, y=5)
amount_label = ctk.CTkLabel(balance_card, text="$1000.00", font=ctk.CTkFont(size=28, weight="bold"), text_color='#222', bg_color='transparent')
amount_label.place(x=20, y=30)

# INcome frame and Labels
income_card = ctk.CTkFrame(dashboard_frame, width=300, height=80, fg_color='white', border_color='#e0e1e2', border_width=2, corner_radius=10)
income_card.place(x=360, y=250)
income_text_label = ctk.CTkLabel(income_card, text="Income", font=ctk.CTkFont(size=15, weight="bold"), text_color='#1375d0', bg_color='transparent')
income_text_label.place(x=20, y=5)  
income_amount_label = ctk.CTkLabel(income_card, text="$500.00", font=ctk.CTkFont(size=28, weight="bold"), text_color='#222', bg_color='transparent')
income_amount_label.place(x=20, y=30)

# Expense frame and Labels
expense_card = ctk.CTkFrame(dashboard_frame, width=300, height=80, fg_color='white', border_color='#e0e1e2', border_width=2, corner_radius=10)
expense_card.place(x=360, y=350)    
expense_text_label = ctk.CTkLabel(expense_card, text="Expense", font=ctk.CTkFont(size=15, weight="bold"), text_color='#1375d0', bg_color='transparent')
expense_text_label.place(x=20, y=5) 
expense_amount_label = ctk.CTkLabel(expense_card, text="$300.00", font=ctk.CTkFont(size=28, weight="bold"), text_color='#222', bg_color='transparent')
expense_amount_label.place(x=20, y=30)

# Reward frame and Labels
reward_card = ctk.CTkFrame(dashboard_frame, width=300, height=80, fg_color='white', border_color='#e0e1e2', border_width=2, corner_radius=10)
reward_card.place(x=20, y=150)
reward_text_label = ctk.CTkLabel(reward_card, text="Reward Points", font=ctk.CTkFont(size=15, weight="bold"), text_color='#1375d0', bg_color='transparent')
reward_text_label.place(x=20, y=5)  
reward_amount_label = ctk.CTkLabel(reward_card, text="200.00", font=ctk.CTkFont(size=28, weight="bold"), text_color='#222', bg_color='transparent')
reward_amount_label.place(x=20, y=30)


# Recent activity frame and Labels
recent_activity_card = ctk.CTkFrame(dashboard_frame, width=300, height=220, fg_color='white', border_color='#e0e1e2', border_width=2, corner_radius=10)
recent_activity_card.place(x=20, y=250)
recent_activity_label = ctk.CTkLabel(recent_activity_card, text="Recent Activity", font=ctk.CTkFont(size=15, weight="bold"), text_color='#1375d0', bg_color='transparent')
recent_activity_label.place(x=20, y=5)

# --- matplotlib graph ---
fig = Figure(figsize=(3.6, 2.3), dpi=100)
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4, 5], [1000, 2000, 1500, 2500, 1000], marker='o', color='#4899f0')
ax.set_xlabel('Day', fontsize=8)
ax.set_ylabel('Amount', fontsize=8)
ax.tick_params(axis='both', labelsize=8)
fig.tight_layout(pad=1)

canvas = FigureCanvasTkAgg(fig, master=recent_activity_card)
canvas.draw()
canvas.get_tk_widget().place(x=10, y=35)

# Setting Functions
def change_password():
    popup = ctk.CTkToplevel(window)
    popup.title("Change Password")
    popup.geometry("400x400")
    popup.resizable(False, False)
    popup.lift()
    popup.focus_force()
    popup.grab_set()
    # labels and entries
    ctk.CTkLabel(popup, text="Change Password", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
    ctk.CTkLabel(popup, text="Current Password:").pack(pady=5)
    current_password_entry = ctk.CTkEntry(popup, width=300, show="*")
    current_password_entry.pack(pady=5)
    ctk.CTkLabel(popup, text="New Password:").pack(pady=5)
    new_password_entry = ctk.CTkEntry(popup, width=300, show="*")
    new_password_entry.pack(pady=5)
    ctk.CTkLabel(popup, text="Confirm New Password:").pack(pady=5)
    confirm_password_entry = ctk.CTkEntry(popup, width=300, show="*")
    confirm_password_entry.pack(pady=5)
    def submit_change():
        current_password = current_password_entry.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()
        if new_password == confirm_password:
            # Here you would add logic to change the password
            print("Password changed successfully!")
            popup.destroy()
        else:
            ctk.CTkMessageBox.show_error("Passwords do not match!")
    submit_btn = ctk.CTkButton(popup, text="Submit", command=submit_change)
    submit_btn.pack(pady=20)
    



# --- Setting Frame ---
settings_frame = ctk.CTkScrollableFrame(window, fg_color='white', width=725, height=500)
settings_frame.place(x=200, y=0)

### ---- Profile Section ---- ###
profile_frame = ctk.CTkFrame(settings_frame, fg_color='white', border_color='#e0e1e2', border_width=2, corner_radius=10)
profile_frame.pack(pady=10, padx=10, fill='x')

profile_label = ctk.CTkLabel(profile_frame, text="Profile Settings", font=ctk.CTkFont(size=20, weight="bold"), text_color='#1375d0')
profile_label.pack(anchor='w', padx=20, pady=(10, 5))

# Full Name
full_name_label = ctk.CTkLabel(profile_frame, text="Full Name:", font=ctk.CTkFont(size=16), text_color='#222')
full_name_label.pack(anchor='w', padx=20)

name_label_frame = ctk.CTkFrame(profile_frame, height=35, border_color='#e0e1e2', border_width=1, corner_radius=5, fg_color='white')
name_label_frame.pack(padx=20, pady=(0, 10), fill='x')
name_label = ctk.CTkLabel(name_label_frame, text="John Doe", font=ctk.CTkFont(size=18), text_color='#222')
name_label.pack(anchor='w', padx=10, pady=5)

# Username
username_label = ctk.CTkLabel(profile_frame, text="Username:", font=ctk.CTkFont(size=16), text_color='#222')
username_label.pack(anchor='w', padx=20)

username_label_frame = ctk.CTkFrame(profile_frame, height=35, border_color='#e0e1e2', border_width=1, corner_radius=5, fg_color='white')
username_label_frame.pack(padx=20, pady=(0, 10), fill='x')
username_label = ctk.CTkLabel(username_label_frame, text="johndoe123", font=ctk.CTkFont(size=18), text_color='#222')
username_label.pack(anchor='w', padx=10, pady=5)

# Email
email_label = ctk.CTkLabel(profile_frame, text="Email:", font=ctk.CTkFont(size=16), text_color='#222')
email_label.pack(anchor='w', padx=20)

email_label_frame = ctk.CTkFrame(profile_frame, height=35, border_color='#e0e1e2', border_width=1, corner_radius=5, fg_color='white')
email_label_frame.pack(padx=20, pady=(0, 10), fill='x')
email_label = ctk.CTkLabel(email_label_frame, text="johndoe123@gmail.com", font=ctk.CTkFont(size=18), text_color='#222')
email_label.pack(anchor='w', padx=10, pady=5)

### ---- Security Section ---- ###
security_frame = ctk.CTkFrame(settings_frame, fg_color='white', border_color='#e0e1e2', border_width=2, corner_radius=10)
security_frame.pack(pady=10, padx=10, fill='x')

security_label = ctk.CTkLabel(security_frame, text="Security Settings", font=ctk.CTkFont(size=20, weight="bold"), text_color='#1375d0')
security_label.pack(anchor='w', padx=20, pady=(10, 5))

change_password_btn = ctk.CTkButton(security_frame, text="Change Password", font=ctk.CTkFont(size=16),
                                     width=200, height=40, fg_color='#4899f0', hover_color='#0052cc',
                                     command=change_password)
change_password_btn.pack(padx=20, pady=(10, 20), anchor='w')

# Notifications 
notifications_frame = ctk.CTkFrame(settings_frame, fg_color='white', border_color='#e0e1e2', border_width=2, corner_radius=10)
notifications_frame.pack(pady=10, padx=10, fill='x')    
notifications_label = ctk.CTkLabel(notifications_frame, text="Notification Settings", font=ctk.CTkFont(size=20, weight="bold"), text_color='#1375d0')
notifications_label.pack(anchor='w', padx=20, pady=(10, 5))
# Add a toggle switch for notifications
notifications_switch = ctk.CTkSwitch(notifications_frame, text="Enable Email Notifications", font=ctk.CTkFont(size=16), 
                                        command=lambda: print("Notifications toggled"))
notifications_switch.pack(anchor='w', padx=20, pady=(0, 10))

# Support and Feedback
support_frame = ctk.CTkFrame(settings_frame, fg_color='white', border_color='#e0e1e2', border_width=2, corner_radius=10)
support_frame.pack(pady=10, padx=10, fill='x')
support_label = ctk.CTkLabel(support_frame, text="Support and Feedback", font=ctk.CTkFont(size=20, weight="bold"), text_color='#1375d0')
support_label.pack(anchor='w', padx=20, pady=(10, 5))
support_text = ctk.CTkLabel(support_frame, text="For any issues or feedback, please contact us at")
support_text.pack(anchor='w', padx=20, pady=(0, 10))
# Add a contact button
contact_btn = ctk.CTkButton(support_frame, text="Contact Support", font=ctk.CTkFont(size=16),
                             width=200, height=40, fg_color='#4899f0', hover_color='#0052cc',
                             command=lambda: print("Contact Support Clicked"))
contact_btn.pack(padx=20, pady=(0, 10), anchor='w')






# Show dashboard by default
dashboard_frame.tkraise()
window.mainloop()
