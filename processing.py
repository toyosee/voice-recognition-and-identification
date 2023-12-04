# Using Mel-frequency cepstral coefficients (MFCCs).
# from Librosa for voice processing and recognition

# processing.py

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import librosa
import numpy as np
import os

def extract_mfcc(audio_file):
    # Loading audio file using librosa
    audio_data, sr = librosa.load(audio_file, sr=None)
    
    # Extracting MFCCs
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sr, n_mfcc=13)
    
    # Calculating the mean of MFCC coefficients along the time axis
    mfccs_mean = np.mean(mfccs.T, axis=0)
    
    return mfccs_mean

def extract_mfcc_from_folder(folder_path):
    mfcc_features = []
    
    # Get a list of all files in the folder
    audio_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
    
    for file in audio_files:
        file_path = os.path.join(folder_path, file)
        # Extract MFCC features for each audio file
        mfcc = extract_mfcc(file_path)
        mfcc_features.append(mfcc)
    
    return np.array(mfcc_features)

def train_knn_model(X, y):
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the KNN classifier
    knn_classifier = KNeighborsClassifier(n_neighbors=5)  # You can adjust the number of neighbors

    # Train the KNN classifier
    knn_classifier.fit(X_train, y_train)

    # Evaluate the trained model
    accuracy = knn_classifier.score(X_test, y_test)
    return knn_classifier, accuracy
