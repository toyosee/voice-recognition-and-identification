# Author: Elijah Abolaji
# Version: 1.0

import os
import pyaudio
import wave
from database_operations import DatabaseHandler

# Get user details from user input
def get_user_details():
    # Function to get user details interactively
    name = input("Enter your name: ")
    sex = input("Enter your sex (Male/Female): ")
    return name, sex

def record_audio(duration=10):
    folder_name = 'recordings'
    
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    
    # Determine the next available filename by checking existing files in the 'recordings' folder
    existing_recordings = os.listdir(folder_name)
    existing_samples = [f for f in existing_recordings if f.startswith('sample')]
    last_sample_number = len(existing_samples)
    next_filename = f"sample{last_sample_number + 1}.wav"
    file_path = os.path.join(folder_name, next_filename)
    
    # Initialize DatabaseHandler
    db_handler = DatabaseHandler()

    chunk = 1024
    sample_format = pyaudio.paInt16
    channels = 1
    fs = 44100
    seconds = duration
    
    p = pyaudio.PyAudio()

    default_device_index = p.get_default_input_device_info().get('index')
    device_info = p.get_device_info_by_index(default_device_index)
    
    if device_info['maxInputChannels'] == 0:
        print("No external microphone detected. Using default system microphone.")

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True,
                    input_device_index=default_device_index)

    print("Recording...")
    frames = []

    for i in range(0, int(fs / chunk * seconds)):
        try:
            data = stream.read(chunk)
            frames.append(data)
        except Exception as e:
            print(f"Error recording: {e}")
            break

    stream.stop_stream()
    stream.close()
    p.terminate()

    print("Finished recording.")

    wf = wave.open(file_path, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"Recording saved to '{file_path}'.")

    # Get user details interactively
    user_name, user_sex = get_user_details()
    
    # Check if the user exists, insert if not
    user_id = db_handler.get_user_id(user_name)
    if not user_id:
        db_handler.insert_user(user_name, user_sex)
        user_id = db_handler.get_user_id(user_name)

    # Insert recording details into the database
    db_handler.insert_recording(user_id, file_path)

    # Close the database connection when done
    db_handler.close_connection()

    print("Database updated.")

# Record a new voice sample for 15 seconds and save it with an incremented filename in the 'recordings' folder
record_length = int(input("How long are you recording for? : "))
record_audio(record_length)
