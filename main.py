# Your main file
import os
import processing

# Create a dictionary mapping filenames to identities
file_identities = {
    'sample.wav': 'John',
    'sample2.wav': 'Alice',
    # Add more filenames and corresponding identities here
}

# Extract MFCC features from the 'recordings' folder
folder_path = 'recordings'
all_mfcc_features = processing.extract_mfcc_from_folder(folder_path)

# Create labels based on the filenames
labels = [file_identities[file] for file in os.listdir(folder_path) if file.endswith('.wav')]

# Train an SVM model using the extracted MFCC features and labels
svm_model, accuracy = processing.train_svm_model(all_mfcc_features, labels)

# Print the accuracy of the trained model
print(f"Accuracy of the SVM model: {accuracy * 100:.2f}%")

