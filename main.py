import tkinter as tk
from PIL import Image, ImageTk
import os
import json
import tkinter
import tkinter.messagebox
import customtkinter
import isUpdate as isUP

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Heritage Haven")
        self.geometry(f"{1200}x{600}")
        self.script_dir = os.path.dirname(os.path.abspath(__file__))
        self.image_path = os.path.join(self.script_dir, "img", "logo.png")
        self.iconpath = ImageTk.PhotoImage(file=self.image_path)
        self.wm_iconbitmap()
        self.iconphoto(False, self.iconpath)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=0, padx=(20, 0), pady=(0, 0))
        self.tabview.add("CTkTabview")
        self.tabview.add("Tab 2")
        self.tabview.add("Settings")
        self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)

        self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
                                                        values=["Value 1", "Value 2", "Value Long Long Long"])
        self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
        self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
                                                    values=["Value 1", "Value 2", "Value Long....."])
        self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
        self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
                                                           command=self.open_input_dialog_event)
        self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
        self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)
        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"), values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
        self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"), values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")

def read_json_file(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data

def notification(head,body):
    pass

def open_main_window():
    if(isUP.isAvailabe()):
        isUP.updateNotify()
    splash_root.destroy()
    app = App()
    app.mainloop()

def splashScreen():
    global splash_root
    splash_root = tk.Tk()

    # Get the screen dimensions
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()

    # Calculate the position to center the splash screen
    x_position = (screen_width - 562) // 2  # Adjust the width of the splash screen as needed
    y_position = (screen_height - 320) // 2  # Adjust the height of the splash screen as needed

    splash_root.overrideredirect(True)
    splash_root.geometry("562x320+{}+{}".format(x_position, y_position))

    # Construct the absolute path to the splash screen image using os.path.join()
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "img", "SplashScreen.png")
    splash_root.iconbitmap(os.path.join(script_dir, "img", "logo.png"))

    # Load the splash screen image using the absolute path
    splash_image = Image.open(image_path)
    splash_photo = ImageTk.PhotoImage(splash_image)

    splash_label = tk.Label(splash_root, image=splash_photo)
    splash_label.image = splash_photo
    splash_label.pack()

    #Fetch Info
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir,"manifest.json")
    json_data = read_json_file(file_path)
    # Add text label on top of the splash screen image
    labelN = tk.Label(splash_root, text=json_data["name"], font=("Helvetica", 40), fg="white", bg="#109595")
    labelN.place(x=6,y=20)
    #labelA = tk.Label(splash_root, text=f"Created by: {json_data['author']}", font=("Helvetica", 8), fg="white", bg="#109595")
    #labelA.place(x=10,y=74)
    labelA = tk.Label(splash_root, text="Created by: Sukarna Jana", font=("Helvetica", 8), fg="white", bg="#109595")
    labelA.place(x=10,y=74)
    labelV = tk.Label(splash_root, text=f"Version: {json_data['version']}V", font=("Helvetica", 8), fg="white", bg="#0F8A8A")
    labelV.place(x=5,y=298)

    splash_root.after(1000, open_main_window)

    splash_root.mainloop()

if __name__ == "__main__":
    splashScreen()
