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

print("DISCLAIMER: This script is intended for use on HARD DRIVES only and will NOT work effectively on Solid State Drives (SSDs).")
print("WARNING: This script will permanently destroy all data on the specified drive.")
drive = input("Enter the drive letter (e.g., D): ")

confirmation1 = input(f"Are you sure you want to erase ALL data on {drive}? This is IRREVERSIBLE. Type 'YES' to confirm: ")
if confirmation1 != "YES":
    print("Operation cancelled.")
    exit()

confirmation2 = input(f"FINAL WARNING: Are you absolutely sure you want to erase {drive}? Type 'ERASE' to confirm: ")
if confirmation2 != "ERASE":
    print("Operation cancelled.")
    exit()

print(f"Starting secure deletion of {drive}. This may take a long time...")
secure_delete(drive)
print("Secure deletion completed.")
