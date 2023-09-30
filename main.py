import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import json
import tkinter
import tkinter.messagebox
import customtkinter
import isUpdate as isUP
from tksheet import Sheet
import mysql.connector

from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from datetime import datetime
from tkinter import messagebox
import webbrowser

customtkinter.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"

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
        self.tabview.add("Surname Master")
        self.tabview.add("Settings")
        #self.tabview.tab("Kaval Master").grid_columnconfigure(0, weight=1) 
        #self.tabview.tab("Surname Master").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)

        self.tabview.tab("Kaval Master").rowconfigure(3, weight=1)
        self.tabview.tab("Kaval Master").columnconfigure(0, weight=1)
        self.tabview.tab("Kaval Master").columnconfigure(1, weight=1)

        self.tabview.tab("Surname Master").rowconfigure(3, weight=1)
        self.tabview.tab("Surname Master").columnconfigure(0, weight=1)
        self.tabview.tab("Surname Master").columnconfigure(1, weight=1)

        # BEGAIN OF TAB 1 NAMED : Kaval Master

        # new entry dilog box part
        self.addNew_frame = customtkinter.CTkFrame(self.tabview.tab("Kaval Master"))
        self.addNew_frame.grid(row=0, column=0, padx=(0, 5), pady=(10, 10),sticky="nsew")

        self.head_label_inNew = customtkinter.CTkLabel(self.addNew_frame, text="Add Data in Database")
        self.head_label_inNew.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=(10, 10))

        self.enterId_label_inNew = customtkinter.CTkLabel(self.addNew_frame, text="Enter ID")
        self.enterId_label_inNew.grid(row=1, column=0, padx=(20, 20), pady=(5, 5))
        self.enter_id_inNew = customtkinter.CTkEntry(self.addNew_frame, placeholder_text="1909")
        self.enter_id_inNew.grid(row=1, column=1, padx=(20, 20), pady=(5, 5))

        self.enterName_label_inNew = customtkinter.CTkLabel(self.addNew_frame, text="Enter Name")
        self.enterName_label_inNew.grid(row=2, column=0, padx=(20, 20), pady=(5, 5))
        self.enter_Name_inNew = customtkinter.CTkEntry(self.addNew_frame, placeholder_text="Kaval xx")
        self.enter_Name_inNew.grid(row=2, column=1, padx=(20, 20), pady=(5, 10))

        self.enterNew_inNew = customtkinter.CTkButton(self.addNew_frame, text="Add into Database",
                                                           command=self.add_to_the_kaval_master)
        self.enterNew_inNew.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(10, 20))

        # find option dilog box
        self.findDB_frame = customtkinter.CTkFrame(self.tabview.tab("Kaval Master"))
        self.findDB_frame.grid(row=0, column=1, padx=(5, 0), pady=(10, 10),sticky="nsew")

        self.head_label_inFind = customtkinter.CTkLabel(self.findDB_frame, text="Scearch in Database")
        self.head_label_inFind.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=(10, 10))
        self.findBy_inEdit_Label = customtkinter.CTkLabel(self.findDB_frame, text="Find By", anchor="w")
        self.findBy_inEdit_Label.grid(row=1, column=0, padx=20, pady=(5, 5))
        self.findBy_inEdit_optionemenu = customtkinter.CTkOptionMenu(self.findDB_frame, values=["Kaval ID", "Kaval Name", "SNo."])
        self.findBy_inEdit_optionemenu.grid(row=1, column=1, padx=20, pady=(5, 5))
        self.data_label_inFind = customtkinter.CTkLabel(self.findDB_frame, text="Enter Respective Data")
        self.data_label_inFind.grid(row=2, column=0, padx=(20, 20), pady=(5, 5))
        self.enter_data_inFind = customtkinter.CTkEntry(self.findDB_frame, placeholder_text="enter data")
        self.enter_data_inFind.grid(row=2, column=1, padx=(20, 20), pady=(5, 5))

        self.editBtn_inEdit = customtkinter.CTkButton(self.findDB_frame, text="Find",
                                                           command=self.findData_from_kaval_master)
        self.editBtn_inEdit.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 20))

        # Just Label to view Tabel
        self.labelkm_frame = customtkinter.CTkFrame(self.tabview.tab("Kaval Master"), fg_color="transparent")
        self.labelkm_frame.grid(row=2, column=0, padx=(0, 0), pady=(10, 10), sticky="nsew")
        self.label_inKMlabel = customtkinter.CTkLabel(self.labelkm_frame, text="Database View Point")
        self.label_inKMlabel.grid(row=0, column=0, padx=(5, 15), pady=(5, 5),sticky="nsew")

        self.editBtn_inKMLabel = customtkinter.CTkButton(self.labelkm_frame, text="Edit",
                                                           command=self.edit_item_from_Kaval_Master)
        self.editBtn_inKMLabel.grid(row=0, column=1, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.deleteBtn_inKMLabel = customtkinter.CTkButton(self.labelkm_frame, text="Delete",
                                                           command=self.delete_item_from_Kaval_Master)
        self.deleteBtn_inKMLabel.grid(row=0, column=2, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_inKMLabel = customtkinter.CTkButton(self.labelkm_frame, text="Refresh",
                                                           command=self.refresh_table)
        self.refreshBtn_inKMLabel.grid(row=0, column=3, padx=(5, 5), pady=(5, 5),sticky="nsew")

        # view Tabel
        self.viewTabel_km_frame = customtkinter.CTkFrame(self.tabview.tab("Kaval Master"))
        self.viewTabel_km_frame.grid(row=3, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        self.viewTabel_km_frame.columnconfigure(0, weight=1)
        self.viewTabel_km_frame.rowconfigure(0, weight=1)
        

        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir,"manifest.json")
        json_data = read_json_file(file_path)
        db = mysql.connector.connect(
            host=json_data["Database"]["host"],
            user=json_data["Database"]["username"],
            password=json_data["Database"]["password"],
            database=json_data["Database"]["database_name"]
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM kaval_master")
        data = cursor.fetchall()
        self.tree = ttk.Treeview(self.viewTabel_km_frame, columns=list(range(len(data[0]))), show="headings", style="Treeview")
        #self.tree = ttk.Treeview(self.viewTabel_km_frame, columns=("SNo.", "Kaval ID", "Kaval Name"))
        # Set column headings
        for i, heading in enumerate(cursor.column_names):
            self.tree.heading(i, text=heading)

        # Insert data into the treeview
        for row in data:
             self.tree.insert("", "end", values=row)

        # Pack the treeview into the parent widget
        self.tree.pack(fill="both", expand=True)

        # Define column names
        #self.tree.heading("#1", text="SNo.")
        #self.tree.heading("#2", text="Kaval ID")
        #self.tree.heading("#3", text="Kaval Name")

        # Insert data into the TreeView
        #for row in data:
        #    self.tree.insert("", "end", values=row)

        # Apply custom styling to the TreeView
        #self.tree.configure(style="Custom.Treeview")

        # Define a custom style using tkinter's Style class
        #style = ttk.Style()
        #style.configure("Custom.Treeview")#, background="#f7f7f7")
        #style.map("Custom.Treeview")#, background=[("selected", "#347083")])

        # Pack the TreeView
        #self.tree.pack(fill="both", expand=True)

        # Close the cursor and database connection
        cursor.close()
        db.close()
        self.tree.grid(row=0, column=0, sticky="nsew")
        # END OF TAB 1 NAMED : Kaval Master

        # BEGAIN OF TAB 2 NAMED : Surname Master
        # Configure Treeview style
        style = ttk.Style()
        style.theme_use("default")
        style.configure("Treeview",
                        background="#2a2d2e",
                        foreground="white",
                        rowheight=25,
                        fieldbackground="#343638",
                        bordercolor="#343638",
                        borderwidth=0,
                        font=('Arial', 12))  # Set the font size to 12 or adjust as needed

        style.map('Treeview', background=[('selected', '#22559b')])

        style.configure("Treeview.Heading",
                        background="#565b5e",
                        foreground="white",
                        relief="flat",
                        font=('Arial', 12))  # Set the font size to 12 or adjust as needed

        style.map("Treeview.Heading",
                background=[('active', '#3484F0')])
        # new entry dilog box part
        self.addNew_frame_SM = customtkinter.CTkFrame(self.tabview.tab("Surname Master"))
        self.addNew_frame_SM.grid(row=0, column=0, padx=(0, 5), pady=(10, 10),sticky="nsew")

        self.head_label_inNew_SM = customtkinter.CTkLabel(self.addNew_frame_SM, text="Add Data in Database")
        self.head_label_inNew_SM.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=(10, 10))

        self.enterId_label_inNew_SM = customtkinter.CTkLabel(self.addNew_frame_SM, text="Enter ID")
        self.enterId_label_inNew_SM.grid(row=1, column=0, padx=(20, 20), pady=(5, 5))
        self.enter_id_inNew_SM = customtkinter.CTkEntry(self.addNew_frame_SM, placeholder_text="1909")
        self.enter_id_inNew_SM.grid(row=1, column=1, padx=(20, 20), pady=(5, 5))

        self.enterName_label_inNew_SM = customtkinter.CTkLabel(self.addNew_frame_SM, text="Enter Name")
        self.enterName_label_inNew_SM.grid(row=2, column=0, padx=(20, 20), pady=(5, 5))
        self.enter_Name_inNew_SM = customtkinter.CTkEntry(self.addNew_frame_SM, placeholder_text="Surname xx")
        self.enter_Name_inNew_SM.grid(row=2, column=1, padx=(20, 20), pady=(5, 10))

        self.enterNew_inNew_SM = customtkinter.CTkButton(self.addNew_frame_SM, text="Add into Database",
                                                           command=self.add_to_the_surname_master)
        self.enterNew_inNew_SM.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(10, 20))

        # find option dilog box
        self.findDB_frame_SM = customtkinter.CTkFrame(self.tabview.tab("Surname Master"))
        self.findDB_frame_SM.grid(row=0, column=1, padx=(5, 0), pady=(10, 10),sticky="nsew")

        self.head_label_inFind_SM = customtkinter.CTkLabel(self.findDB_frame_SM, text="Scearch in Database")
        self.head_label_inFind_SM.grid(row=0, column=0, columnspan=2, padx=(20, 20), pady=(10, 10))
        self.findBy_inEdit_Label_SM = customtkinter.CTkLabel(self.findDB_frame_SM, text="Find By", anchor="w")
        self.findBy_inEdit_Label_SM.grid(row=1, column=0, padx=20, pady=(5, 5))
        self.findBy_inEdit_optionemenu_SM = customtkinter.CTkOptionMenu(self.findDB_frame_SM, values=["Surname ID", "Surname Name"])
        self.findBy_inEdit_optionemenu_SM.grid(row=1, column=1, padx=20, pady=(5, 5))
        self.data_label_inFind_SM = customtkinter.CTkLabel(self.findDB_frame_SM, text="Enter Respective Data")
        self.data_label_inFind_SM.grid(row=2, column=0, padx=(20, 20), pady=(5, 5))
        self.enter_data_inFind_SM = customtkinter.CTkEntry(self.findDB_frame_SM, placeholder_text="enter data")
        self.enter_data_inFind_SM.grid(row=2, column=1, padx=(20, 20), pady=(5, 5))
        self.editBtn_inEdit_SM = customtkinter.CTkButton(self.findDB_frame_SM, text="Find",
                                                           command=self.findData_from_kaval_master_SM)
        self.editBtn_inEdit_SM.grid(row=3, column=0, columnspan=2, padx=(20, 20), pady=(20, 20))

        # Just Label to view Tabel
        self.labelkm_frame_SM = customtkinter.CTkFrame(self.tabview.tab("Surname Master"), fg_color="transparent")
        self.labelkm_frame_SM.grid(row=2, column=0, padx=(0, 0), pady=(10, 10), sticky="nsew")
        
        self.label_inKMlabel_SM = customtkinter.CTkLabel(self.labelkm_frame_SM, text="Database View Point")
        self.label_inKMlabel_SM.grid(row=0, column=0, padx=(5, 15), pady=(5, 5),sticky="nsew")

        self.editBtn_inKMLabel_SM = customtkinter.CTkButton(self.labelkm_frame_SM, text="Edit",
                                                           command=self.edit_item_from_Kaval_Master_SM)
        self.editBtn_inKMLabel_SM.grid(row=0, column=1, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.deleteBtn_inKMLabel_SM = customtkinter.CTkButton(self.labelkm_frame_SM, text="Delete",
                                                           command=self.delete_item_from_Kaval_Master_SM)
        self.deleteBtn_inKMLabel_SM.grid(row=0, column=2, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_inKMLabel_SM = customtkinter.CTkButton(self.labelkm_frame_SM, text="Refresh",
                                                           command=self.refresh_table_SM)
        self.refreshBtn_inKMLabel_SM.grid(row=0, column=3, padx=(5, 5), pady=(5, 5),sticky="nsew")

        # view Tabel
        self.viewTabel_km_frame_SM = customtkinter.CTkFrame(self.tabview.tab("Surname Master"))
        self.viewTabel_km_frame_SM.grid(row=3, column=0, columnspan=2, padx=(5, 5), pady=(5, 5), sticky="nsew")
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "manifest.json")

            with open(file_path, "r") as json_file:
                json_data = json.load(json_file)

            db = mysql.connector.connect(
                host=json_data["Database"]["host"],
                user=json_data["Database"]["username"],
                password=json_data["Database"]["password"],
                database=json_data["Database"]["database_name"]
            )

            cursor = db.cursor()
            cursor.execute("SELECT * FROM surname_master")
            data = cursor.fetchall()

            # Destroy the existing Treeview widget if it exists
            if hasattr(self, "treeview"):
                self.treeview.destroy()

            # Create a new Treeview widget
            self.treeview = ttk.Treeview(self.viewTabel_km_frame_SM, columns=list(range(len(data[0]))), show="headings", style="Treeview")
            # Configure the interior frame to expand
            self.viewTabel_km_frame_SM.columnconfigure(0, weight=1)
            self.viewTabel_km_frame_SM.rowconfigure(0, weight=1)
            self.treeview.grid(row=0, column=0, sticky="nsew")
            self.treeview.grid(sticky="nsew")

            # Set column headings
            for i, heading in enumerate(cursor.column_names):
                self.treeview.heading(i, text=heading)

            # Insert data into the treeview
            for row in data:
                self.treeview.insert("", "end", values=row)

            # Pack the treeview into the parent widget
            self.treeview.pack(fill="both", expand=True)

            cursor.close()
            db.close()

        except Exception as e:
            # Handle exceptions here (e.g., file not found, database connection error)
            print(f"An error occurred: {str(e)}")

        # ENDS OF TAB 2 NAMED : Surname Master

        self.tabview.tab("Settings").columnconfigure(0, weight=1)
        self.tabview.tab("Settings").columnconfigure(1, weight=1)
        self.tabview.tab("Settings").columnconfigure(2, weight=1)
        self.tabview.tab("Settings").columnconfigure(3, weight=1)

        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=2, column=1, padx=20, pady=10)
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"), values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=2, column=2, padx=20, pady=10)
        self.scaling_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=3, column=1, padx=20, pady=10)
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"), values=["80%", "90%", "100%", "110%", "120%"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=3, column=2, padx=20, pady=10)
        #self.color_theme_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Color Theme:", anchor="w")
        #self.color_theme_label.grid(row=9, column=0, padx=20, pady=(10, 0))
        #self.color_theme_optionmenu = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"), values=["Blue", "Green"],
        #                                                        command=self.change_color_theme_event)
        #self.color_theme_optionmenu.grid(row=10, column=0, padx=20, pady=(10, 20))

        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="Download Kaval in PDF",
                                                           command=self.db_2_pdf_kaval_master)
        self.refreshBtn_test.grid(row=4, column=0, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="Download Surname in PDF",
                                                           command=self.db_2_pdf_surname_master)
        self.refreshBtn_test.grid(row=4, column=1, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="Open PDF Location",
                                                           command=self.open_downloads_folder)
        self.refreshBtn_test.grid(row=4, column=2, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="Exit",
                                                           command=self.exit_application)
        self.refreshBtn_test.grid(row=4, column=3, padx=(5, 5), pady=(5, 5),sticky="nsew")

        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="NA",
                                                           command=self.sidebar_button_event,state="disabled")
        self.refreshBtn_test.grid(row=5, column=0, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="NA",
                                                           command=self.sidebar_button_event,state="disabled")
        self.refreshBtn_test.grid(row=5, column=1, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="NA",
                                                           command=self.sidebar_button_event,state="disabled")
        self.refreshBtn_test.grid(row=5, column=2, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="NA",
                                                           command=self.sidebar_button_event,state="disabled")
        self.refreshBtn_test.grid(row=5, column=3, padx=(5, 5), pady=(5, 5),sticky="nsew")

        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="NA",
                                                           command=self.sidebar_button_event,state="disabled")
        self.refreshBtn_test.grid(row=6, column=0, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="NA",
                                                           command=self.sidebar_button_event,state="disabled")
        self.refreshBtn_test.grid(row=6, column=1, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="NA",
                                                           command=self.sidebar_button_event,state="disabled")
        self.refreshBtn_test.grid(row=6, column=2, padx=(5, 5), pady=(5, 5),sticky="nsew")
        self.refreshBtn_test = customtkinter.CTkButton(self.tabview.tab("Settings"), text="NA",
                                                           command=self.sidebar_button_event ,state="disabled")
        self.refreshBtn_test.grid(row=6, column=3, padx=(5, 5), pady=(5, 5),sticky="nsew")

        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Software is under development stage, if any issue please let us know by opening issue in github repo.", anchor="w")
        self.appearance_mode_label.grid(row=8, column=0, columnspan=4, padx=10, pady=10)


    #def set_default_color_theme(self, theme):
        # Set the default color theme based on the selected theme
        #if theme == "Blue":
            #customtkinter.set_default_color_theme("blue")
            # Add more theme-specific colors as needed
        #elif theme == "Green":
            #customtkinter.set_default_color_theme("green")
            # Add more theme-specific colors as needed

    #def change_color_theme_event(self, theme):
        #self.set_default_color_theme(theme)

    def add_to_the_surname_master(self):
        # Retrieve user-entered ID and Name from the Entry widgets
        new_id = self.enter_id_inNew_SM.get()
        new_name = self.enter_Name_inNew_SM.get()

        # Validate that both ID and Name are provided
        if not new_id or not new_name:
            # Show an error message or handle the validation as needed
            print("Both ID and Name are required.")
            return

        try:
            # Create a MySQL connection
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir,"manifest.json")
            json_data = read_json_file(file_path)
            db = mysql.connector.connect(
                host=json_data["Database"]["host"],
                user=json_data["Database"]["username"],
                password=json_data["Database"]["password"],
                database=json_data["Database"]["database_name"]
            )

            # Create a cursor
            cursor = db.cursor()

            # Insert the new data into the MySQL table
            insert_query = "INSERT INTO surname_master (Surname_ID, Surname_Name) VALUES (%s, %s)"
            cursor.execute(insert_query, (new_id, new_name))

            # Commit the changes to the database
            db.commit()

            # Close the cursor and database connection
            cursor.close()
            db.close()

            # Clear the Entry widgets after adding the data
            self.enter_id_inNew.delete(0, "end")
            self.enter_Name_inNew.delete(0, "end")

            # Optionally, refresh the table to reflect the new data
            self.refresh_table_SM()

        except Exception as e:
            # Handle exceptions here (e.g., database connection error)
            print(f"An error occurred while adding data: {str(e)}")
    
    def refresh_table_SM(self):
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "manifest.json")

            with open(file_path, "r") as json_file:
                json_data = json.load(json_file)

            db = mysql.connector.connect(
                host=json_data["Database"]["host"],
                user=json_data["Database"]["username"],
                password=json_data["Database"]["password"],
                database=json_data["Database"]["database_name"]
            )

            cursor = db.cursor()
            cursor.execute("SELECT * FROM surname_master")
            data = cursor.fetchall()

            # Destroy the existing Treeview widget if it exists
            if hasattr(self, "treeview"):
                self.treeview.destroy()

            # Create a new Treeview widget
            self.treeview = ttk.Treeview(self.viewTabel_km_frame_SM, columns=list(range(len(data[0]))), show="headings", style="Treeview")

            # Set column headings
            for i, heading in enumerate(cursor.column_names):
                self.treeview.heading(i, text=heading)

            # Insert data into the treeview
            for row in data:
                self.treeview.insert("", "end", values=row)

            # Pack the treeview into the parent widget
            self.treeview.pack(fill="both", expand=True)

            cursor.close()
            db.close()

        except Exception as e:
            # Handle exceptions here (e.g., file not found, database connection error)
            print(f"An error occurred: {str(e)}")

    def refresh_table(self):
        # Read JSON data from the manifest.json file
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir, "manifest.json")

            with open(file_path, "r") as json_file:
                json_data = json.load(json_file)

            db = mysql.connector.connect(
                host=json_data["Database"]["host"],
                user=json_data["Database"]["username"],
                password=json_data["Database"]["password"],
                database=json_data["Database"]["database_name"]
            )

            cursor = db.cursor()
            cursor.execute("SELECT * FROM kaval_master")
            data = cursor.fetchall()
 
            for item in self.tree.get_children():
                self.tree.delete(item)

            for row in data:
                self.tree.insert("", "end", values=row)

            cursor.close()
            db.close()

        except Exception as e:
            # Handle exceptions here (e.g., file not found, database connection error)
            print(f"An error occurred: {str(e)}")

    def add_to_the_kaval_master(self):
        # Retrieve user-entered ID and Name from the Entry widgets
        new_id = self.enter_id_inNew.get()
        new_name = self.enter_Name_inNew.get()

        # Validate that both ID and Name are provided
        if not new_id or not new_name:
            # Show an error message or handle the validation as needed
            print("Both ID and Name are required.")
            return

        try:
            # Create a MySQL connection
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir,"manifest.json")
            json_data = read_json_file(file_path)
            db = mysql.connector.connect(
                host=json_data["Database"]["host"],
                user=json_data["Database"]["username"],
                password=json_data["Database"]["password"],
                database=json_data["Database"]["database_name"]
            )

            # Create a cursor
            cursor = db.cursor()

            # Insert the new data into the MySQL table
            insert_query = "INSERT INTO kaval_master (Kaval_ID, Kaval_Name) VALUES (%s, %s)"
            cursor.execute(insert_query, (new_id, new_name))

            # Commit the changes to the database
            db.commit()

            # Close the cursor and database connection
            cursor.close()
            db.close()

            # Clear the Entry widgets after adding the data
            self.enter_id_inNew.delete(0, "end")
            self.enter_Name_inNew.delete(0, "end")

            # Optionally, refresh the table to reflect the new data
            self.refresh_table()

        except Exception as e:
            # Handle exceptions here (e.g., database connection error)
            print(f"An error occurred while adding data: {str(e)}")


    def findData_from_kaval_master(self):
        # Retrieve user-selected search criteria and entered data
        find_by = self.findBy_inEdit_optionemenu.get()
        entered_data = self.enter_data_inFind.get()

        # Validate that the entered data is not empty
        if not entered_data:
            # Show an error message or handle the validation as needed
            print("Please enter data to search.")
            return

        try:
            # Create a MySQL connection
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir,"manifest.json")
            json_data = read_json_file(file_path)
            db = mysql.connector.connect(
                host=json_data["Database"]["host"],
                user=json_data["Database"]["username"],
                password=json_data["Database"]["password"],
                database=json_data["Database"]["database_name"]
            )

            # Create a cursor
            cursor = db.cursor()

            # Define the query based on the selected search criteria
            if find_by == "Kaval ID":
                query = "SELECT * FROM kaval_master WHERE Kaval_ID = %s"
            elif find_by == "Kaval Name":
                query = "SELECT * FROM kaval_master WHERE Kaval_Name = %s"
            elif find_by == "SNo.":
                query = "SELECT * FROM kaval_master WHERE SNo = %s"
            else:
                # Handle unsupported search criteria
                print("Unsupported search criteria.")
                return

            # Execute the query with the entered data
            cursor.execute(query, (entered_data,))
            data = cursor.fetchall()

            # Clear the TreeView to display the search results
            for item in self.tree.get_children():
                self.tree.delete(item)

            # Insert the search results into the TreeView
            for row in data:
                self.tree.insert("", "end", values=row)

            # Close the cursor and database connection
            cursor.close()
            db.close()

        except Exception as e:
            # Handle exceptions here (e.g., database connection error)
            print(f"An error occurred while searching: {str(e)}")

    def findData_from_kaval_master_SM(self):
        # Retrieve user-selected search criteria and entered data
        find_by = self.findBy_inEdit_optionemenu_SM.get()
        entered_data = self.enter_data_inFind_SM.get()

        # Validate that the entered data is not empty
        if not entered_data:
            # Show an error message or handle the validation as needed
            print("Please enter data to search.")
            return

        try:
            # Create a MySQL connection
            script_dir = os.path.dirname(os.path.abspath(__file__))
            file_path = os.path.join(script_dir,"manifest.json")
            json_data = read_json_file(file_path)
            db = mysql.connector.connect(
                host=json_data["Database"]["host"],
                user=json_data["Database"]["username"],
                password=json_data["Database"]["password"],
                database=json_data["Database"]["database_name"]
            )

            # Create a cursor
            cursor = db.cursor()

            # Define the query based on the selected search criteria
            if find_by == "Surname ID":
                query = "SELECT * FROM surname_master WHERE Surname_ID = %s"
            elif find_by == "Surname Name":
                query = "SELECT * FROM surname_master WHERE Surname_Name = %s"
            else:
                # Handle unsupported search criteria
                print("Unsupported search criteria.")
                return

            # Execute the query with the entered data
            cursor.execute(query, (entered_data,))
            data = cursor.fetchall()

            # Clear the TreeView to display the search results
            for item in self.treeview.get_children():
                self.treeview.delete(item)

            # Insert the search results into the TreeView
            for row in data:
                self.treeview.insert("", "end", values=row)

            # Close the cursor and database connection
            cursor.close()
            db.close()

        except Exception as e:
            # Handle exceptions here (e.g., database connection error)
            print(f"An error occurred while searching: {str(e)}")

    def open_input_dialog_event(self):
        dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
        print("CTkInputDialog:", dialog.get_input())

    def delete_item_from_Kaval_Master(self):
        # Create an input dialog to get the ID to delete
        dialog = customtkinter.CTkInputDialog(text="Enter ID which you want to delete", title="Deleting Item")
        selected_id = dialog.get_input()

        if not selected_id:
            # No ID entered
            return

        # Create a MySQL connection
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir,"manifest.json")
        json_data = read_json_file(file_path)
        db = mysql.connector.connect(
            host=json_data["Database"]["host"],
            user=json_data["Database"]["username"],
            password=json_data["Database"]["password"],
            database=json_data["Database"]["database_name"]
        )

        # Create a cursor
        cursor = db.cursor()

        # Delete the data from the MySQL table based on the entered ID
        cursor.execute("DELETE FROM kaval_master WHERE Kaval_ID = %s", (selected_id,))

        # Commit the changes to the database
        db.commit()

        # Close the cursor and database connection
        cursor.close()
        db.close()

        # Refresh the table to reflect the changes
        self.refresh_table()

    def edit_item_from_Kaval_Master(self):
        # Create an input dialog to get the ID to edit
        dialog = customtkinter.CTkInputDialog(text="Enter ID to edit", title="Editing Item")
        selected_id = dialog.get_input()

        if not selected_id:
            # No ID entered
            return

        # Create an input dialog to get the new name
        new_name_dialog = customtkinter.CTkInputDialog(text="Enter the new name", title="Editing Name")
        new_name = new_name_dialog.get_input()

        if not new_name:
            # No new name entered
            return

        # Create a MySQL connection
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir,"manifest.json")
        json_data = read_json_file(file_path)
        db = mysql.connector.connect(
            host=json_data["Database"]["host"],
            user=json_data["Database"]["username"],
            password=json_data["Database"]["password"],
            database=json_data["Database"]["database_name"]
        )

        # Create a cursor
        cursor = db.cursor()
        # Update the name in the MySQL table based on the selected ID
        cursor.execute("UPDATE kaval_master SET Kaval_Name = %s WHERE Kaval_ID = %s", (new_name, selected_id))
        # Commit the changes to the database
        db.commit()
        # Close the cursor and database connection
        cursor.close()
        db.close()
        # Refresh the table to reflect the changes
        self.refresh_table()

    #=======
    def delete_item_from_Kaval_Master_SM(self):
        # Create an input dialog to get the ID to delete
        dialog = customtkinter.CTkInputDialog(text="Enter ID which you want to delete", title="Deleting Item")
        selected_id = dialog.get_input()

        if not selected_id:
            # No ID entered
            return

        # Create a MySQL connection
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir,"manifest.json")
        json_data = read_json_file(file_path)
        db = mysql.connector.connect(
            host=json_data["Database"]["host"],
            user=json_data["Database"]["username"],
            password=json_data["Database"]["password"],
            database=json_data["Database"]["database_name"]
        )

        # Create a cursor
        cursor = db.cursor()

        # Delete the data from the MySQL table based on the entered ID
        cursor.execute("DELETE FROM surname_master WHERE Surname_ID = %s", (selected_id,))

        # Commit the changes to the database
        db.commit()

        # Close the cursor and database connection
        cursor.close()
        db.close()

        # Refresh the table to reflect the changes
        self.refresh_table_SM()

    def edit_item_from_Kaval_Master_SM(self):
        # Create an input dialog to get the ID to edit
        dialog = customtkinter.CTkInputDialog(text="Enter ID to edit", title="Editing Item")
        selected_id = dialog.get_input()

        if not selected_id:
            # No ID entered
            return

        # Create an input dialog to get the new name
        new_name_dialog = customtkinter.CTkInputDialog(text="Enter the new name", title="Editing Name")
        new_name = new_name_dialog.get_input()

        if not new_name:
            # No new name entered
            return

        # Create a MySQL connection
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir,"manifest.json")
        json_data = read_json_file(file_path)
        db = mysql.connector.connect(
            host=json_data["Database"]["host"],
            user=json_data["Database"]["username"],
            password=json_data["Database"]["password"],
            database=json_data["Database"]["database_name"]
        )

        # Create a cursor
        cursor = db.cursor()
        # Update the name in the MySQL table based on the selected ID
        cursor.execute("UPDATE surname_master SET Surname_Name = %s WHERE Surname_ID = %s", (new_name, selected_id))
        # Commit the changes to the database
        db.commit()
        # Close the cursor and database connection
        cursor.close()
        db.close()
        # Refresh the table to reflect the changes
        self.refresh_table_SM()


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        new_scaling_float = int(new_scaling.replace("%", "")) / 100
        customtkinter.set_widget_scaling(new_scaling_float)

    def sidebar_button_event(self):
        print("sidebar_button click")
    
    def exit_application(self):
        # Confirm with the user before exiting
        confirm = messagebox.askyesno("Exit", "Are you sure you want to exit?")
        if confirm:
            self.destroy()

    def open_downloads_folder(self):
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        webbrowser.open(downloads_folder)

    def db_2_pdf_kaval_master(self):
        # Load MySQL connection details from manifest.json
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "manifest.json")

        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)

        # Connect to MySQL
        db = mysql.connector.connect(
            host=json_data["Database"]["host"],
            user=json_data["Database"]["username"],
            password=json_data["Database"]["password"],
            database=json_data["Database"]["database_name"]
        )

        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM kaval_master")
        data = cursor.fetchall()

        cursor.close()
        db.close()

        # Generate PDF file name with table name, date, and timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        pdf_filename = f"kaval_master_{timestamp}.pdf"

        # Save PDF in the Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        pdf_path = os.path.join(downloads_folder, pdf_filename)

        # Create a PDF document
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)

        # Create a table from the MySQL data
        table_data = [tuple(['SNo.', 'Kaval ID', 'Kaval Name'])] + data
        pdf_table = Table(table_data)

        # Add style to the table (including borders)
        style = TableStyle([('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))])
        pdf_table.setStyle(style)

        # Build the PDF document
        doc.build([pdf_table])

        # Display a popup notification
        message_title = "PDF Downloaded"
        message_text = f"The PDF file has been downloaded to the Downloads folder: {pdf_path}"
        messagebox.showinfo(message_title, message_text)

    def db_2_pdf_surname_master(self):
        # Load MySQL connection details from manifest.json
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "manifest.json")

        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)

        # Connect to MySQL
        db = mysql.connector.connect(
            host=json_data["Database"]["host"],
            user=json_data["Database"]["username"],
            password=json_data["Database"]["password"],
            database=json_data["Database"]["database_name"]
        )

        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM surname_master")
        data = cursor.fetchall()

        cursor.close()
        db.close()

        # Generate PDF file name with table name, date, and timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        pdf_filename = f"surname_master_{timestamp}.pdf"

        # Save PDF in the Downloads folder
        downloads_folder = os.path.join(os.path.expanduser("~"), "Downloads")
        pdf_path = os.path.join(downloads_folder, pdf_filename)

        # Create a PDF document
        doc = SimpleDocTemplate(pdf_path, pagesize=letter)

        # Create a table from the MySQL data
        table_data = [tuple(['Surname ID', 'Surname Name'])] + data
        pdf_table = Table(table_data)

        # Add style to the table (including borders)
        style = TableStyle([('GRID', (0, 0), (-1, -1), 1, (0, 0, 0))])
        pdf_table.setStyle(style)

        # Build the PDF document
        doc.build([pdf_table])

        # Display a popup notification
        message_title = "PDF Downloaded"
        message_text = f"The PDF file has been downloaded to the Downloads folder: {pdf_path}"
        messagebox.showinfo(message_title, message_text)

def read_json_file(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
        return data

def notification(head,body):
    pass

def open_main_window():
    if(isUP.isAvailabe()):
        isUP.updateNotify()
    # Create a MySQL connection
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
