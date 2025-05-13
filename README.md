# 🕒 Media Timestamp Injector

This Python tool automatically sets image EXIF data and file system timestamps based on the filename (e.g., `IMG_20230731_232323.jpg`, `VID-20231030-WA0094.mp4`). It's perfect for organizing WhatsApp or random gallery exports that have lost metadata.

---

## 📦 Features

- ✅ Parses dates from filenames like `IMG_YYYYMMDD` or `VID-YYYYMMDD`
- 📸 Injects EXIF date metadata into `.jpg` and `.jpeg` images
- 📽️ Updates file modified/access timestamps for `.mp4` and `.webp` files
- 🔒 Skips unsupported or improperly named files safely

---

## 📁 Supported Formats

- `.jpg`, `.jpeg` → EXIF updated
- `.mp4`, `.webp` → File system timestamps updated

---

## 🧑‍💻 Usage

1. **Install dependencies** (requires Python 3.x):

```bash
pip install -r requirements.txt
```

2. **Set the media folder path**

Edit the following line in `set_metadata_from_filename.py`:

```python
path = 'FOLDER_PATH'  # ⬅️ Replace with your actual folder path`
```
3. **Run the script**

```python
set_metadata_from_filename.py
```

### 🧪 Example Filenames That Work

```text
IMG_20220214_041635.jpg

VID-20231030-WA0094.mp4

IMG_20230731_232323_583.webp
```

The script extracts `YYYYMMDD` from filenames and applies that date as metadata.

## 📋 requirements.txt

```
piexif
```

## 🚫 Limitations

Filenames must contain a valid `YYYYMMDD` format.
`.jpg`/`.jpeg` files must be valid image files — corrupt files or files without EXIF support may be skipped.
WebP and MP4 files do not support embedded EXIF — only filesystem timestamps are modified.

## 📂 Project Structure

```bash
media-timestamp-injector/
├── README.md
├── requirements.txt
├── set_metadata_from_filename.py
└── samples/
    └── example-filenames.txt  # Optional demo list
```

## 📄 License

MIT License

## ✨ Credits

Built with ❤️ by [theMimikyu](https://github.com/theMimikyu) to fix messy backups and timestamp-less memories.
