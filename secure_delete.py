import ctypes
import os
import random
import sys

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

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

def get_confirmation(prompt, expected_confirm):
    response = input(prompt).lower()
    if response == expected_confirm:
        return
    elif response == "cancel":
        print("Operation cancelled.")
        exit()
    else:
        print("Invalid input. Please try again.")
        get_confirmation(prompt, expected_confirm)

def is_valid_drive(drive):
    return os.path.exists(drive)

if not is_admin():
    print("This script needs to be run with administrative privileges.")
    sys.exit(1)

print("DISCLAIMER: This script is intended for use on HARD DRIVES only and will NOT work effectively on Solid State Drives (SSDs).")
print("WARNING: This script will permanently destroy all data on the specified drive.")
while True:
    drive_letter = input("Enter the drive letter (e.g., D) or type 'cancel' to exit: ").upper()
    if drive_letter.lower() == "cancel":
        print("Operation cancelled.")
        exit()
    drive = f"{drive_letter}:/"
    if is_valid_drive(drive):
        break
    else:
        print("Invalid drive letter. Please enter a valid drive letter.")

get_confirmation(f"Are you sure you want to erase ALL data on drive {drive}? This is IRREVERSIBLE. Type 'yes' to confirm or 'cancel' to exit: ", "yes")
get_confirmation(f"FINAL WARNING: Are you absolutely sure you want to erase drive {drive}? Type 'erase' to confirm or 'cancel' to exit: ", "erase")

print(f"Starting secure deletion of drive {drive}. This may take a long time...")
secure_delete(drive)
print("Secure deletion completed.")
