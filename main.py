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
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # create tabview
        self.tabview = customtkinter.CTkTabview(self)
        self.tabview.grid(row=0, column=0, padx=0, pady=0, sticky="nsew")
        self.tabview.add("Kaval Master")
        self.tabview.add("Tab 2")
        self.tabview.add("Settings")
        self.tabview.tab("Kaval Master").grid_columnconfigure(0, weight=1) 
        self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)

        # new entry dilog box part
        self.addNew_frame = customtkinter.CTkFrame(self.tabview.tab("Kaval Master"))
        self.addNew_frame.grid(row=0, column=0, padx=(20, 20), pady=(10, 10),sticky="nsew")

        self.enterId_label_inNew = customtkinter.CTkLabel(self.addNew_frame, text="Enter ID")
        self.enterId_label_inNew.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))
        self.enter_id_inNew = customtkinter.CTkEntry(self.addNew_frame, placeholder_text="1909")
        self.enter_id_inNew.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        self.enterName_label_inNew = customtkinter.CTkLabel(self.addNew_frame, text="Enter Name")
        self.enterName_label_inNew.grid(row=1, column=0, padx=(20, 20), pady=(20, 20))
        self.enter_Name_inNew = customtkinter.CTkEntry(self.addNew_frame, placeholder_text="Kaval xx")
        self.enter_Name_inNew.grid(row=1, column=1, padx=(20, 20), pady=(20, 20))

        self.enterNew_inNew = customtkinter.CTkButton(self.addNew_frame, text="Add into Database",
                                                           command=self.open_input_dialog_event)
        self.enterNew_inNew.grid(row=2, column=0, columnspan=2, padx=(20, 20), pady=(20, 20))

        # edit option dilog box
        self.editDB_frame = customtkinter.CTkFrame(self.tabview.tab("Kaval Master"))
        self.editDB_frame.grid(row=0, column=1, padx=(20, 20), pady=(10, 10),sticky="nsew")

        self.enterId_label_inEdit = customtkinter.CTkLabel(self.editDB_frame, text="Enter ID")
        self.enterId_label_inEdit.grid(row=0, column=0, padx=(20, 20), pady=(20, 20))
        self.enter_id_inEdit = customtkinter.CTkEntry(self.editDB_frame, placeholder_text="1909")
        self.enter_id_inEdit.grid(row=0, column=1, padx=(20, 20), pady=(20, 20))

        self.enter_newName_label_inEdit = customtkinter.CTkLabel(self.editDB_frame, text="Enter New Name")
        self.enter_newName_label_inEdit.grid(row=1, column=0, padx=(20, 20), pady=(20, 20))
        self.enter_newName_inEdit = customtkinter.CTkEntry(self.editDB_frame, placeholder_text="Suku...")
        self.enter_newName_inEdit.grid(row=1, column=1, padx=(20, 20), pady=(20, 20))

        self.enter_newNameCof_label_inEdit = customtkinter.CTkLabel(self.editDB_frame, text="Conform New Name")
        self.enter_newNameCof_label_inEdit.grid(row=2, column=0, padx=(20, 20), pady=(20, 20))
        self.enter_newNameCof_inEdit = customtkinter.CTkEntry(self.editDB_frame, placeholder_text="Suku...")
        self.enter_newNameCof_inEdit.grid(row=2, column=1, padx=(20, 20), pady=(20, 20))

        self.editBtn_inEdit = customtkinter.CTkButton(self.editDB_frame, text="Save the changes",
                                                           command=self.open_input_dialog_event)
        self.editBtn_inEdit.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 20))

        # Just Label to view Tabel
        self.labelkm_frame = customtkinter.CTkFrame(self.tabview.tab("Kaval Master"), fg_color="transparent")
        self.labelkm_frame.grid(row=2, column=0, padx=(0, 0), pady=(10, 10), sticky="nsew")
        self.label_inKMlabel = customtkinter.CTkLabel(self.labelkm_frame, text="Database View Point")
        self.label_inKMlabel.grid(row=0, column=0, columnspan=2, padx=(5, 5), pady=(5, 5),sticky="nsew")

        # view Tabel
        self.viewTabel_km_frame = customtkinter.CTkFrame(self.tabview.tab("Kaval Master"))
        self.viewTabel_km_frame.grid(row=3, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")


        self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="Need to write code still")
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
