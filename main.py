# Designed with https://visualtkinter.com - paste this file into File > Import there to edit it visually
# Requires CustomTkinter:  pip install customtkinter
import customtkinter as ctk
import tkinter as tk
# Requires Pillow:  pip install pillow
from PIL import Image


class Application:
    def __init__(self, root):
        self.root = root
        root.title("Main")
        root.geometry("1000x1000")
        root.update_idletasks()
        root.geometry(
            f"+{(root.winfo_screenwidth() - 1000) // 2}"
            f"+{(root.winfo_screenheight() - 1000) // 2}"
        )

        # Kept on self, or Python garbage-collects it and the image goes blank.
        self.BG1_png_image = ctk.CTkImage(Image.open("pngs/BG/BG1.png"), size=(980, 980))
        self.BG1_png = ctk.CTkLabel(root, text="", image=self.BG1_png_image)
        self.BG1_png.place(x=10, y=10, width=980, height=980)

        # Kept on self, or Python garbage-collects it and the image goes blank.
        self.Pot1_image = ctk.CTkImage(Image.open("image.png"), size=(520, 490))
        self.Pot1 = ctk.CTkLabel(root, text="", image=self.Pot1_image)
        self.Pot1.place(x=230, y=480, width=520, height=490)


if __name__ == "__main__":
    ctk.set_appearance_mode("light")
    root = ctk.CTk()
    app = Application(root)
    root.mainloop()