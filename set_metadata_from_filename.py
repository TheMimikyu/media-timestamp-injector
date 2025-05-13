from datetime import datetime
import piexif
import os
import re

# Folder containing the media files
path = 'FOLDER_PATH'
directory = os.fsencode(path)

def get_date_from_filename(filename):
    # Match IMG_YYYYMMDD or VID-YYYYMMDD
    match = re.search(r'(\d{4})(\d{2})(\d{2})', filename)
    if match:
        year, month, day = match.groups()
        return int(year), int(month), int(day)
    return None

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    filepath = os.path.join(path, filename)

    # Supported file types
    is_jpeg = filename.lower().endswith(('.jpg', '.jpeg'))
    is_video = filename.lower().endswith('.mp4')
    is_webp = filename.lower().endswith('.webp')

    if not (is_jpeg or is_video or is_webp):
        continue

    date_parts = get_date_from_filename(filename)
    if not date_parts:
        print(f"Skipped (no date found): {filename}")
        continue

    year, month, day = date_parts
    hour, minute, second = 12, 0, 0  # Default time
    new_datetime = datetime(year, month, day, hour, minute, second)

    try:
        if is_jpeg:
            exif_dict = piexif.load(filepath)
            new_date_str = new_datetime.strftime("%Y:%m:%d %H:%M:%S")
            exif_dict['0th'][piexif.ImageIFD.DateTime] = new_date_str
            exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_date_str
            exif_dict['Exif'][piexif.ExifIFD.DateTimeDigitized] = new_date_str
            exif_bytes = piexif.dump(exif_dict)
            piexif.insert(exif_bytes, filepath)
            print(f"✅ Updated EXIF date: {filename} -> {new_date_str}")
        elif is_video or is_webp:
            # Set file modified and accessed timestamps
            mod_time = new_datetime.timestamp()
            os.utime(filepath, (mod_time, mod_time))
            print(f"📁 Updated timestamps: {filename} -> {new_datetime}")
    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")
