import pathlib
import re
from datetime import datetime

# BULK RENAMER – Day 2/84
# Renames 100s of files like "IMG_1234.jpg" → "Tesla_Event_001.jpg"
folder = pathlib.Path(".")  # current folder — drop your photos here
prefix = "Tesla_Event"
files = list(folder.glob("*.jpg")) + list(folder.glob("*.png"))

# Sort files by name (or modify to use EXIF date later)
files.sort()

for i, file in enumerate(files, start=1):
    new_name = f"{prefix}_{i:03d}{file.suffix.lower()}"
    file.rename(folder / new_name)

print(f"Renamed {len(files)} files → {prefix}_001 … {prefix}_{len(files):03d}")
print("Example: IMG_7890.JPG → Tesla_Event_023.jpg")
Day 2: Bulk renamer (100 files in 1 second) 
