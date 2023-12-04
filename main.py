# Main file
import os
import processing
from file_identities import file_identities

# Extract MFCC features from the 'recordings' folder
folder_path = 'recordings'
all_mfcc_features = processing.extract_mfcc_from_folder(folder_path)

# Create labels based on the filenames
labels = [file_identities[file] for file in os.listdir(folder_path) if file.endswith('.wav')]

# Train a KNN model using the extracted MFCC features and labels
knn_model, accuracy = processing.train_knn_model(all_mfcc_features, labels)

# Print the accuracy of the trained KNN model
print(f"Accuracy of the KNN model: {accuracy * 100:.2f}%")




