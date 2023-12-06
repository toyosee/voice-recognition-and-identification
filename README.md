# voice-recognition-and-identification
An application to track voice and identify users based on their previous voices
Using KNN and librosa

First step is to run the record.py file to make 15 seconds recording each cycle.
Record timing can be edited. The more the audio files, the better the learning result.

Next, run the file_identities_creator.py to map all audio as dictionary for analysis and learning
Run main.py for learning result

HOW IT WORKS

1. Recording Voice Data:

The recording process involves capturing audio data using a microphone and saving it as a WAV file. The code (record_audio.py) utilizes the PyAudio library to record audio for a specified duration (15 seconds by default). It checks for the presence of an external microphone and saves the recorded audio files in a folder named 'recordings'. Each file is named incrementally (e.g., sample1.wav, sample2.wav).

2. Feature Extraction:

After recording, the next step is to extract essential features from the audio files. MFCCs (Mel-frequency cepstral coefficients) are a popular choice for voice recognition tasks. The processing.py file contains functions to extract MFCC features from audio files using the Librosa library. These extracted features serve as the input data for the machine learning model.

3. Database Handler:

Database operations are crucial for storing user information and their respective recordings. The DatabaseHandler class (database_handler.py) uses SQLite to create tables for Users and Recordings. It includes methods for creating tables, inserting user details and recordings, fetching user IDs, and closing the database connection.

4. File Identities:

The file_identities.py file contains a dictionary (file_identities) that maps user IDs to their respective recorded files. Each user ID is associated with a list of filenames that represent their recordings. This mapping aids in organizing and associating the recorded audio files with their respective users during model training.

5. Training the Model:

The main.py file is responsible for training the machine learning model using the extracted MFCC features. It iterates through the file_identities dictionary to associate each recording with its corresponding user ID. The MFCC features and associated labels (user IDs) are collected and used to train a KNN (K-Nearest Neighbors) classification model.

6. Analysis:

The trained KNN model is then evaluated for accuracy using a portion of the data reserved for testing. The accuracy of the model is printed, providing an estimation of how well the model performs in classifying new, unseen data based on the extracted MFCC features.

This comprehensive process outlines the stages from recording audio data to feature extraction, database handling, model training, and finally, the analysis of the trained model's accuracy. Adjustments and enhancements can be made to each step based on specific requirements or improvements in the system's performance