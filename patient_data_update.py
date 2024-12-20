import tkinter
import tkinter.ttk as ttk
import sqlite3


# Define or import the missing class 'Database' if it is not defined in this code.

class UpdateWindow:
    def __init__(self, id):
        self.window = tkinter.Tk()
        self.window.wm_title("Update data")
        bg_color = "Blue"
        fg_color = "white"

        # Initializing all the variables
        self.id = id

        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.contactNumber = tkinter.StringVar()
        self.emailAddress = tkinter.StringVar()
        self.history = tkinter.StringVar()
        self.doctor = tkinter.StringVar()

        self.genderType = ["Male", "Female", "Transgender", "Other"]
        self.dateType = list(range(1, 32))
        self.monthType = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                          "October", "November", "December"]
        self.yearType = list(range(1900, 2020))
        self.bloodListType = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

        # Labels
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, text="Patient Id", font=("times new roman", 10, "bold"),
                      width=25).grid(pady=5, column=1, row=1)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, text="Patient First Name",
                      font=("times new roman", 10, "bold"), width=25).grid(pady=5, column=1, row=2)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Last Name", width=25).grid(pady=5, column=1, row=3)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"), text="Date of Birth",
                      width=25).grid(pady=5, column=1, row=4)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Month of Birth", width=25).grid(pady=5, column=1, row=5)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"), text="Year of Birth",
                      width=25).grid(pady=5, column=1, row=6)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Gender", width=25).grid(pady=5, column=1, row=7)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Address", width=25).grid(pady=5, column=1, row=8)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Contact Number", width=25).grid(pady=5, column=1, row=9)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Email Address", width=25).grid(pady=5, column=1, row=10)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Patient Blood Type", width=25).grid(pady=5, column=1, row=11)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="History of Patient", width=25).grid(pady=5, column=1, row=12)
        tkinter.Label(self.window, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                      text="Name of Doctor", width=25).grid(pady=5, column=1, row=13)
        

        # Set previous values
