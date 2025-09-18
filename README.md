# Eat Utils

Utils for productivity.

## Instructions

1. Create a virtual environment:
   ```bash
   python -m venv .env
   ```
2. Activate the virtual environment:
   - On Windows:
     ```bash
     .env\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source .env/bin/activate
     ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the desired script from the `scripts` directory.
   ```bash
   python your_script.py
   ```
5. Update `requirements.txt` if you install new packages:
   ```bash
   pip freeze > requirements.txt
   ```
6. Deactivate the virtual environment when done:
   ```bash
   deactivate
   ```

## Available Scripts

- [compress-pdf](./scripts/compress-pdf/main.py): Compress PDF files in the `pdfs` directory and save them to the `compressed_pdfs` directory.
