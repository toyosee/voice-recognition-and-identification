import os

def create_identities_dict(folder_path):
    file_identities = {}
    
    audio_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
    
    for file in audio_files:
        # Extract identity (class) from the filename (assuming the name before '.wav' is the identity)
        identity = file.split('.')[0]  # Extract the identity from the filename (sample.wav -> 'sample')
        file_identities[file] = identity
    
    return file_identities

def save_identities_dict_as_script(file_identities):
    with open('file_identities.py', 'w') as file:
        file.write("file_identities = {\n")
        for key, value in file_identities.items():
            file.write(f"    '{key}': '{value}',\n")
        file.write("}\n")

if __name__ == "__main__":
    # Replace 'recordings' with the path to your audio files folder
    folder_path = 'recordings'
    
    # Create the file_identities dictionary
    file_identities = create_identities_dict(folder_path)
    
    # Save the file_identities dictionary as a Python script
    save_identities_dict_as_script(file_identities)
