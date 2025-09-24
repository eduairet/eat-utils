import os
from PIL import Image
from pathlib import Path


def is_image_file(file_path):
    image_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff", ".gif"]
    return file_path.suffix.lower() in image_extensions


def convert_to_webp(src_path):
    dst_path = src_path.with_suffix(".webp")
    try:
        with Image.open(src_path) as img:
            img.save(dst_path, "WEBP")
        print(f"Converted: {src_path} -> {dst_path}")
    except Exception as e:
        print(f"Failed to convert {src_path}: {e}")


def process_folder(folder_path):
    for entry in os.scandir(folder_path):
        if entry.is_file():
            file_path = Path(entry.path)
            if is_image_file(file_path):
                convert_to_webp(file_path)


def main():
    path_input = input("Enter the path to a folder or image file: ").strip()
    path = Path(path_input)
    if not path.exists():
        print("Path does not exist.")
        return
    if path.is_dir():
        process_folder(path)
    elif path.is_file():
        if path.suffix.lower() == ".webp":
            print("File is already in webp format.")
        elif is_image_file(path):
            convert_to_webp(path)
        else:
            print("File is not a supported image format.")
    else:
        print("Invalid path.")


if __name__ == "__main__":
    main()
