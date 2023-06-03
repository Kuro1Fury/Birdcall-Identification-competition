# Read bird_dataset_full.csv and create a list of all the audio files
import shutil

import pandas as pd
import os

ANNOTATIONS_FILE = "bird_dataset_full.csv"
annotations = pd.read_csv(ANNOTATIONS_FILE)
# Create a list for the first column
desired_classes = annotations.iloc[:, 0].tolist()
desired_classes = list(set(desired_classes))
print(desired_classes)
print(len(desired_classes))

train_file = "train.csv"
train_dataset = pd.read_csv(train_file)
# Find corresponding ebird_code for desired_classes
filtered_dataset = train_dataset[train_dataset['species'].str.upper().isin(desired_classes)]

# Create a dictionary to store the correspondence between ebird_codes and species names
correspondence_dict = {}

# Iterate over the filtered dataset and populate the correspondence dictionary
for index, row in filtered_dataset.iterrows():
    ebird_code = row['ebird_code']
    species = row['species'].upper()
    correspondence_dict[ebird_code] = species

# Print the correspondence dictionary
for ebird_code, species in correspondence_dict.items():
    print(f"Ebird Code: {ebird_code}, Species: {species}")

# Get the ebird_code values for the filtered dataset
ebird_codes = filtered_dataset['ebird_code'].tolist()
ebird_codes = list(set(ebird_codes))

# Print the ebird_codes
print(sorted(ebird_codes))
print(len(ebird_codes))

# print the ebird_codes in the sorted order
train_folder = "train"

folders = os.listdir(train_folder)

# # Iterate over the folders and delete the ones not in ebird_codes
# for folder in folders:
#     folder_path = os.path.join(train_folder, folder)
#     if folder not in ebird_codes and os.path.isdir(folder_path):
#         print(f"Deleting folder: {folder_path}")
#         # Delete the folder and its contents recursively
#         shutil.rmtree(folder_path)

# for ebird_code, species in correspondence_dict.items():
#     folder_path_old = os.path.join(train_folder, ebird_code)
#     folder_path_new = os.path.join(train_folder, species)
#     if os.path.isdir(folder_path_old):
#         print(f"Renaming folder: {folder_path_old} to {folder_path_new}")
#         # Rename the folder
#         os.rename(folder_path_old, folder_path_new)


# bird_count = pd.read_csv("bird_count.csv")
# # only keep the rows with ebird_code in ebird_codes
# filtered_bird_count = bird_count[bird_count['ebird_code'].isin(ebird_codes)]
# print(filtered_bird_count)
# # Reindex the dataframe
# filtered_bird_count = filtered_bird_count.reset_index(drop=True)
# # Convert the ebird_code to species name
# filtered_bird_count['ebird_code'] = filtered_bird_count['ebird_code'].map(correspondence_dict)
# print(filtered_bird_count)
# # Save the filtered_bird_count to a csv file
# filtered_bird_count.to_csv("filtered_bird_count.csv", index=False)

# # Revert the map
# correspondence_dict = {v: k for k, v in correspondence_dict.items()}
#
# metadata = pd.read_csv("meta.csv")
# # convert the species name to ebird_code
# metadata['bird'] = metadata['bird'].map(correspondence_dict)
# print(metadata)
# # Save the metadata to a csv file
# metadata.to_csv("filtered_meta.csv", index=False)



# Get names of all amp files in the mel folder
# mel_folder = "mel"
# mel_files = os.listdir(mel_folder)
# mel_files = [file for file in mel_files if file.endswith(".amp")]
# print(mel_files)
# print(len(mel_files))
#
# metadata = pd.read_csv("meta.csv")
# files = metadata['file'].tolist()
# # change .mp3 to .amp
# files = [file.replace(".mp3", ".amp") for file in files]
# print(files)
# print(len(files))
# # Find common files between mel_files and meta[file]
# common_files = list(set(mel_files).intersection(files))
# print(common_files)
# print(len(common_files))


# change metadata['file'] to .amp
metadata = pd.read_csv("filtered_meta.csv")
metadata['file'] = metadata['file'].str.replace(".mp3", ".amp")
print(metadata)
# Save the metadata to a csv file
metadata.to_csv("filtered_meta_amp.csv", index=False)

