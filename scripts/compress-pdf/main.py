import os
import sys
from pathlib import Path
import fitz
import winreg
import io
from PIL import Image


def get_downloads_folder():
    if sys.platform == "win32":
        sub_key = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders"
        downloads_guid = "{374DE290-123F-4565-9164-39C4925E467B}"
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, sub_key) as key:
            downloads = winreg.QueryValueEx(key, downloads_guid)[0]
        return Path(downloads)
    else:
        return Path.home() / "Downloads"


def compress_pdf(input_path, output_path):
    doc = fitz.open(input_path)
    for page in doc:
        images = page.get_images(full=True)
        if not images:
            continue  # Skip pages without images
        for img in images:
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]
            pil_img = Image.open(io.BytesIO(image_bytes))
            pil_img = pil_img.convert("RGB")
            new_size = (int(pil_img.width * 0.7), int(pil_img.height * 0.7))
            pil_img = pil_img.resize(new_size, Image.LANCZOS)
            buf = io.BytesIO()
            pil_img.save(
                buf, format="JPEG", quality=40
            )  # Lower quality for smaller size
            new_img_bytes = buf.getvalue()
            doc.update_image(xref, new_img_bytes)
    # Remove metadata and clean up PDF
    doc.set_metadata({})
    doc.save(output_path, deflate=True, garbage=4, clean=True)
    doc.close()


def main():
    input_pdf = input("Enter the path to the PDF file: ").strip()
    if not os.path.isfile(input_pdf):
        print("File not found.")
        return

    downloads_folder = get_downloads_folder()
    output_pdf = downloads_folder / f"compressed_{Path(input_pdf).name}"

    try:
        compress_pdf(input_pdf, output_pdf)
        print(f"Compression completed. File saved to: {output_pdf}")
    except Exception as e:
        print(f"Error compressing PDF: {e}")


if __name__ == "__main__":
    main()
