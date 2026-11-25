# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
# Requires CustomTkinter:  pip install customtkinter
import customtkinter as ctk
import tkinter as tk
# Requires tkcalendar:  pip install tkcalendar
from tkcalendar import DateEntry
from database import new_entry
from database import get_daily_total
from datetime import date  


class Main:
    def __init__(self, root):
        self.root = root
        root.title("Main")
        root.geometry("1000x1000")
        root.update_idletasks()
        root.geometry(
            f"+{(root.winfo_screenwidth() - 1000) // 2}"
            f"+{(root.winfo_screenheight() - 1000) // 2}"
        )
# gui 
        self.BG1 = ctk.CTkLabel(root, text="BG1", width=1000, height=1000)
        self.BG1.place(x=0, y=0)

        self.Pot1 = ctk.CTkLabel(root, text="Pot1", width=430, height=360)
        self.Pot1.place(x=285, y=410)

        self.Seed1 = ctk.CTkLabel(root, text="seed1", width=340, height=290)
        self.Seed1.place(x=330, y=320)

        self.water_plant = ctk.CTkButton(root, text="Water Plant", command=self.on_water_plant, width=170, height=60)
        self.water_plant.place(x=657, y=470)

        self.History = ctk.CTkButton(root, text="History ", command=self.on_History, width=200, height=70)
        self.History.place(x=20, y=20)

        self.Calendar = ctk.CTkButton(root, text="Calendar ", command=self.on_Calendar, width=180, height=70)
        self.Calendar.place(x=240, y=20)

        self.Customize = ctk.CTkButton(root, text="Customize ", command=self.on_Customize, width=220, height=70)
        self.Customize.place(x=760, y=20)

        self.Achievements = ctk.CTkButton(root, text="Achievements", command=self.on_Achievements, width=280, height=80)
        self.Achievements.place(x=30, y=730)

        self.progressbar2 = ctk.CTkProgressBar(root, orientation="vertical", mode="determinate", width=481, height=90)
        self.progressbar2.set(0)
        self.progressbar2.place(x=261, y=610)

        self.Water_Amount = ctk.CTkLabel(root, text="Water_Amount", width=210, height=70)
        self.Water_Amount.place(x=395, y=220)

    def update_water_total(self):
        today = date.today().isoformat()
        water_total = get_daily_total(today)
        self.Water_Amount.configure(
        text=f"Amount Watered: {water_total} ozs"
        )


# Daily water tracking: 
        today = date.today().isoformat()
        water_total = get_daily_total(today)

        self.Water_Amount = ctk.CTkLabel(
            root,
            text=f"Amount Watered: {water_total} ozs",
            width=210,
            height=70,
        )
        self.Water_Amount.place(x=395, y=220)

# Buttons      

    def open_water_plant(self):
        return WaterPlant(self.root)

    def on_water_plant(self):
        print("button clicked")
        WaterPlant(self.root, self) 
        pass



    def on_History(self):
        pass

    def on_Calendar(self):
        pass

    def on_Customize(self):
        pass

    def on_Achievements(self):
        pass

    

 # Watering plant popup: 
class WaterPlant:
    def __init__(self, master, main_window):
        root = ctk.CTkToplevel(master)
        self.root = root
        root.title("Water_Plant")
        root.geometry("520x380")

        self.label1 = ctk.CTkLabel(root, text="", fg_color="#95afd0", width=520, height=380)
        self.label1.place(x=0, y=0)

        self.label2 = ctk.CTkLabel(root, text="How much water did you drink? ", width=250, height=50)
        self.label2.place(x=0, y=20)

        self.label3 = ctk.CTkLabel(root, text="Cups:", width=90, height=26)
        self.label3.place(x=10, y=70)

        self.entry1 = ctk.CTkEntry(root, width=150, height=28)
        self.entry1.place(x=80, y=68)

        self.label4 = ctk.CTkLabel(root, text="Ozs:", width=90, height=26)
        self.label4.place(x=10, y=120)

        self.entry2 = ctk.CTkEntry(root, width=150, height=28)
        self.entry2.place(x=80, y=118)

        self.dateentry1 = DateEntry(root, date_pattern="yyyy-mm-dd")
        self.dateentry1.place(x=120, y=240, width=160, height=40)

        self.entry3 = ctk.CTkEntry(root, width=150, height=28)
        self.entry3.place(x=100, y=248)

        self.label5 = ctk.CTkLabel(root, text="Time:", width=90, height=30)
        self.label5.place(x=0, y=248)

        self.Date_label = ctk.CTkLabel(root, text="Date", width=90, height=26)
        self.Date_label.place(x=0, y=197)

        self.Save_button = ctk.CTkButton(
                            root,
                            text="Save",
                            command=self.save_entry 
                        )
        self.Save_button.place(x=170, y=280)

        self.main_window = main_window

    def save_entry(self):
        try:
            cups = int(self.entry1.get())
            ozs = float(self.entry2.get())
            date = self.dateentry1.get()
            entry_time = (self.entry3.get())
        
            new_entry(
                date=date,
                entry_time=entry_time,
                water_ozs=ozs,
                water_cups=cups
            )
            self.main_window.update_water_total()
            self.root.destroy()
        
        except ValueError:
            print("Inavalid input")

   


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    app = Main(root)
    root.mainloop()

