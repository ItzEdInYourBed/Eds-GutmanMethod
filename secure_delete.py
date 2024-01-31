import os
import random

def secure_delete(drive, passes=35):
    for root, dirs, files in os.walk(drive):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, "ba+") as f:
                    length = f.tell()
                    for _ in range(passes):
                        f.seek(0)
                        f.write(os.urandom(length))
                os.remove(file_path)
            except Exception as e:
                print(f"Error deleting file {file_path}: {e}")

def get_confirmation(prompt, exit_code):
    response = input(prompt)
    if response.lower() == exit_code:
        print("Operation cancelled.")
        exit()
    return response

def is_valid_drive(drive):
    return os.path.exists(drive)

print("DISCLAIMER: This script is intended for use on HARD DRIVES only and will NOT work effectively on Solid State Drives (SSDs).")
print("WARNING: This script will permanently destroy all data on the specified drive.")
while True:
    drive_letter = get_confirmation("Enter the drive letter (e.g., D) or type 'cancel' to exit: ", "cancel")
    drive = f"{drive_letter}:/"
    if is_valid_drive(drive):
        break
    else:
        print("Invalid drive letter. Please enter a valid drive letter.")

confirmation1 = get_confirmation(f"Are you sure you want to erase ALL data on drive {drive}? This is IRREVERSIBLE. Type 'YES' to confirm or 'cancel' to exit: ", "cancel")
if confirmation1 != "YES":
    print("Operation cancelled.")
    exit()

confirmation2 = get_confirmation(f"FINAL WARNING: Are you absolutely sure you want to erase drive {drive}? Type 'ERASE' to confirm or 'cancel' to exit: ", "cancel")
if confirmation2 != "ERASE":
    print("Operation cancelled.")
    exit()

print(f"Starting secure deletion of drive {drive}. This may take a long time...")
secure_delete(drive)
print("Secure deletion completed.")
