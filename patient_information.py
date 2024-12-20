
from msilib.schema import SelfReg
import tkinter
import sqlite3
from typing import Self
class SearchDeleteWindow:
    def __init__(self, action):
        # Implementation for the SearchDeleteWindow goes here...
        pass
class UpdateWindow:
    def __init__(self, id_entry_value):
        # Implementation for the UpdateWindow goes here...
        pass
class DatabaseView:
    def __init__(self, data):
        # Implementation for the DatabaseView goes here...
        pass
class InsertWindow:
    def __init__(self):
        # Implementation for the InsertWindow goes here...
        pass


class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
             "CREATE TABLE IF NOT EXISTS patient_table (id PRIMARYKEY text, firstname text, lastname text, dateOfBirth text, monthOfBirth text, yearOfBirth text, gender text, address text, contactNumber text, emailAddress text, bloodType text, history text, doctor text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, doctor):
        self.dbCursor.execute("INSERT INTO patient_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        id, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, doctor))
        self.dbConnection.commit()

    def Update(self, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, doctor, id):
        self.dbCursor.execute(
            "UPDATE patient_table SET firstname = ?, lastname = ?, dateOfBirth = ?, monthOfBirth = ?, yearOfBirth = ?, gender = ?, address = ?, contactNumber = ?, emailAddress = ?, bloodType = ?, history = ?, doctor = ? WHERE id = ?",
        (firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, doctor, id))
        self.dbConnection.commit()

    def Search(self, id):
        self.dbCursor.execute("SELECT * FROM patient_table WHERE id = ?", (id,))
        searchResults = self.dbCursor.fetchall()
        return searchResults

    def Delete(self, id):
        self.dbCursor.execute("DELETE FROM patient_table WHERE id = ?", (id,))
        self.dbConnection.commit()

    def Display(self):
        self.dbCursor.execute("SELECT * FROM patient_table")
        records = self.dbCursor.fetchall()
        return records
class Values:
    def Validate(self, id, firstname, lastname, contactNumber, emailAdress, history, doctor):
        if not (id.isdigit() and (len(id) == 3)):
            return "id"
        elif not (firstname.isalpha()):
             return "firstname"
        elif not (lastname.isalpha()):
             return "lastname"
        elif not (contactNumber.isdigit() and (len(contactNumber) == 11)):
             return "contactNumber"
        elif not (emailAdress.count("@") == 1 and emailAdress.count(".") > 0):
             return "emailAddress"
        elif not (history.isalpha()):
             return "history"
        elif not (doctor.isalpha()):
             return "doctor"
        else:
             return "SUCCESS"
class HomePage:
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Patient Information Details")
bg_color = "blue"
fg_color = "white"
lbl_color = 'GREEN'
tkinter.Label(self.homePageWindow, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Home Page", font=("times new roman",20,"bold"), width=30).grid(pady=20, column=1, row=1)

tkinter.Button(self.homePageWindow, width=20, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Insert", font=("times new roman",15,"bold"), command=self.Insert).grid(pady=15, column=1, row=2)
tkinter.Button(self.homePageWindow, width=20, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Update", font=("times new roman",15,"bold"), command=self.Update).grid(pady=15, column=1, row=3)
tkinter.Button(self.homePageWindow, width=20, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Search", font=("times new roman",15,"bold"), command=self.Search).grid(pady=15, column=1, row=4)
tkinter.Button(self.homePageWindow, width=20, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Delete", font=("times new roman",15,"bold"), command=self.Delete).grid(pady=15, column=1, row=5)
tkinter.Button(self.homePageWindow, width=20, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Display", font=("times new roman",15,"bold"), command=self.Display).grid(pady=15, column=1,row=6)
tkinter.Button(self.homePageWindow, width=20, relief=tkinter.GROOVE, fg=fg_color, bg=bg_color, text="Exit", font=("times new roman",15,"bold"), command=self.homePageWindow.destroy).grid(pady=15, column=1, row=7)

Self.homePageWindow.mainloop()

def Insert(self):
    self.insertWindow = InsertWindow()

def Update(self):
    self.updateIDWindow = tkinter.Tk()
    self.updateIDWindow.wm_title("Update data")

# Initializing all the variables
    self.id = tkinter.StringVar()

# Label
tkinter.Label(SelfReg.updateIDWindow, text="Enter the ID to update", width=50).grid(pady=20, row=1)

# Entry widgets
Self.idEntry = tkinter.Entry(self.updateIDWindow, width=5, textvariable=self.id)

self.idEntry.grid(pady=10, row=2)

# Button widgets
tkinter.Button(self.updateIDWindow, width=20, text="Update", command=self.updateID).grid(pady=10, row=3)
self.updateIDWindow.mainloop()

def updateID(self):
    self.updateWindow = UpdateWindow(self.idEntry.get())
    self.updateIDWindow.destroy()

    def Search(self):
        self.searchWindow = SearchDeleteWindow("Search")

    def Delete(self):
        self.deleteWindow = SearchDeleteWindow("Delete")

    def Display(self):
        self.database = Database()
        self.data = self.database.Display()
        self.displayWindow = DatabaseView(self.data)


homePage = HomePage()