import os
import processing
from file_identities import file_identities

folder_path = 'recordings'

all_features = []
all_labels = []

for user_id, recordings in file_identities.items():
    for recording in recordings:
        file_path = os.path.join(folder_path, recording)
        mfcc = processing.extract_mfcc(file_path)
        all_features.append(mfcc)
        all_labels.append(user_id)

knn_model, accuracy = processing.train_knn_model(all_features, all_labels, n_neighbors=1)

print(f"Accuracy of the KNN model: {accuracy * 100:.2f}%")
