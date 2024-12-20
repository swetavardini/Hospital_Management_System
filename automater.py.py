import tkinter as tk
from tkinter import ttk
import sqlite3
from faker import Faker
import random

class Database:
    def __init__(self):
        self.dbConnection = sqlite3.connect("patientdb.db")
        self.dbCursor = self.dbConnection.cursor()
        self.dbCursor.execute(
            "CREATE TABLE IF NOT EXISTS patient_table (id INTEGER PRIMARY KEY AUTOINCREMENT, firstname TEXT, lastname TEXT, dateOfBirth TEXT, monthOfBirth TEXT, yearOfBirth TEXT, gender TEXT, address TEXT, contactNumber TEXT, emailAddress TEXT, bloodType TEXT, history TEXT, doctor TEXT)"
        )

    def __del__(self):
        self.dbCursor.close()
        self.dbConnection.close()

    def Insert(self, data):
        self.dbCursor.execute(
            "INSERT INTO patient_table (firstname, lastname, dateOfBirth, monthOfBirth, yearOfBirth, gender, address, contactNumber, emailAddress, bloodType, history, doctor) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            data
        )
        self.dbConnection.commit()

    def DisplayAll(self):
        self.dbCursor.execute("SELECT * FROM patient_table")
        records = self.dbCursor.fetchall()
        return records

class MedicalReportsGenerator:
    def __init__(self):
        self.root = tk.Tk()
        self.root.wm_title("Medical Reports Generator")
        self.db = Database()

        # Create and pack frames
        self.frame_generate = tk.Frame(self.root)
        self.frame_generate.pack(pady=10)
        self.frame_view = tk.Frame(self.root)
        self.frame_view.pack(pady=10)

        # Create buttons for generating reports and viewing them
        tk.Button(self.frame_generate, text="Generate Report", command=self.GenerateReport).pack(side=tk.LEFT, padx=10)
        tk.Button(self.frame_view, text="View All Reports", command=self.ViewAllReports).pack(side=tk.LEFT, padx=10)

    def GenerateReport(self):
        # Generate random patient data using Faker
        fake = Faker()
        first_name = fake.first_name()
        last_name = fake.last_name()
        date_of_birth = fake.date_of_birth()
        gender = random.choice(["Male", "Female"])
        address = fake.address()
        contact_number = fake.phone_number()
        email_address = fake.email()
        blood_type = random.choice(["A+", "B+", "AB+", "O+", "A-", "B-", "AB-", "O-"])
        medical_history = fake.text(max_nb_chars=200)

        # Insert the generated data into the database
        data = (
            first_name,
            last_name,
            date_of_birth.strftime("%d"),
            date_of_birth.strftime("%B"),
            date_of_birth.strftime("%Y"),
            gender,
            address,
            contact_number,
            email_address,
            blood_type,
            medical_history,
            "Automated Report Generator",
        )
        self.db.Insert(data)
        print("Generated and inserted a new medical report.")

    def ViewAllReports(self):
        # Call the DisplayAll method from the Database class to get all patient records
        all_records = self.db.DisplayAll()
        for record in all_records:
            print(record)

if __name__ == "__main__":
    generator = MedicalReportsGenerator()
    generator.root.mainloop()
