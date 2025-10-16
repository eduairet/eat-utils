import os
from PIL import Image


def main():
    image_path = input("Enter the path to the image: ").strip()
    if not os.path.isfile(image_path):
        print("File does not exist.")
        return

    try:
        img = Image.open(image_path)
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    base, _ = os.path.splitext(image_path)
    ico_path = base + ".ico"

    try:
        img.save(ico_path, format="ICO")
        print(f"Icon saved as: {ico_path}")
    except Exception as e:
        print(f"Error saving .ico file: {e}")


if __name__ == "__main__":
    main()
