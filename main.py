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


# Predict the labels (user IDs) for all features
predicted_labels = knn_model.predict(all_features)

# Create a list of user IDs for each prediction
associated_ids = []
for predicted_label in predicted_labels:
    user_id = str(predicted_label)
    associated_ids.extend([user_id] * len(file_identities[user_id]))


print(f"Accuracy of the KNN model: {accuracy * 100:.2f}%")

# Find the most common user ID in the associated IDs
most_common_id = max(set(associated_ids), key=associated_ids.count)
print(f"The ID associated with the voice with the highest match is: {most_common_id}")