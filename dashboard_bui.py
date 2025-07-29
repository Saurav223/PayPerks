import customtkinter as ctk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image
import random

class PayPerksDashboard:
    def __init__(self):
        # Window setup
        ctk.set_appearance_mode("light")
        ctk.set_default_color_theme("blue")
        self.window = ctk.CTk(fg_color="white")
        self.window.title('PayPerks Dashboard')
        self.window.geometry('925x500')
        self.window.resizable(False, False)

        self.ACTIVE_COLOR = '#4899f0'
        self.INACTIVE_COLOR = '#1375d0'
        self.sidebar_buttons = {}
        self.button_font = ctk.CTkFont(family='Segoe UI', size=17, weight='bold')

        # Initialize frames
        self.dashboard_frame = ctk.CTkFrame(self.window, fg_color='white', width=725, height=500)
        self.transaction_frame = ctk.CTkFrame(self.window, fg_color='white', width=725, height=500)
        self.settings_frame = ctk.CTkScrollableFrame(self.window, fg_color='white', width=725, height=500)

        self.setup_sidebar()
        self.setup_dashboard()
        self.setup_transactions()
        self.setup_settings()
        
        # Show dashboard by default
        self.show_dashboard()

    def set_active(self, btn_name):
        for name, btn in self.sidebar_buttons.items():
            btn.configure(fg_color=self.ACTIVE_COLOR if name == btn_name else self.INACTIVE_COLOR)

    def show_dashboard(self):
        self.dashboard_frame.place(x=200, y=0)
        self.settings_frame.place_forget()
        self.transaction_frame.place_forget()
        self.set_active('dashboard')

    def show_transactions(self):
        self.transaction_frame.place(x=200, y=0)
        self.dashboard_frame.place_forget()
        self.settings_frame.place_forget()
        self.set_active('transactions')

    def show_settings(self):
        self.settings_frame.place(x=200, y=0)
        self.dashboard_frame.place_forget()
        self.transaction_frame.place_forget()
        self.set_active('settings')

    def setup_sidebar(self):
        sidebar = ctk.CTkFrame(self.window, fg_color='#1375d0', width=200, corner_radius=0)
        sidebar.pack(side='left', fill='y', padx=(0, 10))
        sidebar.pack_propagate(False)

        buttons = [
            ('Dashboard', self.show_dashboard, self.ACTIVE_COLOR),
            ('Transactions', self.show_transactions, self.INACTIVE_COLOR),
            ('Settings', self.show_settings, self.INACTIVE_COLOR)
        ]

        for name, command, color in buttons:
            btn = ctk.CTkButton(
                sidebar, text=name, font=self.button_font, height=40,
                fg_color=color, hover_color=self.ACTIVE_COLOR,
                text_color='white', corner_radius=8, command=command
            )
            btn.pack(fill='x', padx=20, pady=5)
            self.sidebar_buttons[name.lower()] = btn

    def setup_dashboard(self):
        # User icon
        user_img = ['img/user_icon/user1.png', 'img/user_icon/user2.png', 'img/user_icon/user3.png', 
                    'img/user_icon/user4.png', 'img/user_icon/user5.png']
        user_icon = ctk.CTkImage(light_image=Image.open(random.choice(user_img)), size=(50, 50))
        ctk.CTkLabel(self.dashboard_frame, image=user_icon, text="").place(x=20, y=50)

        # Welcome label
        ctk.CTkLabel(self.dashboard_frame, text="Welcome! Saurav Subedi", 
                    font=ctk.CTkFont(size=20, weight="bold")).place(x=80, y=65)

        # PayPerks Logo
        logo_img = ctk.CTkImage(light_image=Image.open('img/PAYPERKS2.png'), size=(250, 250))
        ctk.CTkLabel(self.dashboard_frame, image=logo_img, text="").place(x=400, y=-50)

        # Card configurations
        cards = [
            ("Balance", "$1000.00", 360, 150),
            ("Income", "$500.00", 360, 250),
            ("Expense", "$300.00", 360, 350),
            ("Reward Points", "200.00", 20, 150)
        ]

        for title, amount, x, y in cards:
            card = ctk.CTkFrame(self.dashboard_frame, width=300, height=80, fg_color='white', 
                              border_color='#e0e1e2', border_width=2, corner_radius=10)
            card.place(x=x, y=y)
            ctk.CTkLabel(card, text=title, font=ctk.CTkFont(size=15, weight="bold"), 
                        text_color='#1375d0', bg_color='transparent').place(x=20, y=5)
            ctk.CTkLabel(card, text=amount, font=ctk.CTkFont(size=28, weight="bold"), 
                        text_color='#222', bg_color='transparent').place(x=20, y=30)

        # Recent activity
        recent_activity_card = ctk.CTkFrame(self.dashboard_frame, width=300, height=220, 
                                          fg_color='white', border_color='#e0e1e2', 
                                          border_width=2, corner_radius=10)
        recent_activity_card.place(x=20, y=250)
        ctk.CTkLabel(recent_activity_card, text="Recent Activity", 
                    font=ctk.CTkFont(size=15, weight="bold"), 
                    text_color='#1375d0', bg_color='transparent').place(x=20, y=5)

        # Matplotlib graph
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

    def change_password(self):
        popup = ctk.CTkToplevel(self.window)
        popup.title("Change Password")
        popup.geometry("400x400")
        popup.resizable(False, False)
        popup.lift()
        popup.focus_force()
        popup.grab_set()

        ctk.CTkLabel(popup, text="Change Password", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)
        
        labels = ["Current Password:", "New Password:", "Confirm New Password:"]
        entries = []
        for label in labels:
            ctk.CTkLabel(popup, text=label).pack(pady=5)
            entry = ctk.CTkEntry(popup, width=300, show="*")
            entry.pack(pady=5)
            entries.append(entry)

        def submit_change():
            current_password, new_password, confirm_password = [entry.get() for entry in entries]
            if new_password == confirm_password:
                print("Password changed successfully!")
                popup.destroy()
            else:
                print("Passwords do not match!")  # Note: CTkMessageBox not available in standard customtkinter

        ctk.CTkButton(popup, text="Submit", command=submit_change).pack(pady=20)

    def setup_settings(self):
        # Profile Section
        profile_frame = ctk.CTkFrame(self.settings_frame, fg_color='white', 
                                   border_color='#e0e1e2', border_width=2, corner_radius=10)
        profile_frame.pack(pady=10, padx=10, fill='x')
        
        ctk.CTkLabel(profile_frame, text="Profile Settings", 
                    font=ctk.CTkFont(size=20, weight="bold"), text_color='#1375d0').pack(anchor='w', padx=20, pady=(10, 5))

        profile_data = [("Full Name:", "John Doe"), ("Username:", "johndoe123"), ("Email:", "johndoe123@gmail.com")]
        for label_text, value in profile_data:
            ctk.CTkLabel(profile_frame, text=label_text, font=ctk.CTkFont(size=16), 
                        text_color='#222').pack(anchor='w', padx=20)
            frame = ctk.CTkFrame(profile_frame, height=35, border_color='#e0e1e2', 
                               border_width=1, corner_radius=5, fg_color='white')
            frame.pack(padx=20, pady=(0, 10), fill='x')
            ctk.CTkLabel(frame, text=value, font=ctk.CTkFont(size=18), 
                        text_color='#222').pack(anchor='w', padx=10, pady=5)

        # Security Section
        security_frame = ctk.CTkFrame(self.settings_frame, fg_color='white', 
                                    border_color='#e0e1e2', border_width=2, corner_radius=10)
        security_frame.pack(pady=10, padx=10, fill='x')
        ctk.CTkLabel(security_frame, text="Security Settings", 
                    font=ctk.CTkFont(size=20, weight="bold"), 
                    text_color='#1375d0').pack(anchor='w', padx=20, pady=(10, 5))
        ctk.CTkButton(security_frame, text="Change Password", font=ctk.CTkFont(size=16),
                     width=200, height=40, fg_color='#4899f0', hover_color='#0052cc',
                     command=self.change_password).pack(padx=20, pady=(10, 20), anchor='w')

        # Notifications Section
        notifications_frame = ctk.CTkFrame(self.settings_frame, fg_color='white', 
                                         border_color='#e0e1e2', border_width=2, corner_radius=10)
        notifications_frame.pack(pady=10, padx=10, fill='x')
        ctk.CTkLabel(notifications_frame, text="Notification Settings", 
                    font=ctk.CTkFont(size=20, weight="bold"), 
                    text_color='#1375d0').pack(anchor='w', padx=20, pady=(10, 5))
        ctk.CTkSwitch(notifications_frame, text="Enable Email Notifications", 
                     font=ctk.CTkFont(size=16), 
                     command=lambda: print("Notifications toggled")).pack(anchor='w', padx=20, pady=(0, 10))

        # Support Section
        support_frame = ctk.CTkFrame(self.settings_frame, fg_color='white', 
                                   border_color='#e0e1e2', border_width=2, corner_radius=10)
        support_frame.pack(pady=10, padx=10, fill='x')
        ctk.CTkLabel(support_frame, text="Support and Feedback", 
                    font=ctk.CTkFont(size=20, weight="bold"), 
                    text_color='#1375d0').pack(anchor='w', padx=20, pady=(10, 5))
        ctk.CTkLabel(support_frame, text="For any issues or feedback, please contact us at").pack(anchor='w', padx=20, pady=(0, 10))
        ctk.CTkButton(support_frame, text="Contact Support", font=ctk.CTkFont(size=16),
                     width=200, height=40, fg_color='#4899f0', hover_color='#0052cc',
                     command=lambda: print("Contact Support Clicked")).pack(padx=20, pady=(0, 10), anchor='w')

    def send_function(self):
        print("Send Money Function Triggered")

    def setup_transactions(self):
        ctk.CTkLabel(self.transaction_frame, text="Transactions", 
                    font=ctk.CTkFont(family='Segoe UI', size=45, weight="bold"), 
                    text_color='#1375d0').place(x=80, y=65)

        logo_img = ctk.CTkImage(light_image=Image.open('img/PAYPERKS2.png'), size=(250, 250))
        ctk.CTkLabel(self.transaction_frame, image=logo_img, text="").place(x=400, y=-50)

        buttons = [
            ("Send Money", 'img/icon/send.png', 210, 150, 150),
            ("Load Money", 'img/icon/load.png', 20, 150, 150),
            ("Transaction History", 'img/icon/transaction.png', 20, 425, 150),
            ("Redeem Rewards Points", 'img/icon/token.png', 400, 150, 180),
            ("TopUp Mobile", 'img/icon/topup.png', 20, 275, 150),
            ("Electricity Bill", 'img/icon/electricity.png', 210, 275, 150),
            ("Internet Bill", 'img/icon/internet.png', 400, 275, 150),
            ("Water Bill", 'img/icon/water.png', 20, 350, 150),
            ("Education Fee", 'img/icon/education.png', 210, 350, 150),
            ("Healthcare Payment", 'img/icon/health.png', 400, 350, 180)
        ]

        for text, icon_path, x, y, width in buttons:
            icon = ctk.CTkImage(light_image=Image.open(icon_path), size=(40, 40))
            ctk.CTkButton(
                self.transaction_frame, text=text, font=ctk.CTkFont(size=14, weight="bold"),
                text_color='black', image=icon, compound="left", command=self.send_function,
                fg_color='white', hover_color='#e0e1e2', width=width, height=50,
                border_color='#e0e1e2', border_width=1, corner_radius=10
            ).place(x=x, y=y)

        ctk.CTkLabel(self.transaction_frame, text="Utility & Bill Payments", 
                    font=ctk.CTkFont(family='Segoe UI', size=20, weight="bold"), 
                    text_color='#1375d0').place(x=20, y=225)

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = PayPerksDashboard()
    app.run()