class Database:

    def __init__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS patient_table (id PRIMARY KEY text, firstname text, lastname text, dateOfBirth text, monthOfBirth text, yearOfBirth text, gender text, address text, contactNumber text, emailAddress text, bloodType text, history text, doctor text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    

    def Update(self, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber,
               emailAddress, bloodType, history, doctor, id):
        self.dbCursor.execute(
            "UPDATE patient_table SET firstname = ?, lastname = ?, dateOfBirth = ?, monthOfBirth = ?, yearOfBirth = ?, gender = ?, address = ?, contactNumber = ?, emailAddress = ?, bloodType = ?, history = ?, doctor = ? WHERE id = ?",
            (firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress,
             bloodType, history, doctor, id))
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
    # Set previous values
        self.database = Database()
        self.searchResults = self.database.Search(id)

    
       

        if self.searchResults:
            tkinter.Label(self.window, text=self.searchResults[0][1], width=25).grid(pady=5, column=2, row=2)
            tkinter.Label(self.window, text=self.searchResults[0][2], width=25).grid(pady=5, column=2, row=3)
            tkinter.Label(self.window, text=self.searchResults[0][3], width=25).grid(pady=5, column=2, row=4)
            tkinter.Label(self.window, text=self.searchResults[0][4], width=25).grid(pady=5, column=2, row=5)
            tkinter.Label(self.window, text=self.searchResults[0][5], width=25).grid(pady=5, column=2, row=6)
            tkinter.Label(self.window, text=self.searchResults[0][6], width=25).grid(pady=5, column=2, row=7)
            tkinter.Label(self.window, text=self.searchResults[0][7], width=25).grid(pady=5, column=2, row=8)
            tkinter.Label(self.window, text=self.searchResults[0][8], width=25).grid(pady=5, column=2, row=9)
            tkinter.Label(self.window, text=self.searchResults[0][9], width=25).grid(pady=5, column=2, row=10)
            tkinter.Label(self.window, text=self.searchResults[0][10], width=25).grid(pady=5, column=2, row=11)
            tkinter.Label(self.window, text=self.searchResults[0][11], width=25).grid(pady=5, column=2, row=12)
            tkinter.Label(self.window, text=self.searchResults[0][12], width=25).grid(pady=5, column=2, row=13)

        self.idEntry = tkinter.Entry(self.window, width=25, textvariable=self.id)
        self.firstnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.firstname)
        self.lastnameEntry = tkinter.Entry(self.window, width=25, textvariable=self.lastname)
        self.addressEntry = tkinter.Entry(self.window, width=25, textvariable=self.address)
        self.contactNumberEntry = tkinter.Entry(self.window, width=25, textvariable=self.contactNumber)
        self.emailAddressEntry = tkinter.Entry(self.window, width=25, textvariable=self.emailAddress)
        self.historyEntry = tkinter.Entry(self.window, width=25, textvariable=self.history)
        self.doctorEntry = tkinter.Entry(self.window, width=25, textvariable=self.doctor)

        self.idEntry.grid(pady=5, column=3, row=1)
        self.firstnameEntry.grid(pady=5, column=3, row=2)
        self.lastnameEntry.grid(pady=5, column=3, row=3)
        self.addressEntry.grid(pady=5, column=3, row=8)
        self.contactNumberEntry.grid(pady=5, column=3, row=9)
        self.emailAddressEntry.grid(pady=5, column=3, row=10)
        self.historyEntry.grid(pady=5, column=3, row=12)
        self.doctorEntry.grid(pady=5, column=3, row=13)

        # Combobox
        self.dateOfBirthBox = ttk.Combobox(self.window, values=self.dateType, width=20)
        self.monthOfBirthBox = ttk.Combobox(self.window, values=self.monthType, width=20)
        self.yearOfBirthBox = ttk.Combobox(self.window, values=self.yearType, width=20)
        self.genderBox = ttk.Combobox(self.window, values=self.genderType, width=20)
        self.bloodListBox = ttk.Combobox(self.window, values=self.bloodListType, width=20)

        self.dateOfBirthBox.grid(pady=5, column=3, row=4)
        self.monthOfBirthBox.grid(pady=5, column=3, row=5)
        self.yearOfBirthBox.grid(pady=5, column=3, row=6)
        self.genderBox.grid(pady=5, column=3, row=7)
        self.bloodListBox.grid(pady=5, column=3, row=11)

        # Button
        tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                       text="Insert", command=self.Insert).grid(pady=15, padx=5, column=1, row=14)
        tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                       text="Reset", command=self.Reset).grid(pady=15, padx=5, column=2, row=14)
        tkinter.Button(self.window, width=10, fg=fg_color, bg=bg_color, font=("times new roman", 10, "bold"),
                       text="Close", command=self.window.destroy).grid(pady=15, padx=5, column=3, row=14)

        self.window.mainloop()
    def Insert(self):
        # Get the values from the input fields
        id_val = self.id.get()
        firstname_val = self.firstname.get()
        lastname_val = self.lastname.get()
        dateOfBirth_val = self.dateOfBirthBox.get()
        monthOfBirth_val = self.monthOfBirthBox.get()
        yearOfBirth_val = self.yearOfBirthBox.get()
        gender_val = self.genderBox.get()
        address_val = self.address.get()
        contactNumber_val = self.contactNumber.get()
        emailAddress_val = self.emailAddress.get()
        bloodType_val = self.bloodListBox.get()
        history_val = self.history.get()
        doctor_val = self.doctor.get()

        # Call the Database class to insert dataclass Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS patient_table (id PRIMARY KEY text, firstname text, lastname text, dateOfBirth text, monthOfBirth text, yearOfBirth text, gender text, address text, contactNumber text, emailAddress text, bloodType text, history text, doctor text)")

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, id, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, doctor):
        self.dbCursor.execute("INSERT INTO patient_table VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (
        id, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress,
        bloodType, history, doctor))
        self.dbConnection.commit()

    def Update(self, firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber,
               emailAddress, bloodType, history, doctor, id):
        self.dbCursor.execute(
            "UPDATE patient_table SET firstname = ?, lastname = ?, dateOfBirth = ?, monthOfBirth = ?, yearOfBirth = ?, gender = ?, address = ?, contactNumber = ?, emailAddress = ?, bloodType = ?, history = ?, doctor = ? WHERE id = ?",
            (firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress,
             bloodType, history, doctor, id))
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
        self.database = Database()
        self.database.Insert(id_val, firstname_val, lastname_val, dateOfBirth_val, monthOfBirth_val, yearOfBirth_val,
                             gender_val, address_val, contactNumber_val, emailAddress_val, bloodType_val, history_val,
                             doctor_val)

        # Display a message to indicate successful insertion
        tkinter.messagebox.showinfo("Success", "Data inserted successfully!")

        # Clear the input fields
        self.id.set("")
        self.firstname.set("")
        self.lastname.set("")
        self.dateOfBirthBox.set("")
        self.monthOfBirthBox.set("")
        self.yearOfBirthBox.set("")
        self.genderBox.set("")
        self.address.set("")
        self.contactNumber.set("")
        self.emailAddress.set("")
        self.bloodListBox.set("")
        self.history.set("")
        self.doctor.set("")

    def Reset(self):
        # Clear the input fields
        self.id.set("")
        self.firstname.set("")
        self.lastname.set("")
        self.dateOfBirthBox.set("")
        self.monthOfBirthBox.set("")
        self.yearOfBirthBox.set("")
        self.genderBox.set("")
        self.address.set("")
        self.contactNumber.set("")
        self.emailAddress.set("")
        self.bloodListBox.set("")
        self.history.set("")
        self.doctor.set("")
    if __name__ == "__main__":
    # Instantiate UpdateWindow with a patient ID
      update_window = UpdateWindow("PAT123")
