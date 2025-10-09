import os
import glob
from PIL import Image


def get_input(prompt, default=None):
    value = input(prompt)
    if not value and default is not None:
        return default
    return value


def main():
    dir_path = get_input("Enter directory path: ").strip()
    if not os.path.isdir(dir_path):
        print(f"Error: '{dir_path}' is not a valid directory.")
        return

    pattern = get_input("Enter file pattern (e.g. my-image-*.webp): ").strip()
    if not pattern:
        print("Error: Pattern is required.")
        return

    size_input = get_input("Enter width and height (e.g. 300 or 300x200): ").strip()
    if "x" in size_input:
        try:
            width, height = map(int, size_input.lower().split("x"))
        except Exception:
            print("Error: Invalid size format.")
            return
    else:
        try:
            width = height = int(size_input)
        except Exception:
            print("Error: Invalid size format.")
            return

    search_pattern = os.path.join(dir_path, pattern)
    files = glob.glob(search_pattern)
    if not files:
        print("No files found matching the pattern.")
        return

    print(f"Resizing {len(files)} files to {width}x{height}...")

    for file_path in files:
        try:
            with Image.open(file_path) as img:
                img = img.resize((width, height), Image.LANCZOS)
                img.save(file_path)
            print(f"Resized: {file_path}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")


if __name__ == "__main__":
    main()
