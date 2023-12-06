# Using Mel-frequency cepstral coefficients (MFCCs).
# from Librosa for voice processing and recognition

# processing.py

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import librosa
import numpy as np
import os

def extract_mfcc(audio_file):
    audio_data, sr = librosa.load(audio_file, sr=None)
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sr, n_mfcc=13)
    mfccs_mean = np.mean(mfccs.T, axis=0)
    return mfccs_mean

def extract_mfcc_from_folder(folder_path):
    mfcc_features = []
    audio_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
    for file in audio_files:
        file_path = os.path.join(folder_path, file)
        mfcc = extract_mfcc(file_path)
        mfcc_features.append(mfcc)
    return np.array(mfcc_features)

def train_knn_model(X, y, n_neighbors=3):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    knn_classifier = KNeighborsClassifier(n_neighbors=n_neighbors)
    knn_classifier.fit(X_train, y_train)
    accuracy = knn_classifier.score(X_test, y_test)
    return knn_classifier, accuracy
