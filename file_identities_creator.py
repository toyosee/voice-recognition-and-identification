import os
import sqlite3

def fetch_names_from_database():
    conn = sqlite3.connect('voice_database.db')  # Replace 'voice_database.db' with your actual database file
    
    cursor = conn.cursor()
    
    cursor.execute("SELECT ID, Name FROM Users")
    user_rows = cursor.fetchall()
    
    cursor.execute("SELECT UserID, FilePath FROM Recordings")
    recording_rows = cursor.fetchall()
    
    conn.close()
   
    users_dict = {user_id: name for user_id, name in user_rows}
    
    # Collect all recordings for each user using a dictionary of lists
    recordings_dict = {user_id: [] for user_id in users_dict}
    for user_id, file_path in recording_rows:
        recordings_dict[user_id].append(os.path.basename(file_path))
    
    # Combine the information using a dictionary comprehension
    names_dict = {user_id: recordings_dict[user_id] for user_id in users_dict}
    print(names_dict)
    
    return names_dict

def save_identities_dict_as_script(file_identities):
    with open('file_identities.py', 'w') as file:
        file.write("# All audio files are mapped here as a dictionary\n\nfile_identities = {\n")
        for key, value in file_identities.items():
            file.write(f"    '{key}': {value},\n")
        file.write("}\n")

if __name__ == "__main__":
    folder_path = 'recordings'  # Replace 'recordings' with the path to your audio files folder
    
    file_identities = fetch_names_from_database()
    
    save_identities_dict_as_script(file_identities)
