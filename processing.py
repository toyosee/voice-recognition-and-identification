# Using Mel-frequency cepstral coefficients (MFCCs).
# from Librosa for voice processing and recognition

import os
import librosa
import numpy as np

def extract_mfcc(audio_file):
    # Load audio file using librosa
    audio_data, sr = librosa.load(audio_file, sr=None)
    
    # Extract MFCCs
    mfccs = librosa.feature.mfcc(y=audio_data, sr=sr, n_mfcc=13)
    
    # Calculate the mean of MFCC coefficients along the time axis
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

# Example usage: Extract MFCCs from all audio files in the 'recordings' folder
folder_path = 'recordings'
all_mfcc_features = extract_mfcc_from_folder(folder_path)
print("All MFCC features shape:", all_mfcc_features.shape)
print(all_mfcc_features)
