import webbrowser
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk

class Login_System:
    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.state("zoomed")
        self.bg_icon = ImageTk.PhotoImage(file=r"C:\Users\salim\AppData\Local\Programs\Python\Python313\sir login zach\bg1.jpg")
        self.user_icon = PhotoImage(file=r"C:\Users\salim\AppData\Local\Programs\Python\Python313\sir login zach\man-user.png")
        self.pass_icon = PhotoImage(file=r"C:\Users\salim\AppData\Local\Programs\Python\Python313\sir login zach\password.png")
        self.logo_icon = PhotoImage(file=r"C:\Users\salim\AppData\Local\Programs\Python\Python313\sir login zach\logo.png")
        self.uname = StringVar()
        self.pass_ = StringVar()
        self.users = {"martin": "123", "zac": "345", "thomas": "234"}
        self.current_booking = None
        bg_lbl = Label(self.root, image=self.bg_icon).pack()
        title = Label(self.root, text="Login System", font=("times new roman", 40, "bold"), bg="yellow", fg="red", bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)
        Login_Frame = Frame(self.root, bg="white")
        Login_Frame.place(x=400, y=150)
        logolbl = Label(Login_Frame, image=self.logo_icon, border=0)
        logolbl.grid(row=0, columnspan=2, pady=20)
        lbluser = Label(Login_Frame, text="Username", image=self.user_icon, compound=LEFT, font=("times new roman", 20, "bold"), bg="white")
        lbluser.grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(Login_Frame, bd=5, textvariable=self.uname, relief=GROOVE, font=(",15"))
        txtuser.grid(row=1, column=1, padx=20)
        lblpass = Label(Login_Frame, text="Password", image=self.pass_icon, compound=LEFT, font=("times new roman", 20, "bold"), bg="white")
        lblpass.grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(Login_Frame, bd=5, textvariable=self.pass_, relief=GROOVE, font=(",15"), show="*")
        txtpass.grid(row=2, column=1, padx=20)
        btn_log = Button(Login_Frame, text="Login", width=15, command=self.login, font=("times new roman", 14, "bold"), bg="yellow", fg="red")
        btn_log.grid(row=3, column=1, pady=10)

    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.uname.get() in self.users and self.users[self.uname.get()] == self.pass_.get():
            messagebox.showinfo("Successful", f"Welcome {self.uname.get()}")
            self.options_menu()
        else:
            messagebox.showerror("Error", "Invalid username or password")

    def options_menu(self):
        self.root.destroy()
        options_window = Tk()
        options_window.title("Options Menu")
        options_window.geometry("500x400")
        Label(options_window, text="Choose an Option", font=("times new roman", 20, "bold")).pack(pady=20)
        Button(options_window, text="Show Live Location", font=("times new roman", 14), command=self.get_location).pack(pady=10)
        Button(options_window, text="Book a Parking Spot", font=("times new roman", 14), command=lambda: self.book_parking(options_window)).pack(pady=10)
        Button(options_window, text="Change Booked Parking Spot", font=("times new roman", 14), command=lambda: self.change_parking(options_window)).pack(pady=10)
        Button(options_window, text="Cancel Parking Spot", font=("times new roman", 14), command=self.cancel_parking).pack(pady=10)
        options_window.mainloop()

    def get_location(self):
        lat = 10 + 31 / 60 + 19.9 / 3600
        lon = 76 + 13 / 60 + 39.8 / 3600
        messagebox.showinfo("Live Location", f"Latitude: {lat}, Longitude: {lon}")
        self.open_in_google_maps(lat, lon)

    def open_in_google_maps(self, latitude, longitude):
        url = f"https://www.google.com/maps?q={latitude},{longitude}"
        webbrowser.open(url)

    def book_parking(self, parent_window):
        dummy_parking_spots = [
            {"name": "Jubilee Mission Parking", "address": "Jubilee Rd", "type": "Paid", "slots": 5, "free_slots": 3},
            {"name": "Lourde Church Parking", "address": "Lourde Church St", "type": "Free", "slots": 10, "free_slots": 10},
            {"name": "Reliance Fresh Underground Parking", "address": "Reliance Mall, 101 Market", "type": "Paid", "slots": 15, "free_slots": 2},
            {"name": "Zudio Parking", "address": "Zudio Mall, 5th Avenue", "type": "Free", "slots": 20, "free_slots": 18}
        ]
        parking_window = Toplevel(parent_window)
        parking_window.title("Book Parking Spot")
        for index, spot in enumerate(dummy_parking_spots):
            name = spot["name"]
            address = spot["address"]
            free_slots = spot["free_slots"]
            Button(parking_window, text=f"{name} ({free_slots} slots free)", command=lambda n=name: self.confirm_booking(n)).pack(pady=5)

    def confirm_booking(self, parking_name):
        self.current_booking = parking_name
        messagebox.showinfo("Booking Confirmed", f"You have booked {parking_name}")

    def change_parking(self, parent_window):
        if not self.current_booking:
            messagebox.showerror("Error", "No parking spot is currently booked!")
            return
        self.book_parking(parent_window)

    def cancel_parking(self):
        if not self.current_booking:
            messagebox.showerror("Error", "No parking spot to cancel!")
        else:
            messagebox.showinfo("Cancelled", f"Your booking at {self.current_booking} has been cancelled.")
            self.current_booking = None


root = Tk()
obj = Login_System(root)
root.mainloop()
