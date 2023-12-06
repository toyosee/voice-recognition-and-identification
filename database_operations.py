import sqlite3

class DatabaseHandler:
    def __init__(self, db_name='voice_database.db'):
        try:
            self.conn = sqlite3.connect(db_name)
            self.cursor = self.conn.cursor()
            self.create_tables()  # Ensure tables are created upon initialization
            print("Database connection established.")
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def create_tables(self):
        try:
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Users (
                                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                   Name TEXT,
                                   Sex TEXT)''')
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS Recordings (
                                   ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                   UserID INTEGER,
                                   FilePath TEXT,
                                   FOREIGN KEY (UserID) REFERENCES Users(ID))''')
            self.conn.commit()
            print("Tables created successfully.")
        except sqlite3.Error as e:
            print(f"Error creating tables: {e}")

    def insert_user(self, name, sex):
        try:
            self.cursor.execute("INSERT INTO Users (Name, Sex) VALUES (?, ?)", (name, sex))
            self.conn.commit()
            print("User inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting user: {e}")

    def insert_recording(self, user_id, file_path):
        try:
            self.cursor.execute("INSERT INTO Recordings (UserID, FilePath) VALUES (?, ?)", (user_id, file_path))
            self.conn.commit()
            print("Recording inserted successfully.")
        except sqlite3.Error as e:
            print(f"Error inserting recording: {e}")

    def get_user_id(self, name):
        try:
            self.cursor.execute("SELECT ID FROM Users WHERE Name = ?", (name,))
            user = self.cursor.fetchone()
            return user[0] if user else None
        except sqlite3.Error as e:
            print(f"Error fetching user ID: {e}")

    def close_connection(self):
        try:
            self.conn.close()
            print("Database connection closed.")
        except sqlite3.Error as e:
            print(f"Error closing database connection: {e}")
